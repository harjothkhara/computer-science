# Code to extract the instruction length from the opcode on the LS8
inst_len = ((ir & 0b11000000) >> 6) + 1   # 3
pc += inst_len
