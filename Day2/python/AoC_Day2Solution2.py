def operation(pos, op):
    op1 = instr[pos + 1]
    op2 = instr[pos + 2]
    save = instr[pos + 3]
#    print(f"save: {save}")
    if op == 1:
        instr[save] = instr[op1] + instr[op2]
#       print(f"instr[save]: {instr[save]}")
    if op == 2:
        instr[save] = instr[op1] * instr[op2]

def make_calculation (instr, pos):
    while instr[pos] != 99:
        if instr[pos] == 1:
#        print(f"before opearation add: {instr}")
            operation(pos, 1)
#        print(f"after opearation add: {instr}")
            pos += 4
        elif instr[pos] == 2:
#        print(f"before opearation mul: {instr}")
            operation(pos, 2)
#        print(f"after opearation mul: {instr}")
            pos += 4

############################################################

instr = []
with open("../Day2Input.txt") as f:
    for zeile in f:
        instr = list(map(int, zeile.strip().split(",")))

instr_temp = instr.copy()
pos = 0

for noun in range(40,50): # I have tried the first value manually
    if instr[0] == 19690720:
        noun -= 1
        break
    for verb in range(90):
        instr[1] = noun
        instr[2] = verb

        make_calculation(instr, pos)
#        print(f"Result: {instr[0]}, {noun}, {verb}")
        if instr[0] == 19690720:
            break
        instr = instr_temp.copy()
        pos = 0


print(f"Result: {instr[0]}, {noun}, {verb}")
