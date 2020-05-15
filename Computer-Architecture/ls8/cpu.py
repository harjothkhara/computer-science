"""CPU functionality."""

import sys

# parse the command line
# print(sys.argv)

HLT = 1
LDI = 130  # SAVE
PRN = 71  # PRINT
MUL = 162  # MULTIPLY
PUSH = 69  # 0b01000101
POP = 70  # 0b01000110
CALL = 80
ADD = 160
RET = 17
SUB = 161
DIV = 163

SP = 7  # R7 is reserved as the stack pointer (SP) Fixed


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # like variables R0-R7, 8 bit register, 8 registers, index 0-7
        self.reg = [0] * 8
        # LS8 has only 8 registers, each 1 byte (base 2) 256 buckets, index 0-255,
        self.ram = [0] * 256
        self.pc = 0  # program counter
        # the SP points at the value at the top of the stack (most recently pushed), or at address F4 if the stack is empty. initialized 1 spot above the beginning of stack when empty. address of SP register to start. this is what SP is pointing to
        self.reg[SP] = 0xF4

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
                # adding program(binary) instructions to RAM
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

        if op == ADD:
            # adding reg_a and reb_b together and storing result in reg_a
            self.reg[reg_a] += self.reg[reg_b]
        elif op == SUB:
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == MUL:
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == DIV:
            self.reg[reg_a] /= self.reg[reg_b]
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
            # get our instructions from where PC is currently pointing
            IR = self.ram_read(self.pc)

            # getting the number of operands (AA) from the program instructions (opcode)
            operand_count = IR >> 6  # bitshift to get number of operands for this instruction
            # Grab C of the program instruction for if the instruction sets PC counter
            sets_pc = IR >> 4 & 0b0001

            # if instruction is LDI
            if IR == LDI:  # opcode for save (130)
                register = self.ram_read(self.pc + 1)  # operand 1
                value = self.ram_read(self.pc + 2)   # operand 2
                # store the data in a register
                self.reg[register] = value  # reg 0 = 8
                # go to the next instruction in our RAM

            # if instrcution is PRN
            elif IR == PRN:  # opcode for print
                # grab our only operand (register number)
                operand = self.ram_read(self.pc + 1)  # 0
                # using our operand we print the register value where we originally saved
                print(self.reg[operand])  # 8

            # if instruction is MUL or ADD
            elif IR == MUL or IR == ADD:
                reg_a = self.ram_read(self.pc + 1)
                reg_b = self.ram_read(self.pc + 2)
                self.alu(IR, reg_a, reg_b)

            elif IR == PUSH:
                # which register do you want to push to the stack?
                register = self.ram_read(self.pc + 1)
                # get the value at that register
                value = self.reg[register]
                # decrement the stack pointer (SP)
                self.reg[SP] -= 1
                # copy the value from the given register to RAM at the SP index
                self.ram_write(self.reg[SP], value)

            elif IR == POP:
                # grab the address of where to store the value in our CPU register
                register = self.ram_read(self.pc + 1)
                # get the last value in the stack
                last_value = self.ram_read(self.reg[SP])
                # assign that value in the register at the provided address
                self.reg[register] = last_value
                # increment the SP
                self.reg[SP] += 1

            # sets of a subroutine
            elif IR == CALL:  # instruction sets the PC
                self.reg[SP] -= 1
                # return address is pushed to stack (PC for next instruction)
                self.ram_write(self.reg[SP], self.pc + 2)
                # get register location for subroutine
                reg = self.ram_read(self.pc+1)
                # set the pc to the value in the given register (where the function is)
                self.pc = self.reg[reg]

            # return back from the subroutine
            elif IR == RET:
                # return address gets popped off the stack and stored in PC
                self.pc = self.ram_read(self.reg[SP])
                self.reg[SP] += 1
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
            if sets_pc == 0:
                self.pc += operand_count + 1
            # The number of operands AA is useful to know because the total number of bytes in any instruction is the number of operands + 1 (for the opcode).


# The SP points at the value at the top of the stack (most recently pushed), or at address F4 if the stack is empty.

#   PUSH the value in the given register on the stack.
# 1. Decrement the SP.
# 2. Copy the value in the given register to the address pointed to by SP.

# POP the value at the top of the stack into the given register.
# 1. Copy the value from the address pointed to by SP to the given register.
# 2. Increment SP.


# Quick Code Walk Through for mult.ls8 program: http://pythontutor.com/visualize.html#code=%22%22%22CPU%20functionality.%22%22%22%0A%0Aimport%20sys%0A%0AHLT%20%3D%201%0ALDI%20%3D%20130%20%20%23%20SAVE%0APRN%20%3D%2071%20%20%23%20PRINT%0AMUL%20%3D%20162%20%0A%0Aclass%20CPU%3A%0A%20%20%20%20%22%22%22Main%20CPU%20class.%22%22%22%0A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Construct%20a%20new%20CPU.%22%22%22%0A%20%20%20%20%20%20%20%20%23%20like%20variables%20R0-R7,%208%20bit%20register,%208%20registers,%20index%200-7%0A%20%20%20%20%20%20%20%20self.reg%20%3D%20%5B0%5D%20*%208%0A%20%20%20%20%20%20%20%20%23%20LS8%20has%20only%208%20registers,%20each%201%20byte%20%28base%202%29%20256%20buckets,%20index%200-255,%0A%20%20%20%20%20%20%20%20self.ram%20%3D%20%5B0%5D%20*%20256%0A%20%20%20%20%20%20%20%20self.pc%20%3D%200%20%20%23%20program%20counter%0A%0A%20%20%20%20def%20load%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Load%20a%20program%20into%20memory.%22%22%22%0A%0A%20%20%20%20%20%20%20%20address%20%3D%200%20%20%23%20indexes%20the%20long%20array%20%28256%20slots%29%20of%20memory%20%28RAM%29%0A%0A%20%20%20%20%20%20%20%20%23%20For%20now,%20we've%20just%20hardcoded%20a%20program%3A%0A%0A%20%20%20%20%20%20%20%20program%20%3D%20%5B%20%20%23%20list%20of%20opcodes%20%28program%20instructions%29%0A%20%20%20%20%20%20%20%20%20%20%20%200b10000010,%20%23%20LDI%20R0,8%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00001000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b10000010,%20%23%20LDI%20R1,9%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00001001,%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%200b10100010,%20%23%20MUL%20R0,R1%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%20%23%20HLT%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%20%20%23%20adding%20program%20instructions%20to%20RAM%0A%20%20%20%20%20%20%20%20for%20instruction%20in%20program%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20inserting%20instruction%20into%20memory%20slot%20%28self.ram%5B0%5D%20%3D%20130%29%0A%20%20%20%20%20%20%20%20%20%20%20%20self.ram%5Baddress%5D%20%3D%20instruction%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20print%28instruction%29%0A%20%20%20%20%20%20%20%20%20%20%20%20address%20%2B%3D%201%0A%0A%20%20%20%20def%20ram_read%28self,%20MAR%29%3A%0A%20%20%20%20%20%20%20%20return%20self.ram%5BMAR%5D%0A%0A%20%20%20%20def%20ram_write%28self,%20MAR,%20MDR%29%3A%0A%20%20%20%20%20%20%20%20%23%20MAR%20%3D%20Memory%20Address%20Register,%20contains%20the%20address%20that%20is%20being%20read%20or%20written%20to%0A%20%20%20%20%20%20%20%20%23%20MDR%20%3D%20Memory%20Data%20Register,%20contains%20the%20data%20that%20was%20read%20or%20the%20data%20to%20write%0A%20%20%20%20%20%20%20%20self.ram%5BMAR%5D%20%3D%20MDR%0A%0A%20%20%20%20def%20alu%28self,%20op,%20reg_a,%20reg_b%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22ALU%20operations.%22%22%22%0A%0A%20%20%20%20%20%20%20%20if%20op%20%3D%3D%20%22ADD%22%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5Breg_a%5D%20%2B%3D%20self.reg%5Breg_b%5D%0A%20%20%20%20%20%20%20%20%23%20elif%20op%20%3D%3D%20%22SUB%22%3A%20etc%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20Exception%28%22Unsupported%20ALU%20operation%22%29%0A%0A%0A%20%20%20%20def%20run%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Run%20the%20CPU.%22%22%22%0A%20%20%20%20%20%20%20%20%23%20%23%20load%20the%20program%20into%20memory%20%28if%20not%20already%20loaded%29%0A%20%20%20%20%20%20%20%20%23%20self.load%28%29%0A%0A%20%20%20%20%20%20%20%20running%20%3D%20True%0A%0A%20%20%20%20%20%20%20%20while%20running%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20IR%20%3D%20%20read%20the%20memory%20address%20that's%20stored%20in%20register%20PC%20%28special%20purpose%20register%29,%20and%20store%20that%20result%20in%20IR.%20initially%20points%20to%20the%200th%20spot%20in%20our%20RAM%0A%20%20%20%20%20%20%20%20%20%20%20%20IR%20%3D%20self.ram%5Bself.pc%5D%20%20%23%20130,%2071,%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20print%28IR%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20getting%20the%20number%20of%20operands%20%28AA%29%20from%20the%20program%20instructions%28opcode%29%0A%20%20%20%20%20%20%20%20%20%20%20%20operand_count%20%3D%20IR%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20instruction%20is%20LDI%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20IR%20%3D%3D%20LDI%3A%20%20%23%20opcode%20for%20save%20%28130%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20address%20%3D%20self.ram%5Bself.pc%20%2B%201%5D%20%20%23%20operand%201%20-%200%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20value%20%3D%20self.ram%5Bself.pc%20%2B%202%5D%20%20%20%23%20operand%202%20-%208%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20store%20the%20data%20in%20a%20register%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5Baddress%5D%20%3D%20value%20%20%23%20reg%200%20%3D%208%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20go%20to%20the%20next%20instruction%20in%20our%20RAM%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.pc%20%2B%3D%203%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20instrcution%20is%20PRN%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20PRN%3A%20%20%23%20opcode%20for%20print%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20grab%20our%20only%20operand%20%28register%20number%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20operand%20%3D%20self.ram%5Bself.pc%20%2B%201%5D%20%20%23%200%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20using%20our%20operand%20we%20print%20the%20register%20value%20where%20we%20originally%20saved%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28self.reg%5Boperand%5D%29%20%20%23%208%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20go%20to%20the%20next%20instruction%20in%20our%20RAM%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.pc%20%2B%3D%202%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20MUL%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20reg_A%20%3D%20self.ram%5Bself.pc%20%2B%201%5D%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20reg_B%20%3D%20self.ram%5Bself.pc%20%2B%202%5D%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5Breg_A%5D%20*%3D%20self.reg%5Breg_B%5D%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.pc%20%2B%3D%203%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20insruction%20is%20HLT%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20HLT%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20sys.exit%280%29%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20instruction%20is%20non%20recognizable%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22I%20did%20not%20understand%20that%20command%3A%20%7BIR%7D%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20sys.exit%281%29%0A%0A%0Acpu%20%3D%20CPU%28%29%0A%0Acpu.load%28%29%0Acpu.run%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=py3anaconda&rawInputLstJSON=%5B%5D&textReferences=false

# python tutor for system stack - push/pop http://pythontutor.com/visualize.html#code=%22%22%22CPU%20functionality.%22%22%22%0A%0Aimport%20sys%0A%0AHLT%20%3D%201%0ALDI%20%3D%20130%20%20%23%20SAVE%0APRN%20%3D%2071%20%20%23%20PRINT%0AMUL%20%3D%20162%0APUSH%20%3D%2069%20%20%23%200b01000101%0APOP%20%3D%2070%20%20%23%200b01000110%0A%23%20CAL%20%3D%2080%0A%23%20RET%20%3D%2017%0A%0ASP%20%3D%207%20%20%20%20%23%20stack%20pointer%0A%0Aclass%20CPU%3A%0A%20%20%20%20%22%22%22Main%20CPU%20class.%22%22%22%0A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Construct%20a%20new%20CPU.%22%22%22%0A%20%20%20%20%20%20%20%20self.reg%20%3D%20%5B0%5D%20*%208%0A%20%20%20%20%20%20%20%20%23%20LS8%20has%20only%208%20registers,%20each%201%20byte%20%28base%202%29%20256%20buckets,%20index%200-255,%0A%20%20%20%20%20%20%20%20self.ram%20%3D%20%5B0%5D%20*%20256%0A%20%20%20%20%20%20%20%20self.pc%20%3D%200%20%20%23%20program%20counter%0A%20%20%20%20%20%20%20%20self.reg%5BSP%5D%20%3D%200xF4%0A%0A%20%20%20%20def%20load%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Load%20a%20program%20into%20memory.%22%22%22%0A%20%20%20%20%20%20%20%20address%20%3D%200%20%20%23%20indexes%20the%20long%20array%20%28256%20slots%29%20of%20memory%20%28RAM%29%0A%20%20%20%20%20%20%20%20%23%20For%20now,%20we've%20just%20hardcoded%20a%20program%3A%0A%20%20%20%20%20%20%20%20program%20%3D%20%5B%20%0A%20%20%20%20%20%20%20%20%20%20%20%200b10000010,%20%23%20LDI%20R0,1%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%0A%20%20%20%20%20%20%20%20%20%20%20%200b10000010,%20%23%20LDI%20R1,2%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000010,%0A%20%20%20%20%20%20%20%20%20%20%20%200b01000101,%20%23%20PUSH%20R0%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b01000101,%20%23%20PUSH%20R1%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%0A%20%20%20%20%20%20%20%20%20%20%20%200b01000110,%20%23%20POP%20R0%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001%20%23%20HLT%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%20%20%23%20adding%20program%20instructions%20to%20RAM%0A%20%20%20%20%20%20%20%20for%20instruction%20in%20program%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20inserting%20instruction%20into%20memory%20slot%20%28self.ram%5B0%5D%20%3D%20130%29%0A%20%20%20%20%20%20%20%20%20%20%20%20self.ram%5Baddress%5D%20%3D%20instruction%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20print%28instruction%29%0A%20%20%20%20%20%20%20%20%20%20%20%20address%20%2B%3D%201%0A%0A%20%20%20%20def%20ram_read%28self,%20MAR%29%3A%0A%20%20%20%20%20%20%20%20return%20self.ram%5BMAR%5D%0A%0A%20%20%20%20def%20ram_write%28self,%20MAR,%20MDR%29%3A%0A%20%20%20%20%20%20%20%20self.ram%5BMAR%5D%20%3D%20MDR%0A%0A%20%20%20%20def%20run%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Run%20the%20CPU.%22%22%22%0A%20%20%20%20%20%20%20%20running%20%3D%20True%0A%20%20%20%20%20%20%20%20while%20running%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20IR%20%3D%20self.ram%5Bself.pc%5D%20%20%23%20130,%2071,%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20getting%20the%20number%20of%20operands%20%28AA%29%20from%20the%20program%20instructions%28opcode%29%0A%20%20%20%20%20%20%20%20%20%20%20%20operand_count%20%3D%20IR%20%3E%3E%206%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20instruction%20is%20LDI%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20IR%20%3D%3D%20LDI%3A%20%20%23%20opcode%20for%20save%20%28130%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20address%20%3D%20self.ram%5Bself.pc%20%2B%201%5D%20%20%23%20operand%201%20-%200%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20value%20%3D%20self.ram%5Bself.pc%20%2B%202%5D%20%20%20%23%20operand%202%20-%208%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20store%20the%20data%20in%20a%20register%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5Baddress%5D%20%3D%20value%20%20%23%20reg%200%20%3D%208%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20instrcution%20is%20PRN%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20PRN%3A%20%20%23%20opcode%20for%20print%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20grab%20our%20only%20operand%20%28register%20number%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20operand%20%3D%20self.ram%5Bself.pc%20%2B%201%5D%20%20%23%200%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20using%20our%20operand%20we%20print%20the%20register%20value%20where%20we%20originally%20saved%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28self.reg%5Boperand%5D%29%20%20%23%208%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20MUL%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20reg_A%20%3D%20self.ram%5Bself.pc%20%2B%201%5D%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20reg_B%20%3D%20self.ram%5Bself.pc%20%2B%202%5D%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5Breg_A%5D%20*%3D%20self.reg%5Breg_B%5D%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20PUSH%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20grab%20the%20register%20operand%20%28which%20register%3F%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20register%20%3D%20self.ram_read%28self.pc%20%2B%201%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20get%20the%20value%20in%20register%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20value%20%3D%20self.reg%5Bregister%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20decrement%20the%20stack%20pointer%20%28SP%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5BSP%5D%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20copy%20the%20value%20from%20the%20given%20register%20to%20RAM%20at%20the%20SP%20index%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.ram_write%28self.reg%5BSP%5D,%20value%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20POP%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20grab%20the%20address%20of%20where%20to%20store%20the%20value%20in%20register%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20reg%20%3D%20self.ram_read%28self.pc%20%2B%201%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20get%20the%20last%20value%20in%20the%20stack%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20last_value%20%3D%20self.ram_read%28self.reg%5BSP%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20assign%20that%20value%20in%20the%20register%20at%20the%20provided%20address%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5Breg%5D%20%3D%20last_value%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20increment%20the%20SP%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5BSP%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20CALL%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5BSP%5D%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.ram_write%28self.reg%5BSP%5D,%20self.pc%20%2B%202%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20reg%20%3D%20self.ram_read%28self.pc%2B1%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.pc%20%3D%20self.reg%5Breg%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20RET%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.pc%20%3D%20self.ram_read%28self.reg%5BSP%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5BSP%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20insruction%20is%20HLT%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20HLT%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20sys.exit%280%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20instruction%20is%20non%20recognizable%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22I%20did%20not%20understand%20that%20command%3A%20%7BIR%7D%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20sys.exit%281%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20increment%20PC%20to%20next%20instruction%0A%20%20%20%20%20%20%20%20%20%20%20%20self.pc%20%2B%3D%20operand_count%20%2B%201%0A%0A%0Acpu%20%3D%20CPU%28%29%0Acpu.load%28%29%0Acpu.run%28%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=py3anaconda&rawInputLstJSON=%5B%5D&textReferences=false

# python tutor - subroutine calls http://pythontutor.com/visualize.html#code=import%20sys%0A%0AHLT%20%3D%201%0ALDI%20%3D%20130%0APRN%20%3D%2071%20%20%0APUSH%20%3D%2069%0APOP%20%3D%2070%20%20%0ACALL%20%3D%2080%0AADD%20%3D%20160%0ARET%20%3D%2017%0A%0ASP%20%3D%207%20%20%20%20%0A%0Aclass%20CPU%3A%0A%20%20%20%20%22%22%22Main%20CPU%20class.%22%22%22%0A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Construct%20a%20new%20CPU.%22%22%22%0A%20%20%20%20%20%20%20%20self.reg%20%3D%20%5B0%5D%20*%208%0A%20%20%20%20%20%20%20%20self.ram%20%3D%20%5B0%5D%20*%20256%0A%20%20%20%20%20%20%20%20self.pc%20%3D%200%20%20%0A%20%20%20%20%20%20%20%20self.reg%5BSP%5D%20%3D%200xF4%0A%0A%20%20%20%20def%20load%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Load%20a%20program%20into%20memory.%22%22%22%0A%20%20%20%20%20%20%20%20address%20%3D%200%20%20%0A%20%20%20%20%20%20%20%20program%20%3D%20%5B%20%0A%20%20%20%20%20%20%20%20%20%20%20%200b10000010,%20%23%20LDI%20R1,MULT2PRINT%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00011000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b10000010,%20%23%20LDI%20R0,10%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00001010,%0A%20%20%20%20%20%20%20%20%20%20%20%200b01010000,%20%23%20CALL%20R1%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%0A%20%20%20%20%20%20%20%20%20%20%20%200b10000010,%20%23%20LDI%20R0,15%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00001111,%0A%20%20%20%20%20%20%20%20%20%20%20%200b01010000,%20%23%20CALL%20R1%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%0A%20%20%20%20%20%20%20%20%20%20%20%200b10000010,%20%23%20LDI%20R0,18%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00010010,%0A%20%20%20%20%20%20%20%20%20%20%20%200b01010000,%20%23%20CALL%20R1%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%0A%20%20%20%20%20%20%20%20%20%20%20%200b10000010,%20%23%20LDI%20R0,30%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00011110,%0A%20%20%20%20%20%20%20%20%20%20%20%200b01010000,%20%23%20CALL%20R1%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000001,%20%23%20HLT%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20MULT2PRI,NT%20%28address%2024%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%200b10100000,%20%23%20ADD%20R0,R0%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b01000111,%20%23%20PRN%20R0%0A%20%20%20%20%20%20%20%20%20%20%20%200b00000000,%0A%20%20%20%20%20%20%20%20%20%20%20%200b00010001,%20%23%20RET%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%20%20for%20instruction%20in%20program%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.ram%5Baddress%5D%20%3D%20instruction%0A%20%20%20%20%20%20%20%20%20%20%20%20address%20%2B%3D%201%0A%0A%20%20%20%20def%20ram_read%28self,%20MAR%29%3A%0A%20%20%20%20%20%20%20%20return%20self.ram%5BMAR%5D%0A%0A%20%20%20%20def%20ram_write%28self,%20MAR,%20MDR%29%3A%0A%20%20%20%20%20%20%20%20self.ram%5BMAR%5D%20%3D%20MDR%0A%0A%20%20%20%20def%20run%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Run%20the%20CPU.%22%22%22%0A%20%20%20%20%20%20%20%20running%20%3D%20True%0A%20%20%20%20%20%20%20%20while%20running%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20IR%20%3D%20self.ram%5Bself.pc%5D%20%20%23%20130,%2071,%201%0A%20%20%20%20%20%20%20%20%20%20%20%20operand_count%20%3D%20IR%20%3E%3E%206%0A%20%20%20%20%20%20%20%20%20%20%20%20sets_pc%20%3D%20IR%20%3E%3E%204%20%26%200b0001%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20IR%20%3D%3D%20LDI%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20address%20%3D%20self.ram%5Bself.pc%20%2B%201%5D%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20value%20%3D%20self.ram%5Bself.pc%20%2B%202%5D%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5Baddress%5D%20%3D%20value%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20PRN%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20operand%20%3D%20self.ram%5Bself.pc%20%2B%201%5D%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28self.reg%5Boperand%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20ADD%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20reg_a%20%3D%20self.ram_read%28self.pc%20%2B%201%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20reg_b%20%3D%20self.ram_read%28self.pc%20%2B%202%29%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5Breg_a%5D%20%2B%3D%20self.reg%5Breg_b%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20PUSH%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20register%20%3D%20self.ram_read%28self.pc%20%2B%201%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20value%20%3D%20self.reg%5Bregister%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5BSP%5D%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.ram_write%28self.reg%5BSP%5D,%20value%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20POP%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20reg%20%3D%20self.ram_read%28self.pc%20%2B%201%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20last_value%20%3D%20self.ram_read%28self.reg%5BSP%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5Breg%5D%20%3D%20last_value%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5BSP%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20CALL%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5BSP%5D%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.ram_write%28self.reg%5BSP%5D,%20self.pc%20%2B%202%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20reg%20%3D%20self.ram_read%28self.pc%2B1%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.pc%20%3D%20self.reg%5Breg%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20RET%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.pc%20%3D%20self.ram_read%28self.reg%5BSP%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.reg%5BSP%5D%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20IR%20%3D%3D%20HLT%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20sys.exit%280%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28f%22I%20did%20not%20understand%20that%20command%3A%20%7BIR%7D%22%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20sys.exit%281%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20sets_pc%20%3D%3D%200%3A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.pc%20%2B%3D%20operand_count%20%2B%201%0A%0A%0Acpu%20%3D%20CPU%28%29%0Acpu.load%28%29%0Acpu.run%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=py3anaconda&rawInputLstJSON=%5B%5D&textReferences=false
