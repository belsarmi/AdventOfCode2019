#solution with help from: https://www.youtube.com/watch?v=PcgQirxsnR4
from typing import NamedTuple, Set

class XY(NamedTuple):
    x: int
    y: int


def locations(path: str) -> Set[XY]:
    #R8,U5,L5,D3
   x = y = 0
    
   visited = set()

   for line in path.split(","):
       direction = line[0]
       distance = int(line[1:])

       for _ in range(distance):
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

           visited.add(XY(x,y))

   return visited

def all_intersections(path1: str, path2: str) -> Set[XY]:
    locations1 = locations(path1)
    locations2 = locations(path2)
    return locations1.intersection(locations2)

def manhattan_distance(xy: XY) -> int:
    return abs(xy.x) + abs(xy.y)

def closest_intersection (path1: str, path2: str) -> int:
    ai = all_intersections(path1, path2)
    return min(manhattan_distance(i) for i in ai)

assert closest_intersection("R75,D30,R83,U83,L12,D49,R71,U7,L72",
                            "U62,R66,U55,R34,D71,R55,D58,R83") == 159
assert closest_intersection("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7") == 135

directions =[]
with open("../Day3Input.txt") as f:
    for zeile in f:
        directions.append(zeile.strip())
my_result = closest_intersection(directions[0], directions[1])
print(my_result)
