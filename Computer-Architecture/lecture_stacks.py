FF: 00
FE: 00
FD: 00
FC: 00
FB: 00
FA: 00
F9: 00
F8: 00
F7: 00
F6: 00
F5: 00
F4: 00 < -- SP  # stack pointer # SP started here (top of stack)
F3: 12   # just stays here until it we push something and it gets overwritten
F2: 12   # just stays here until it we push something and it gets overwritten
F1: 00
F0: 00
EF: 00
.
.
.
05: 00
04: 00
03: XX  # instruction - not empty
02: XX  # instruction - not empty
01: XX  # instruction - not empty
00: XX < -- PC  # program counter


# REGISTERS
R0: 00
R1: 23
R2: 12

R7: F4  # this is the SP

# lets run these instructions
PUSH R0 ✅
PUSH R1 ✅
POP R2  ✅
POP R1  ✅
POP R1 < --  # Pop on an empty stack??

# stack pointer (always points to the most recently pushed item)
# per spec:

# The SP points at the value at the top of the stack (most recently pushed), or at address F4 if the stack is empty.

#   PUSH the value in the given register on the stack.
# 1. Decrement the SP. - F4->F3->F2
# 2. Copy the value in the given register to the address pointed to by SP. - F3:12, F2: 32

# POP the value at the top of the stack into the given register.
# 1. Copy the value from the address pointed to by SP to the given register. - R2: 32, R1: 12
# 2. Increment SP. - R7: F3, R7: F4


# what happens if you cause an overflow (too many pushes past 0) or an underflow (too many pops past FF-255)? if you roll off the top of memory the stackpointer actually rolls around to the bottom or top. if you pop of the top of memory or push from the bottom of memory it'll wrap around to the other side because there's not a wire to hold that extra bit. too many pushes past 0 is stack overflow and too many pops past FF is stack underflow.
0xff 0b11111111

11111111  # 8 bit machine
+      1  # add extra bit
________
00000000

# to emulate using python code which has no memory restrictions like C, use this code:
(r1 + r2) & 0xff

    100000000    # 9 bits
  & 011111111  # 0xff (bit masking)
    ____________
    000000000

# why does the stack start at the top and grow downward?
# stack pointer and PC overlap, stack has impacted the program we have stack overflow
# starting the stack at the top gives us the most space before we hit the program at the bottom
