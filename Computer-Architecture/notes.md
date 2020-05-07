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


BINARY (Base 2)
+--------128s place
|+-------64s place
||+------32s place
|||+-----16s place
||||+----8s place
|||||+----4s place
||||||+--2s place
|||||||+-1s place
||||||||
76543210

########
Bases
########

  0
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10

1234

one 1000
two 100
three 10
four 1

1 * 1000 + (10**3)
2 * 100 + (10**2)
3 * 10 + (10**1)
4 * 1 (10**0)

powers of 10

binary counting (same pattern but in a different base)
+----8s place (0b1000's place)
|+----4s place (0b100's place)
||+--2s place (0b10's place)
|||+-1s place (0b1's place)
||||
   0    # 0
   1    # 1
  10    # 2
  11    # 3
 100    # 4
 101    # 5
 110    # 6
 111    # 7
1000    # 8

1101 in decimal?

one in the 8's place +
1 * 8
one in the 4's place +
1 * 4
zero in the 2's place +
0 * 2
one in the 1's place +
1 * 1
________
13

to know the place values in your destination base and then add them up
base 10 numbers for the binary place values.

Binary to Hex

############
Binary to Hex
#############
0 - 9, a,b,c,d,e,f
4 binary digits == 1 hex digit
  ^^         ^
Byte is 8 bits

11010011 binary == d3 hexadecimal

1101 0011
 |     |
 13    3
  |
  d

0xff
  15    15 (last in prefix 0-9,a-f)
   |     |
   ^     ^
  1111  1111

one in the 8 bucket place +
1 * 8
one in the 4 bucket place +
1 * 4
once in 2 bucket place +
1 * 2
one in the 1 bucket place +
1 * 1
________
8 + 4 + 2 + 1 = 15 decimal
1111 binary

    f             f
   1111          1111

128+64+32+16 +  8+4+2+1 = 255

0xff == 0b11111111 == 255 (max amount we can store in 8 bits, or 1 byte)
