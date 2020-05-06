#########
base 2: binary
#########
- 0b is prefix for binary

2 ** 0 = 1
2 ** 1 = 2
2 ** 2 = 4
2 ** 3 = 8
2 ** 4 = 16
2 ** 5 = 32
2 ** 6 = 64
2 ** 7 = 128
2 ** 8 = 256
2 ** 9 = 512
2 ** 10 = 1024

binary
0b 10100110

look at binary index and match with base 2 row

0 - 0
1 - 2
2 - 4
3 - 0
4 - 0
5 - 32
6 - 0
7 - 128

add them up
2 + 4 + 32 + 128 = 166

###########
base 10 number: decimal (humans use, we have 10 fingers, makes sense to us)
############

123

10 ** 0 = 1
10 ** 1 = 10
10 ** 2 = 100

how many 1's? 3 how many 10's? 20 how many 100's? 1

3 - 3
2 - 20
1 - 100
add up: 3 + 20 + 100 = 123

#################
Binary (base 2) -> Decimal (base 10)
#################

what is this binary number (base2) in base 10 (decimal?
0b 1010

0 - 0
1 - 2
2 - 0
3 - 8

2 + 8 = 10


what is this binary number (base2) in base 10 (decimal?
0b 1100

0 - 0
1 - 0
2 - 4
3 - 8

4 + 8 = 12

what is this binary number (base2) in base 10 (decimal?
0b 00110101

0 - 1
1 - 0
2 - 4
3 - 0
4 - 16
5 - 32
6 - 0
7 - 0

1 + 4 + 16 + 32 = 53

###################
Hexadecimal (base 16)
#####################
- 16 digits
- 0 - 9 then A - F
- 1 Byte = 8 bits
- 0x is prefix for hexadecimal

0b   0011       0101  = 1 Byte
      |          |
     4 bit     4 bit (nybble)

0b 1111

   1 + 2 + 4 + 8 = 15

we can represent 16 different values with 4 bits
here are 16 total values that we can represent in hexadecimal

16 hexadecimal digits:
0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

e.g
0b 0011 0101 = 53
    |     |
    3     5

the binary number above can be represented as:

0x 35

e.g
binary to hexadecimal to decimal
0b 1111 1111 = 0xFF = 255
    |    |
    15   15


in regular decimal we have 8 bits here so the max number we represent in 8 bits is 2 ** 8 = 256 - 1 or 255

e.g binary(base2) -> hex(base16) -> decimal(base10)
0b 1100 1011 = 0xCB = 203
    |     |
   12     11
16 hexadecimal digits:
0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
                      | |
                     11 12

base 2 eval l->r (binary -> dec)
11 + 64 + 128 = 203

can also use base 16 to evaluate: B has 11 1's
1 - 11 * 1
16 - 12 * 16

12 * 16 + 11 * 1 = 203
