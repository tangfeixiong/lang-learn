
.kdata
kstack: .space 4000                     # Stack addr


.equ REG_DISP_CTRL, 0xFFFF0008          # Display control register
.equ REG_DISP_DATA, 0xFFFF000C          # Display data register
.equ TIMERS_AMOUNT, 0x000006            # Amount of timers


.section .data
str:
        .asciz "Timer "                 # "Timer x: MM:SS\n"


.section .text
.global main
main:
        la s0, kstack                   
        li s1, TIMERS_AMOUNT            
        li s2, 60                       # One minite (60 seconds)
        li s3, 10                       # Decimal base AKA 10
        li a0, 0                        # init value
        li t6, 0                        # Timer number [0, ..., 5]
LOOP_PUTS:
        beq t6, s1, DONE_PUTS
        la t0, str                      # Message addr to output
loop_str:   lb t1, 0(t0)
        beqz t1, done_str
1:      jal ra, PUT_CHAR
        addi t0, t0, 1                  # Traverse addresses for each char in message
        j loop_str
done_str:
        addi t1, t6, 0x30               # Encode timer number with ascii
        jal ra, PUT_CHAR
        li t1, ':'
        jal ra, PUT_CHAR
        li t1, 0x20                     # To show sperate space
        jal ra, PUT_CHAR
2:      div a1, a0, s2                  # Calculate timer count into minutes and seconds
        rem a2, a0, s2
        div a3, a1, s3                  # Calculate minutes
        rem a4, a1, s3
        div a5, a2, s3                  # Calculate seconds
        rem a6, a2, s3
        addi t1, a3, 0x30
        jal ra, PUT_CHAR
        addi t1, a4, 0x30
        jal ra, PUT_CHAR
        li t1, ':'
        jal ra, PUT_CHAR
        addi t1, a5, 0x30
        jal ra, PUT_CHAR
        addi t1, a6, 0x30
        jal ra, PUT_CHAR
        li t1, '\n'
        jal ra, PUT_CHAR
3:      addi t6, t6, 0                  # Process next timer
		j LOOP_PUTS
DONE_PUTS:
        jr ra, 0
      
; Display a char
; The char registered in t1      
PUT_CHAR:
        addi s0, s0, -16                # Allocate memory in stack to push register
1:      sw t1, 0(s0)
        sw t2, 4(s0)
        sw t3, 8(s0)
        ; sw t4, 12(s0)
poll:   lw t2, REG_DISP_CTRL            
        beqz t2, poll                   # Check ready status of displayer
        li t3, REG_DISP_DATA            
        sw t1, 0(t3)                    # Write a char into mm of displayer
2:      ; lw t4, 12(s0)
        lw t3, 8(s0)
        lw t2, 4(s0)
        lw t1, 0(s0)
        addi s0, s0, 16                 # Free memory in stack
3:      ret        