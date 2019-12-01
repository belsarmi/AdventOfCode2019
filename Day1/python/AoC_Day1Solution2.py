modules = []
#testinput  = [100756]

def calc_result(module):
    return module // 3 - 2

def calculate (modules):
    mysum = 0
    i_res = False
    res2 = 0
    for module in modules:
        res = calc_result(module)
        mysum += res
        while not i_res:
            if calc_result(res) >= 0:
                res = calc_result(res)
                mysum += res
            else:
                i_res = True
        i_res = False
    return mysum


with open("../Day1Input.txt") as f:
    for zeile in f:
        modules.append(int(zeile.strip()))

print(calculate(modules))
