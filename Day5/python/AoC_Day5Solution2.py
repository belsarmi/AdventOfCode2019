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
    if op == 1 or op == 2 or op== 5 or op == 6 or op == 7 or op == 8:
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
#        print(f"pos: {pos}; op_input: {op_input}; op: {op}, a: {a}, b: {b}, c: {c}, op1: {op1}, op2: {op2}, op3: {op3}")
#        print(f"op_intput: {op_input}")
        print(f"Output: {instr[op1]}")
#        print(f"Output: {op1}")
        newpos = pos + 2
    if op == 5: 
        if op1 != 0:
            newpos = op2
        else: 
            newpos = pos + 3
    if op == 6: 
        if op1 == 0:
            newpos = op2
        else: 
            newpos = pos + 3
    if op == 7: 
        if op1 < op2:
            instr[op3] = 1
        else: instr[op3] = 0
        newpos = pos + 4
    if op == 8:
        if op1 == op2:
            instr[op3] = 1
        else: instr[op3] = 0
        newpos = pos + 4
#    print(f"pos: {pos}; op_input: {op_input}; op: {op}, a: {a}, b: {b}, c: {c}, op1: {op1}, op2: {op2}, op3: {op3}")
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

#test input:
#instr = [ 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
#1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
#999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

_instr = make_calculation(instr, pos, 5)

#instr = [1101,100,-1,4,0]
#instr = [1002,  4, 3, 4,33]
#assert [1101, 100, -1, 4, 99] == make_calculation([1101,100,-1, 4, 0],0)
#assert [1002,   4,  3, 4, 99] == make_calculation([1002,  4, 3, 4,33],0) 

