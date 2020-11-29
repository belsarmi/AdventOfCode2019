from typing import NamedTuple, Set, Dict

class XY(NamedTuple):
    x: int
    y: int


def locations(path: str) -> Dict[XY, int]:
    #R8,U5,L5,D3
   x = y = num_steps = 0
    
   visited = {}

   for line in path.split(","):
       direction = line[0]
       distance = int(line[1:])

       for _ in range(distance):
           num_steps += 1
           if direction == "U":
               y += 1
           elif direction == "D":
               y -= 1
           elif direction == "R":
               x += 1
           elif direction == "L":
               x -= 1
           else:
               raise RuntimeError(f"bad direction: {direction}")

           loc = XY(x,y)
           if loc not in visited:
               visited[loc] = num_steps

   return visited

def closest_intersection (path1: str, path2: str) -> int:
    dist1 = locations(path1)
    dist2 = locations(path2)
    intersections = set(dist1).intersection(set(dist2))


    return min(dist1[loc] + dist2[loc] for loc in intersections)

assert closest_intersection("R75,D30,R83,U83,L12,D49,R71,U7,L72",
                            "U62,R66,U55,R34,D71,R55,D58,R83") == 610
assert closest_intersection("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 410

directions =[]
with open("../Day3Input.txt") as f:
    for zeile in f:
        directions.append(zeile.strip())
my_result = closest_intersection(directions[0], directions[1])
print(my_result)
