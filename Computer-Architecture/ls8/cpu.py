"""CPU functionality."""

import sys

# print(sys.argv)

HLT = 1
LDI = 130  # SAVE
PRN = 71  # PRINT


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8  # like variables R0-R7
        self.ram = [0] * 256
        self.pc = 0  # program counter

    def load(self):
        """Load a program into memory."""

        address = 0  # indexes the long array of memory (RAM)

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8 - decimal value: 130
            0b00000000,  # at reg[0] (operand 1)
            0b00001000,  # store the value 8 - (operand 2)
            0b01000111,  # PRN R0 -- decimal value is 71
            0b00000000,  # print reg[0] (operand 1)
            0b00000001,  # HLT - decimal value is 1
        ]
        # adding program instructions from CPU register to RAM
        for instruction in program:
            self.ram[address] = instruction
            address += 1

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
        # load the program into memory
        self.load()

        while True:
            # Instruction Register, contains a copy of the currently executing instruction
            # lets receive some instructions from RAM, and execute them
            # IR =  read the memory address that's stored in register PC (special purpose register), and store that result in IR. initially points to the 0th spot in our RAM
            IR = self.ram[self.pc]
            if IR == LDI:  # opcode for save
                address = self.ram[self.pc + 1]  # operand 1
                value = self.ram[self.pc + 2]   # operand 2
                # store the data
                self.LDI(address, value)
                # increment the PC by 3 to skips the operands and go to next instruction
                self.pc += 3
            elif IR == PRN:  # opcode for print
                data = self.ram[self.pc + 1]
                # print the data
                print(self.PRN(data))
                # increment the PC by 2 to skip the operand and go to next instruction
                self.pc += 2
            elif IR == HLT:  # opcode for HLT - Halts the program and exits
                # 0 - means a clean exit without any errors / problems
                sys.exit(0)
            else:
                print(f"I did not understand that command: {IR}")
                # 1 - means there was some issue / error / problem and that is why the program is exiting.
                sys.exit(1)
