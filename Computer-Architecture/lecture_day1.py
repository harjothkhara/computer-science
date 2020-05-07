# write a program in python that runs programs

# op codes, this is what you would give a programmer as "documentation"
PRINT_BEEJ = 1  # for LS8 look up what this is in spec
HALT = 2  # for LS8 look up what this is in spec
SAVE_REG = 3  # Store a value in a register (in the LS8 called LDI)
PRINT_REG = 4  # corresponds to PRN instruction in the LS8

memory = [  # instructions (scroll)
    PRINT_BEEJ,  # instruction is 1 byte long

    # SAVE R0, 37    store 37 in R0      the opcode (if pc is here) instruction is 3 bytes long
    SAVE_REG,
    0,  # R0 (register slot 0) operand ("argument") (pc + 1)
    37,  # 37 (value we want to store) operand (pc + 2)

    PRINT_BEEJ,

    PRINT_REG,  # PRINT_REG R0 (instruction is 2 bytes long)
    0,  # R0

    HALT
]

# ALL THE CODE BELOW IS THE "COMPUTER"

register = [0] * 8  # like variables R0-R7

# Program Counter, the address (which slot in memory, which index in memory it is) of the current instruction. Wherever the pc is the instruction that's currently running right now
pc = 0
running = True

while running:  # piano
    inst = memory[pc]  # lets receive some instructions, and execute them

    if inst == PRINT_BEEJ:
        print("Beej")
        pc += 1  # moving to the next instruction

    elif inst == SAVE_REG:
        reg_num = memory[pc+1]  # R0=0
        value = memory[pc+2]  # 37
        register[reg_num] = value  # register[0] = 37
        pc += 3

    elif inst == PRINT_REG:
        reg_num = memory[pc+1]
        value = register[reg_num]
        print(value)
        pc += 2

    elif inst == HALT:
        running = False

    else:
        print("Unknown instruction")
        running = False
