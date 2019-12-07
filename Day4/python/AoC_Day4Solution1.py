input = "134564-585159"
#generated a list with all possible numbers
all_possible_numbers = [x for x in range(int(input.split("-")[0]), int(input.split("-")[1]) + 1)]
all_possible_numbers = [str(x) for x in all_possible_numbers]

def check_for_double(_in):
    double = False
    for i in range(len(_in)-1):
        char = _in[i]
        if char == _in[i+1]: 
            double = True
    return double 

def check_for_increase(_in):
    increase = False
    for i in range(len(_in)-1):
        char = int(_in[i])
        if int(_in[i+1]) >= char:
            increase = True
        else: 
            return  False
    return increase

erg = [check_for_double(_in) and check_for_increase(_in) for _in in all_possible_numbers]
passwords = []
count = 0
for i, e in enumerate(erg):
    if e:
        count += 1
        passwords.append(all_possible_numbers[i])
        
print(passwords)
print(f"Part1: {count}")
