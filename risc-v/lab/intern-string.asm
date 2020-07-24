.data
.align 4
errEnvc: asciz "error: Environment call failed"
errDivz: asciz "error: Divided by zero failed"

asciiSpace: .byte '\t', '\n', '\v', '\f', '\r', ' '
asciiLineFeed: .byte 0x0a
asciiLineSpace: .byte 0x20
asciiEOT: .byte 4

arrIdentifiers: .space 512              # Hold identifiers, capacity=128
sizeIdentifiers: .4byte 0               # Size of identifiers
pHashTable: .space 128                  # Hold hash, capacity=32
sizeHashTable: .4byte 0                 # Size of hashtable

.text
internFileImpl:
        addi    s11, a0                 # save original buffer pointer
        addi    a7, a7, 0               # offset of first interned-string
        addi    a6, a6, 0               # index of interned-string
        addi    t0, t0, 0               # length of interned-string
loop_space_front:
        lb      t1, 0(a0) 
        li      t6, asciiEOT
        beq     t1, t6, done_space_front     
        li      t6, asciiLineFeed
        beq     t1, t6, pass_space_front
        li      t6, asciiLineSpace
        beq     t1, t6, pass_space_front
        lw      a7, a0
        j       done_space_front
pass_space_front:        
        addi    a0, a0, 1
        j       loop_space_front
done_space_front:
        addi    a0, a0, 1
        addi    t0, t0, 0
        
        
        jal     ra, 0
        
# Add hashtable
# 
# Param:
#   a7: string address        
#   a6: registerd hash, also is index of hashtable to add
# Return:
#   a5: 
add_hashtable:
        la      t0, arrIdentifiers
        mul     t6, a6, 4
        addi    t0, t0, t6
        lw      t1, 0(t0)
        bne     t1, add_bucket
        sw      a7, 0(t0)
        jal     add_identifiers
        ret
        

add_bucket:
        
        
        
        ret
        
# Add id into array

add_identifiers:

         
        
        
        
# Hash string
# Calculate hash with checksum 
# Param:
#   a7: registerd address of string (ended with '\0')
#   a6: registerd modulo
# Return:
#   a5: hash
calculate_string_hash:
        beqz    a6, failed             # divide by 0 err
        li      a5, 0
loop_string:
        lb      t0, 0(a7)
        beqz    t0, pass
        
        addi    t1, a5, t0
        ; div     t1, a6
        rem     a5, t1, a6
        
        addi    a7, a7, 1
        j       pass
failed:        
        la      a0, errDivz             # to stdErr
        li      a7, 4
        ecall
        li      a7, 10                  # terminate
        ecall        
pass:
        ret
        
# Allocate in heap to perform immutable copy
# The source are char buffer not include white space
# The destination are copy of source plus '\0'
# Param:
#   a7: registerd address of source
#   a6: source length
# Retrun:
#   a5: destination address
copy_string_buffer:
        lw      t0, a7                  # save source
        
        addi    a7, 9                   # using RARS to allocate heap
        addi    a0, a6, 1
        ecall
        li      t1, 0x80000000
        bge     a0, t1, failed          # not heap (kernel mem)    
        
        li      t6, 0                   # index of source
        li      a7, t0                  # restore source
        lw      a5, a0                  # save destination
loop_src:
        beq     t6, a6, done_loop
        lb      t0, 0(a7)
        sw      t0, 0(a0)
        addi    t6, t6, 1
        addi    a7, a7, 1
        addi    a0, a0, 1
        j       loop_src
done_loop:
        li      t0, 0
        sw      t0, 0(a0)
        j       pass
failed:
        la      a0, errEnvc             # to stdErr
        li      a7, 4
        ecall
        li      a7, 10                  # terminate
        ecall
pass:
        jalr    zero, 0(ra)     
