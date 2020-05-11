# true table code
for A in [False, True]:
    for B in [False, True]:
        print(f"{A} - {B} -- {(not A or not B)}")

# we can represent binary addition using logic
A and B
A    B   result
--------------
0    0     0
0    1     0
1    0     0
1    1     1

A or B
A    B   result
--------------
0    0     0
0    1     1
1    0     1
1    1     1


A + B    result
------------------
0    0     0  0
0    1     0  1
1    0     0  1
1    1     1  0  # -> converted to binary from 2


0 - False
1 - True

A and B
A    B   result
--------------
0    0     0
0    1     0
1    0     0
1    1     1

# bitwise operator
# and
4 & 3 = ? 0
# write out in binary
  0100  # 4
& 0011  # 3
  --------
  0000

A or B
A    B   result
--------------
0    0     0
0    1     1
1    0     1
1    1     1
# or
14 | 6 = ? 14

  1110  # 14
| 0110  # 6
  ________
  1110  # 14

# bitwise AND can be used for bitmasking and to see the value of that single bit
# works like a stencil put a '1' on whichever column your interested in and will tell you if you have visited that person or not (Brady game example).
# bitwise AND is also known as bitmask b/c just like that mask/stencil it will show only columns that are labeled with a 1
            ↓
       01011100  # visited our inn keeper
     & 00000100 # extracting the value 4 out of the single bit above
     ___________
       00000100  # we've extracted this bit out and tell us if we've visited that person or not
            ↑
# you store your values in bitwise operations
# you can use a bitwise OR to flip a single bit
             ↓
        01011000  # 88 - not visited our inn keeper, say we wanted to flip that to say we visited
      | 00000100  # we could do an bitwise OR on 88
        ________
        01011100  # now it is visited
             ↑

# XOR - exclusive OR, used to coerce
A XOR B
A    B   result
--------------
0    0     0 <- # not exclusive
0    1     1
1    0     1
1    1     0 <- # not exclusive

# useful for encryption
   0b10101010 <-- # want to encrypt - 170
 ^ 0b11110000 <-- # key - 240
   __________
   0b01011010 # 90 is our encrypted value, if we want to decrypt we XOR this with our key again
^  0b11110000 <-- # key - 240
   __________
     10101010 <-- # back to our original value

# bit shifting
01011000 >> 4 # 88 >> 4 = 5
00101100
00010110
00001011
00000101 # 5

01011000 << 2
10110000
01100000


# opcode instructions

01101001
^^
# tells use how many arguments(operands) this instructions has. this one has 1
# can use bit shifting to get opcode instructions
0b01101001 # opcode, need to bitshift by 6 to get number of operands
0b01101001 >> 6
0b00000001 # 1 - this opcode has one operand or argument

# how do we know how much to increment our pc - program counter. we can use bit shifting to accomplish this.

# what arithmetic operation is shifting to the left by one equal to? * 2
8 << 1
0b00001000 # 8
0b00010000 # 16
# what arithmetic operation is shifting to the right by one equal to? /2
  # if your ever want to do division really quick do bit shifting
8 >> 1
0b00001000 # 8
0b00000100 # 4
