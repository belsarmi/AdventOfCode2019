directions = []
lineA = []
lineB = []

with open("../Day3Input.txt") as f:
    for zeile in f:
        directions.append(zeile.strip())
print(directions)
lineA = directions[0].split(',')
lineB = directions[1].split(',')

print(lineA)
print("=================================")
print(lineB)

mydir, steps = (lineA[0][0], int(lineA[0][1:]))

print(mydir, steps)
results = {}
#found = False
#numberLoops = 0
#while not found:
#    numberLoops += 1
#    print(f"Loop #:{numberLoops}")
#    for zahl in directions:
#        result += zahl
#        if result in results:
#            print(f"Frequncy: {result}")
#            found = True
#            break
#        else:
#            results[result] = False
#print(f"Sum of the input: {sum(directions)}")
#print(results)
## number of loops 144
##frequency: 71961
