
.equ CSR_USTATUS, 0                     # CSR ustatus
.equ CSR_UIE, 4                         # CSR uie
.equ CSR_UTVEC, 5                       # CSR utvec
.equ CSR_UCAUSE, 66                     # CSR ucause

.equ USER_IE, 0x00000001                # User level interrupts enabled

.equ USER_TI_BITMASK, 0x00000008        # User level timer interrupt bit mask
.equ USER_EI_BITMASK, 0x00000080        # User level external interrupt bit mask

.equ USER_TI_EXCEPCODE, 4               # User software interrupt exception code
.equ USER_EI_EXCEPCODE, 8               # User external interrupt exception code

.equ REG_KBD_CTRL, 0xFFFF0000           # Keyboard control register
.equ REG_KBD_DATA, 0xFFFF0004           # Keyboard data register
.equ KDB_CTRL_IEBM, 0x00000003          # Keyboard interrupt enabled bit mask
.equ REG_DISP_CTRL, 0xFFFF0008          # Display control register
.equ REG_DISP_DATA, 0xFFFF000C          # Display data register
.equ REG_TIME, 0xFFFF0018               # time register
.equ REG_TIMECMP, 0xFFFF0020            # timecmp register

.kdata
kstack:         .space 4000             # User stack

.section .data
.align 4
str:
                .asciz "Timer "         # "Timer x: MM:SS\n"
colon:          .byte 0x3A              # ascii ':'
line_feed:      .byte 0x0A              # ascii '\n'
quit_char:      .byte 0x71              # ascii 'q'
at_char:        .byte 0x40              # ascii '@'
timers_count:
                .word 0x000006          # Amount of timers
timers_remaining_seconds:
                .word 0, 0, 0, 0, 0, 0  # Array of 6 remaining seconds
row:            .4byte 0
col:            .4byte 0
buf:            .space 4000             # Hold key sequence

.section .text
.global main
main:
        addi    sp, sp, -4
        sw      ra, 0(sp)
        
        ; csrrw   s0, 0x140, s0           # kernal stack
        ; la      s0, kstack                 
        ; addi    s0, s0, -128
        ; csrrw   s0, 0x140, s0
                 
        jal     ra, disp_init_content   # Display all timers init info

# Init interrupts
# Setup trap vector
1:      auipc   t0, %pcrel_hi(handler)  # load mtvec(hi)
        addi    t0, t0, %pcrel_lo(1b)   # load mtvec(lo)
        csrrw   zero, CSR_UTVEC, t0

# Enable user level interrupts
# Set ustatus.UIE=1 (enable U mode interrupt)
        li      t0, USER_IE
        csrrs   zero, CSR_USTATUS, t0

# Enable timer interrupt
# set mie.MTIE=1 (enable U mode timer interrupts)
        li      t0, 128
        csrrs   zero, CSR_UIE, t0

# Enable keyboard interrupt
# Set uie.UEIE=1 (enable U mode external interrupts)
        csrr    t0, CSR_UIE
        ori     t0, USER_EI_BITMASK
        csrs    CSR_UIE, t0

# read from RTC time
        li      a0, REG_TIME
        ld      a1, 0(a0)

# write to utimecmp
        li      a0, REG_TIMECMP
        li      t0, 1000                # 1000 milliseconds
        add     a1, a1, t0
        sd      a1, 0(a0)

loop:
        lw      t0, REG_KBD_CTRL        # Disable kbd
        lw      t1, KDB_CTRL_IEBM        
        not     t1, t1
        and     t1, t0, t1  
        sw      t1, REG_KBD_CTRL
        la      t6, buf                 # check quit command
        lb      t5, 0(t6)
        ori     t5, 0x20
        li      t4, quit_char           # load ascii 'q'
        and     t5, t5, t4              # compare with 'q' or 'Q'
        beq     t5, t4, done
        lw      t0, REG_KBD_CTRL        # Enable kbd
        ori     t1, t0, KDB_CTRL_IEBM
        sw      t1, REG_KBD_CTRL
        
        j       loop
done:
        lw      ra, 0(sp)
        addi    sp, sp, 4
        jr      ra


# Interrupts handler
# Wait for key to modify timer or quit
# To modify timer, the key sequence must like "123@5\n"
# Or "q" to quit handler
# Time interrupt invoked in every one second
# Otherwise exception is raised
handler:
        csrrc   t0, CSR_UCAUSE, zero
        bgez    t0, fail                # interrupt causes are less than zero
        slli    t0, t0, 1               # shift off high bit
        srli    t0, t0, 1

        li      t1, USER_EI_EXCEPCODE   # Check interrupt type
        and     t2, t0, t1
        beq     t2, t1, external_ir
        li      t1, USER_TI_EXCEPCODE
        and     t2, t0, t1
        beq     t2, t1, timer_ir
        j       unknown
external_ir:
        lw      t1, REG_KBD_CTRL
        li      t2, KDB_CTRL_IEBM
        and     t1, t1, t2
        beqz    t1, is_kbd
        j       unknown
is_kbd:
        li      a7, REG_KBD_DATA
        jal     ra, append_key
        la      t6, buf                 # buffer of key sequence
        lb      t5, 0(t6)
        or      t3, t5, 0x20
        li      t4, quit_char           # If 1st char is 'q' or 'Q'
        and     t3, t3, t4
        beq     t3, t4, done
        li      t4, line_feed           # If 1st char is '\n'
        and     t3, t5, t4
        beq     t3, t4, enable_kbd
        lb      t5, a7
        or      t3, t5, t4
        la      a7, buf
        beq     t3, t4, parse_string    # if current key is '\n'
enable_kbd:   
        lw      t0, REG_KBD_CTRL
        ori     t1, t0, KDB_CTRL_IEBM
        sw      t1, REG_KBD_CTRL
        j       pass       
         
timer_ir:
        li      a0, REG_TIME
        lw      a1, 0(a0)
        li      a0, REG_TIMECMP
        addi    a1, a1, 1000            # 1000 milliseconds
        sw      a1, 0(a0)

        li      a7, timers_count
        la      a6, times_remaining_seconds
        jal     ra, countdown_all
        li      s11, timers_count
        li      s10, times_remaining_seconds
        li      a7, 0
loop_timer:
        beq     a7, s11, pass
        lw      a6, 0(s10)
        jal     ra, display_time
        addi    a7, a7, 1        
        addi    s10, s10, 4
        j       loop_timer
pass:
        csrr    t0, CSR_USTATUS
        ori     t1, t0, USER_IE
        csrs    CSR_USTATUS, t1
        j       done
unknown:
        nop
        j       done
fail:
        nop
        j       done
done:
        uret

# Parse key sequence whether it should separate into time and timer index
# For example, "9@0", "10@1", "100@3", "3599@5"
# Separate char '@' its position in string >0 and <5
# time should >= 0 and < 3600, timer index should >=0 and <6
# Reg param:
#  a7: buf addr
# 
parse_string:
        la      t6, buf
        li      s11, 4000
        li      s10, 0
        li      s9, 5                   # separate char position
        li      s8, 3600                # max time value
        li      s7, 6                   # max timer count
        li      s6, line_feed           # ascii '\n'
        li      a0, at_char             # ascii '@'
        li      a1, 10                  # decimal base 10
        li      a2, 0                   # parsed time
        li      a3, 6                   # parsed timer index
loop_separate:
        beq     s10, s11, fail
        lb      t5, 0(t6)
        beq     t5, a0, separate_done
        addi    t6, t6, 1
        addi    s10, s10, 1
        j       loop_separate 
separate_done:
        beqz    s10, fail               # '@' is not 1st char of string
        bge     s10, s9, fail           # '@' is not in last 2 chars
        li      t0, 0
        la      t6, buf
loop_time:
        beq     t0, s10, time_done
        lb      t5, 0(t6)
        blt     t5, 0x30, fail          # Not digit < '0'
        bge     t5, 0x40, fail          # Not digit > '9'
        div     a2, a2, a1              # * 10
        add     a2, a2, t5
        addi    t6, t6, 1
        addi    t0, t0, 1
        j       loop_time
time_done:
        bge     a2, s8, fail            # time >= 3600
        addi    t6, t6, 1               # skip "@"
        addi    t0, s10, 1
index_loop:
        beq     t0, s11, index_done
        lb      t5, 0(t6)
        blt     t5, 0x30, fail          # Not digit < '0'
        bge     t5, 0x40, fail          # Not digit > '9'
        beq     t5, s6, index_done      # Meet '\n'
        div     a3, a3, a1              # * 10
        add     a3, a3, t5        
        addi    t6, t6, 1
        addi    t0, t0, 1
        j       index_loop
index_done:
        bge     a3, s7, fail            # invalid timer index
        la      t6, timers_remaining_seconds
        li      t0, 0
loop:
        beq     t0, a3, pass
        addi    t6, t6, 4
        addi    t0, t0, 1
        j       loop
pass:
        sw      a2, 0(t6)
        jal     ra, clear_buf
        lw      a7, a3
        lw      a6, a2
        jal     ra, display_time
        j       done
fail:
        nop        
done:
        ret

# Append key into buf
# Reg param:
#   a7: ascii
#
append_key:
        la      t6, buf
        li      s11, 4000
        li      s10, 0
loop:
        beq     s10, s11, fail
        lb      t5, 0(t6)
        beqz    t5, pass
        addi    t6, t6, 1
        addi    s10, s10, 1
        j       loop 
pass:
        sb      a7, 0(t6)
        j       done
fail:
        nop
done:
        ret


# Fill the buffer with 0
#
clear_buf:
        la      t6, buf
        li      a7, 0
        li      s11, 4000
        li      s10, 0
loop:
        beq     s10, s11, done
        lb      t5, 0(t6)
        beqz    t5, done
        sb      a7, 0(t6)
        addi    t6, t6, 1
        addi    s10, s10, 1
        j loop
done:
        ret


# Loop to display all timers init information
# str addr is registered into t0
# timer number is registered into t6, and ascii is registed into t1
# timers left seconds are registed into s4(addr) and a0(value)
display_init_content:     
        addi    sp, sp, -128            # Enlarge stack to push register
        sw      s0, 76(sp)
        lw      s0, sp     
        sw      a7, 0(s0)
        sw      a6, 4(s0)
        sw      a5, 8(s0)
        sw      s11, 32(s0)
        sw      s10, 36(s0)
        sw      t0, 80(s0)
        sw      t5, 100(s0)
        sw      t6, 104(s0)

        la      t0, row
        lw      a7, 0(t0)
        la      t0, col
        lw      a6, 0(t0)
          
        li      s11, timers_count            
        la      s10, timers_remaining_seconds              

        li      t6, 0                   # Timer index [0, ..., 5]
        la      t5, str                 # Leading message addr
1:      beq     t6, s11, 2f             # Loop timers index
        jal     ra, move_cursor         # move cursor to left upper
        lw      a5, a6
        lw      a6, a7
        la      a7, t5                  # Leading message addr
        jal     ra, put_string
        addi    a7, t6, 0x30            # Encode timer number with ascii
        jal     ra, put_char
        li      a7, colon
        jal     ra, put_char
        li      a7, 0x20                # To show sperate space
        jal     ra, put_char
        lw      a7, 0(s10)              # remaining seconds of current timer
        jal     ra, display_time
        li      a7, line_feed
        jal     ra, put_char
        addi    t6, t6, 1               # Process next timer
        addi    s10, s10, 4
        addi    a7, a6, 0                  
        addi    a6, a5, 0                      
		j       1b
2:                                      # Done loop
        la t0, row
        sw a6, 0(t0)
        la t0, col
        sw a5, 0(t0)
        lw a7, 0(s0)
        lw a6, 4(s0)
        lw a5, 8(s0)
        lw s11, 32(s0)
        lw s10, 46(s0)
        lw t0, 80(s0)
        lw t5, 100(s0)
        lw t6, 104(s0)
        lw s0, 76(sp)
        addi sp, sp, 128                # Free memory in stack
        ret
        

# Display string (ended with null)
# Reg param:
#   a7: String address
#   a6: Cursor row
#   a5: Cursor col
# Reg returned:
#   a6: New cursor row
#   a5: New cursor col
# Exception:
#   n/a
put_string:
        addi sp, sp, -128               # Enlarge stack   
        sw s0, 76(sp)
        lw s0, sp     
        sw a7, 0(s0)                    # Push
        sw a6, 4(s0)
        sw a5, 8(s0)
        sw s11, 32(s0)
        sw s10, 36(s0)
        sw s9, 40(s0)
        sw t0, 80(s0)
        sw t1, 84(s0)
        lw s11, a7
        lw s10, a6
        jw s9, a5
        nop
        lw t0, a7
1:                                      # Loop char
        lb t1, 0(t0)                    
        beqz t1, 2f
        lw a7, t1
        jal ra, put_char
        addi t0, t0, 1                 
        lw s10, a6                      # New row returned by put_char
        lw s9, a5                       # New col returned by put_char
        j 1b
2:                                      # Done loop
        lw a7, 0(s0)                    # Pop
        ; lw a6, 4(s0)
        ; lw a5, 8(s0)
        lw s11, 32(s0)
        lw s10, 36(s0)
        lw s9, 40(s0)
        lw t0, 80(s0)
        lw t1, 84(s0)
        lw s0, 76(sp)
        addi sp, sp, 128                # Shrink stack
        ret
            
    
# Display a char
# Char are alphabets, numbers, and symbols
# It only move cursor if char is line feed, otherwise fail
# Reg param:
#   a7: char
#   a6: row
#   a5: column
# Reg returned:
#   a6: new row by cursor
#   a5: new col by cursor
# Exception:
#   Char is not a alphabet/digit/punctuation or such control (\t, ' ', \n)      
put_char:
        addi sp, sp, -128               # Allocate memory in stack
        sw s0, 76(sp)
        lw s0, sp
        sw a7, 0(s0)                    # Push
        sw a6, 4(s0)
        sw a5, 8(s0)
        sw s6, 52(s0)
        sw s5, 56(s0)
        li s6, 0xFF                     # ascii 127, control code
        li s5, 0x20                     # ascii 20, space code
        bge a7, s6  1f
        blt a7, s5, 1f
poll:   lw t2, REG_DISP_CTRL            
        beqz t2, poll                   # Check ready status of displayer
        li t3, REG_DISP_DATA            
        lb t1, a7
        sw t1, 0(t3)                    # Write a char into mm of displayer
1:      li t4, line_feed
        bne a7, t4, fail
        addi a7, a6, 1
        lw a6, 0
        jal ra, move_cursor
        lw a5, a6
        lw a6, a7
        j pass
fail:
        nop
pass:
        lw a7, 0(s0)                    # Pop
        ; lw a6, 4(s0)
        ; lw a5, 8(s0)
        lw s6, 52(s0)
        lw s5, 56(s0)
        ; lw t1, 4(sp)
        lw s0, 76(sp)
        addi sp, sp, 128                # Free memory in stack
        ret        
            
    
# Move display cursor
# Reg param:
#   a7: row
#   a6: column     
# Exception:
#   row is exceeded
#   col is exceeded 
move_cursor:
        addi sp, sp, -128               # Allocate memory in stack to push register
        sw a7, 0(sp)                    # Push
        sw a6, 4(sp)
        sw s11, 32(sp)
        sw t6, 80(sp)
        sw t5, 84(sp)
        li s11, 0x00008000
        bge a7, s11, fail
        bge a6, s11, fail
        lb t6, a7                       # Format row and col to send
        slli t6, 24
        lb t5, a6
        slli t5, 12
        add t6, t6, t5
        addi t6, t6, 0x07 
poll:   lw t5, REG_DISP_CTRL            
        beqz t5, poll                   # Check ready status of displayer
        li t5, REG_DISP_DATA            
        sw t6, 0(t5)                    # Send into mmr of displayer
        j pass
fail:
        nop
pass:
        lw a7, 0(sp)                    # Pop
        lw a6, 4(sp)
        lw s11, 32(sp)
        lw t6, 80(sp)
        lw t5, 84(sp)
        addi sp, sp, 128                # Free memory in stack
        ret        


# Count all timers its time >0 then decrement with 1 second till to 0,
# and response modification into screen
# Reg param:
#   a7: Timers count, aka 6
#   a6: Array of remaining seconds addresses
# Exception:
#
countdown_all:
        addi sp, sp, -128               # addi s0, s0, -128     # Stack
        sw a7, 0(sp)                    # Push
        sw a6, 4(sp)
        sw s11, 32(sp)
        sw s10, 36(sp)
        sw s9, 40(sp)
        sw t6, 96(sp)
        sw t5, 100(sp)
        li t6, 0                        # Loop index [0:5] for timers number
        lw s11, a7                      
        lw s10, a6                      
1:                                      # Loop timer
        beq t6, a7, 2f
        li t5, 0(a6)                    
        beqz t5, 2f
        addi t5, t5, -1
        sw t5, 0(a6)                    # Save new time
        lw s9, a6                       # Store value temporary
        lw a7, t6                       # show time arguments
        lw a6, t5
        jal ra, display_time
        lw a6, s9                       # Restore value
        lw a7, s11
2:                                      # Next timer
        addi t6, t6, 1
        addi a6, a6, 4        
        j 1b
3:                                      # Done loop
        lw a7, 0(sp)
        lw a6, 4(sp)
        lw s11, 32(sp)
        lw s10, 36(sp)
        lw s9, 40(sp)
        lw t6, 96(sp)
        lw t5, 100(sp)
        addi sp, sp, 128
        ret


# Display remaining time for speified timer number
# Register param: 
#   a7: timer number, also meaning row that display cursor should move to
#   a6: remaining seconds
# Exception:
#   Invalid timer number
#   Time is out of bounds
display_time:
        addi sp, sp, -128
        sw a7, 0(sp)
        sw a6, 4(sp)
        sw a5, 8(sp)
        sw a3, 16(sp)
        sw a2, 20(sp)
        sw a1, 24(sp)
        sw a0, 28(sp)
        sw s11, 32(sp)
        sw s10, 36(sp)
        sw s9, 40(sp)
        sw s8, 44(sp)
        sw s7, 48(sp)
        sw t0, 80(sp)
        sw t1, 84(sp) 

        lw s11, a7                       
        lw s10, a6
        lw s9, 9                        # The 1st column to show time
        li s8, 60                       # Minite base (60 seconds)
        li s7, 10                       # Decimal base 10

        div t0, a6, s8                  # Calculate timer count into minutes and seconds
        rem t1, a6, s8
        div a0, t0, s7                  # Calculate minutes
        rem a1, t0, s7
        div a2, t1, s7                  # Calculate seconds
        rem a3, t1, s7

        lw a7, s11                      # Row to cursor
        lw a6, s9                       # Col to cursor
        jal ra, move_cursor
        addi s0, a6, 1                  # Save new col 
        addi a5, a6, 0
        addi a6, s11, 0
        addi a7, a0, 0x30
        jal ra, put_char
        
        lw a7, s11
        lw a6, s0
        jal ra, move_cursor
        addi s0, a6, 2
        addi a5, a6, 0
        addi a6, s11, 0
        addi a7, a1, 0x30
        jal ra, put_char
        
        lw a7, s11
        lw a6, s0
        jal ra, move_cursor
        addi s0, a6, 1
        addi a5, a6, 0
        addi a6, s11, 0
        addi a7, a2, 0x30
        jal ra, put_char
        
        lw a7, s11
        lw a6, s0
        jal ra, move_cursor
        addi a5, a6, 0
        addi a6, s11, 0
        addi a7, a3, 0x30
        jal ra, put_char

        lw a7, 0(sp)
        lw a6, 4(sp)
        lw a5, 8(sp)
        lw a3, 16(sp)
        lw a2, 20(sp)
        lw a1, 24(sp)
        lw a0, 28(sp)
        lw s11, 32(sp)
        lw s10, 36(sp)
        lw s9, 40(sp)
        lw s8, 44(sp)
        lw s7, 48(sp)
        lw t0, 80(sp)
        lw t1, 84(sp)         
        addi sp, sp, 128
        ret
