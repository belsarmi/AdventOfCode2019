def get_opcode_mode(op):
    """
ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
    """
    DE = op%10
    C = (op%1000)//100
    B = (op%10000)//1000
    A = op//10000

    return A, B, C, DE
assert (0, 1, 0, 2) == get_opcode_mode(1002)
assert (0, 1, 1, 1) == get_opcode_mode(1101)

def operand_by_mode(pos, mod3rd_param, mod2nd_param, mod1st_param):
    op1 = instr[instr[pos + 1]] if mod1st_param == 0 else instr[pos + 1]
    op2 = instr[instr[pos + 2]] if mod2nd_param == 0 else instr[pos + 2]
    op3 = instr[pos + 3]
    return op1, op2, op3

def operation(pos, op_input):
   
    a, b, c, op = get_opcode_mode(op_input)
    op1, op2, op3 = operand_by_mode(pos, a,b,c)
    if op == 1: #addition
        instr[op3] = op1 + op2
        newpos = pos + 4
    if op == 2: #mulitplication
        instr[op3] = op1 * op2
        newpos = pos + 4
    if op == 3: #input
        instr[op1] = input_to_save
        newpos = pos + 2
    if op == 4: #output
        output = instr[op1]
        newpos = pos + 2
    return newpos

def make_calculation (instr, pos):
    newpos = pos
    while instr[newpos] != 99:
        _, _, _, oper = get_opcode_mode(instr[newpos]) 
        newpos = operation(newpos, instr[newpos])
#        if oper == 1:
#            newpos = operation(newpos, 1)
#        elif oper == 2:
#            newpos = operation(newpos, 2)
    return instr
############################################################

instr = []
with open("../Day5Input.txt") as f:
    for zeile in f:
        instr = list(map(int, zeile.strip().split(",")))

#instr = [1101,100,-1,4,0]
instr = [1002,  4, 3, 4,33]
pos = 0

print(f"{instr}")
_instr = make_calculation(instr, pos)
#assert [1101, 100, -1, 4, 99] == make_calculation([1101,100,-1, 4, 0],0)
#assert [1002,   4,  3, 4, 99] == make_calculation([1002,  4, 3, 4,33],0) 
print(f"Result: {_instr}")
