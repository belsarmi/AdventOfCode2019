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
    op_str = f"{op:05}"
    DE = int(op_str[-2:])
    C = int(op_str[2])
    B = int(op_str[1]) 
    A = int(op_str[0]) 

    return A, B, C, DE
assert (0, 1, 0, 2) == get_opcode_mode(1002)
assert (0, 1, 1, 1) == get_opcode_mode(1101)
assert (0, 0, 0, 3) == get_opcode_mode(3)

def operand_by_mode(pos, mod3rd_param, mod2nd_param, mod1st_param, op):
    
    op1 = op2 = op3 = None
    addr1 = instr[pos +1]
    addr2 = instr[pos +2]
    if op == 1 or op == 2:
        op1 = instr[addr1] if mod1st_param == 0 else instr[pos + 1]
        op2 = instr[addr2] if mod2nd_param == 0 else instr[pos + 2]
        op3 = instr[pos + 3]
    addr1 = addr2 = None
    if op == 3 or op == 4:
        op1 = instr[pos + 1]

    return op1, op2, op3

def operation(pos, op_input, input_value):
   
    newpos = None
    a, b, c, op = get_opcode_mode(op_input)
    op1, op2, op3 = operand_by_mode(pos, a,b,c, op)
    if op == 1: #addition
        instr[op3] = op1 + op2
        newpos = pos + 4
    if op == 2: #multiplication
        instr[op3] = op1 * op2
        newpos = pos + 4
    if op == 3: #input
        instr[op1] = input_value
        newpos = pos + 2
    if op == 4: #output
        print(f"Output: {instr[op1]}")
        newpos = pos + 2
    return newpos

def make_calculation (instr, pos, input_value):
    while instr[pos] != 99:
        pos = operation(pos, instr[pos], input_value)
    return instr
############################################################

instr = []
with open("../Day5Input.txt") as f:
    for zeile in f:
        instr = list(map(int, zeile.strip().split(",")))

pos = 0
_instr = make_calculation(instr, pos, 1)

#instr = [1101,100,-1,4,0]
#instr = [1002,  4, 3, 4,33]
#assert [1101, 100, -1, 4, 99] == make_calculation([1101,100,-1, 4, 0],0)
#assert [1002,   4,  3, 4, 99] == make_calculation([1002,  4, 3, 4,33],0) 

#Output to the console

#Output: 3
#Output: 0
#Output: 0
#Output: 0
#Output: 0
#Output: 0
#Output: 0
#Output: 0
#Output: 0
#Output: 9006673

