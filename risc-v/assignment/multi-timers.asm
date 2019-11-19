
; .kdata
; kstack: .space 4000                     # Stack addr

.equ CSR_USTATUS, 0                     # CSR ustatus
.equ CSR_UIE, 4                         # CSR uie
.equ CSR_UTVEC, 5                       # CSR utvec
.equ CSR_UCAUSE, 66                     # CSR ucause

.equ USER_IE, 0x00000001                # User level interrupts enabled

.equ USER_TI_BITMASK, 0x00000004        # User level timer interrupt bit mask
.equ USER_EI_BITMASK, 0x00000008        # User level external interrupt bit mask

.equ USER_TI_EXCEPCODE, 4               # User software interrupt exception code
.equ USER_EI_EXCEPCODE, 8               # User external interrupt exception code

.equ REG_KBD_CTRL, 0xFFFF0000           # Keyboard control register
.equ REG_KBD_DATA, 0xFFFF0004           # Keyboard data register
.equ REG_DISP_CTRL, 0xFFFF0008          # Display control register
.equ REG_DISP_DATA, 0xFFFF000C          # Display data register
.equ REG_TIME, 0xFFFF0018               # time register
.equ REG_TIMECMP, 0xFFFF0020            # timecmp register


.section .data
.align 2
str:
        .asciz "Timer "                 # "Timer x: MM:SS\n"
.align 2
colon:  .byte 0x3A                      # ascii ':'
.align 2
line_feed .byte 0x0A                    # ascii '\n'
.align 2
timers_count
        .word 0x000006                  # Amount of timers
timers_remaining_seconds
        .word 0, 0, 0, 0, 0, 0          # Hold remaining seconds for all 6 timers

.section .text
.global main
main:
        la s0, sp                       # la s0, kstack         # Stack     
        li s10, timers_count            
        la s11, timers_remaining_seconds              
        jal display_time                # Display initial timers

# Init keyboard
INIT_KBD:

# Setup keyboard trap vector
1:      auipc   t0, %pcrel_hi(handler)             # load mtvec(hi)
        addi    t0, t0, %pcrel_lo(1b)                       # load mtvec(lo)
        csrrw   zero, CSR_UTVEC, t0

# Enable user level interrupts
# Set ustatus.UIE=1 (enable U mode interrupt)
        li      t0, USER_LEVEL_IE
        csrrs   zero, CSR_USTATUS, t0

# Enable keyboard interrupt
# set uie.UEIE=1 (enable U mode external interrupts)
        csrr t0, CSR_UIE
        ori  t0, USER_LEVEL_EIBM
        csrs CSR_UIE, t0


# set mie.MTIE=1 (enable U mode timer interrupts)
        li      t0, 128
        csrrs   zero, mie, t0

        jal ra, INIT_KBD                # Enable keyboard ()
    
done_return:
        jr ra, 0
   

# Display all timers
# str addr is registered into t0
# timer number is registered into t6, and ascii is registed into t1
# timers left seconds are registed into s4(addr) and a0(value)
display_timer:     
        addi s0, s0, -120               # Allocate memory in stack to push register        
        sw t0, 0(s0)
        sw t1, 4(s0)
        sw t6, 24(s0)
        sw s1, 44(s0)
        sw s2, 48(s0)
        sw s3, 52(s0)
        sw s4, 56(s0)
        sw a0, 80(s0)
        sw a1, 84(s0)
        sw a2, 88(s0)
        sw a3, 92(s0)
        sw a4, 96(s0)
        sw a5, 100(s0)
        sw a6, 104(s0)
        li s1, timers_count            
        li s2, 60                       # Minite base (60 seconds)
        li s3, 10                       # Decimal base 10
        la s4, timers_remaining_seconds              
        li t6, 0                        # Timer index [0, ..., 5]
1:      beq t6, s1, 2f                  # Loop timers
        la t0, str                      # Message addr to output
        jal ra, put_string
        addi t1, t6, 0x30               # Encode timer number with ascii
        jal ra, put_char
        li t1, colon
        jal ra, put_char
        li t1, 0x20                     # To show sperate space
        jal ra, put_char
        lw  a0, 0(s4)                   # seconds left of current timer
        div a1, a0, s2                  # Calculate timer count into minutes and seconds
        rem a2, a0, s2
        div a3, a1, s3                  # Calculate minutes
        rem a4, a1, s3
        div a5, a2, s3                  # Calculate seconds
        rem a6, a2, s3
        addi t1, a3, 0x30
        jal ra, put_char
        addi t1, a4, 0x30
        jal ra, put_char
        li t1, colon
        jal ra, put_char
        addi t1, a5, 0x30
        jal ra, put_char
        addi t1, a6, 0x30
        jal ra, put_char
        li t1, line_feed
        jal ra, put_char
        addi t6, t6, 1                  # Process next timer
        addi s4, s4, 4
		j 1b
2:      nop                             # Done loop
        lw t0, 0(s0)
        lw t1, 4(s0)
        lw t6, 24(s0)
        lw s1, 44(s0)
        lw s2, 48(s0)
        lw s3, 52(s0)
        lw s4, 56(s0)
        lw a0, 80(s0)
        lw a1, 84(s0)
        lw a2, 88(s0)
        lw a3, 92(s0)
        lw a4, 96(s0)
        lw a5, 100(s0)
        lw a6, 104(s0)
        addi s0, s0, 120                # Free memory in stack
        ret
        
# Display remaining time for speified timer number
# Register param: 
#   a7: timer number
#   a1: remaining seconds
# Exception:
#   Invalid timer number
#   Time is out of bounds
show_time:


        ret

# Display string (ended with null)
# The string address is registered in t0
put_string:
        addi s0, s0, -8                 # Allocate memory in stack to push register        
        sw t1, 0(s0)                    # Push
1:      lb t1, 0(t0)                    # Loop char
        beqz t1, 2f
        jal ra, put_char
        addi t0, t0, 1                  # Traverse addresses for each char in message
        j 1b
2:      nop                             # Done loop
        lw t1, 0(s0)                    # Pop
        addi s0, s0, 8                  # Free memory in stack
        ret
            
    
# Display a char
# The char registered in t1      
put_char:
        addi s0, s0, -16                # Allocate memory in stack to push register
1:      sw t1, 0(s0)                    # Push
        sw t2, 4(s0)
        sw t3, 8(s0)
        ; sw t4, 12(s0)
poll:   lw t2, REG_DISP_CTRL            
        beqz t2, poll                   # Check ready status of displayer
        li t3, REG_DISP_DATA            
        sw t1, 0(t3)                    # Write a char into mm of displayer
2:      ; lw t4, 12(s0)                 # Pop
        lw t3, 8(s0)
        lw t2, 4(s0)
        lw t1, 0(s0)
        addi s0, s0, 16                 # Free memory in stack
        ret        



# Wait for key to invoke timer or quit
# To invoke timer, the key sequence must be "123@5\n"
# Or "q\n" to shutdown program
# Otherwise raise exception
handler:
        csrrc  t0, CSR_UCAUSE, zero
        bgez t0, fail                   # interrupt causes are less than zero
        slli t0, t0, 1                  # shift off high bit
        srli t0, t0, 1
        li t1, USER_TI_EXCEPCODE        # check this is an u_timer interrupt
        beq t0, t1, timer_pass
        j timer_pass
        li t1, USER_EI_EXCEPCODE        # check this is an u_external interrupt
        bne t0, t1, fail

timer_pass:
        la a0, pass_msg
        jal puts
        j shutdown

unknown:

        j shutdown

fail:
        la a0, fail_msg
        jal puts
        j shutdown
    
shutdown:
        uret


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
        lw s9, a6                       # Store value temporary
        lw a7, t6                       # show time arguments
        lw a6, t5
        jal show_time
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