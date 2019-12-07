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

def check_for_double_not_matching(_in):
    group = {}
    double_not_matching = False
    counter = 0
    actual_char = ''
    for i in range(len(_in)-1):
        char = _in[i]
        if char == _in[i+1]: 
            if char not in group:
                group[char] = 0
            group[char] += 1
        counter = 0
    for key, val in group.items():
        if val == 1:
            double_not_matching = True
    return double_not_matching 

testarr = ["111111", "223450", "123789", "122345", "111123", "137677","112233","123444","111122"]
assert [False, True, False, True, False, True, True, False, True] == [check_for_double_not_matching(_in) for _in in testarr]

erg = [check_for_double(_in) and check_for_increase(_in) and check_for_double_not_matching(_in) for _in in all_possible_numbers]
passwords = []
count = 0
for i, e in enumerate(erg):
    if e:
        count += 1
        passwords.append(all_possible_numbers[i])
        
print(passwords)
print(f"Part2: {count}")
