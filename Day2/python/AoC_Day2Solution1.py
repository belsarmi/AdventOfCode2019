instr = []

with open("../Day2Input.txt") as f:
    for zeile in f:
        instr = list(map(int, zeile.strip().split(",")))
pos = 0
instr[1] = 12
instr[2] = 2
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

print("halt")
print(f"Result: {instr[0]}")
