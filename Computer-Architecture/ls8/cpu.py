"""CPU functionality."""

import sys

# parse the command line
# print(sys.argv)

HLT = 1
LDI = 130  # SAVE
PRN = 71  # PRINT
MUL = 162  # MULTIPLY


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # like variables R0-R7, 8 bit register, 8 registers, index 0-7
        self.reg = [0] * 8
        # LS8 has only 8 registers, each 1 byte (base 2) 256 buckets, index 0-255,
        self.ram = [0] * 256
        self.pc = 0  # program counter

    def load(self):
        """Load a program into memory."""

        program_filename = sys.argv[1]
        address = 0  # indexes the long array (256 slots) of memory (RAM)

        # For now, we've just hardcoded a program:

        # program = [  # list of opcodes (program instructions)
        #     # From print8.ls8
        #     0b10000010,  # LDI R0,8 - decimal value: 130
        #     0b00000000,  # at reg[0] (operand 1)
        #     0b00001000,  # store the value 8 - (operand 2)
        #     0b01000111,  # PRN R0 -- decimal value is 71
        #     0b00000000,  # print reg[0] (operand 1)
        #     0b00000001,  # HLT - decimal value is 1
        # ]
        # # adding program instructions to RAM
        # for instruction in program:
        #     # inserting instruction into memory slot (self.ram[0] = 130)
        #     self.ram[address] = instruction
        #     # print(instruction)
        #     address += 1
        with open(program_filename) as f:
            # iterate through each line in the program
            for line in f:
                # remove any comments
                line = line.split("#")[0]
                # remove whitespace
                line = line.strip()
                # skip any empty lines
                if line == "":
                    continue  # skips rest of the code for current iteration only
                # change from str to int - since binary using base 2, otherwise default base 10
                value = int(line, 2)
                # adding program instructions to RAM
                self.ram[address] = value
                # print(value, type(value))
                # print(value)
                address += 1

        # print(self.ram)

    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MAR, MDR):
        # MAR = Memory Address Register, contains the address that is being read or written to
        # MDR = Memory Data Register, contains the data that was read or the data to write
        self.ram[MAR] = MDR

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # load the program into memory (if not already loaded)
        self.load()

        running = True

        while running:
            # Instruction Register, contains a copy of the currently executing instruction
            # lets receive some instructions from RAM, and execute them
            # IR =  read the memory address that's stored in register PC (special purpose register), and store that result in IR. initially points to the 0th spot in our RAM
            IR = self.ram[self.pc]  # 130, 71, 1

            # getting the number of operands (AA) from the program instructions (opcode)
            operand_count = IR >> 6  # bitshift to get number of operands for this opcode

            # if instruction is LDI
            if IR == LDI:  # opcode for save (130)
                address = self.ram[self.pc + 1]  # operand 1 - 0
                value = self.ram[self.pc + 2]   # operand 2 - 8
                # store the data in a register
                self.reg[address] = value  # reg 0 = 8
                # go to the next instruction in our RAM

            # if instrcution is PRN
            elif IR == PRN:  # opcode for print
                # grab our only operand (register number)
                operand = self.ram[self.pc + 1]  # 0
                # using our operand we print the register value where we originally saved
                print(self.reg[operand])  # 8

            # if instruction is MUL
            elif IR == MUL:  # opcode for multiply
                # print(f"mul_before:{self.reg}")
                # grab operand 1 for register A
                reg_A = self.ram[self.pc + 1]  # value in register A
                # grab operand 2 for register B
                reg_B = self.ram[self.pc + 2]  # value in register B

                # multiple the values in two registers together and store the result in register A. store in one of our registers
                self.reg[reg_A] *= self.reg[reg_B]
                # print(f"mul_after:{self.reg}")
            # if instruction is HLT - Halt the CPU (and exit the emulator)
            elif IR == HLT:  # opcode for HLT - Halts the program and exits
                # 0 - means a clean exit without any errors / problems
                sys.exit(0)

            # if instruction is non recognizable
            else:
                print(f"I did not understand that command: {IR}")
                # 1 - means there was some issue / error / problem and that is why the program is exiting.
                sys.exit(1)
            # go to the next instruction in our RAM
            self.pc += operand_count + 1
            # The number of operands AA is useful to know because the total number of bytes in any instruction is the number of operands + 1 (for the opcode).
