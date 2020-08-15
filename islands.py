T = int(input())


def manhattan(x,y, a, b):
    manhattan_distance = abs(x-a) + abs(y-b)
    return manhattan_distance


def distance_warship(island, a, b):
    x1 = island["x1"]
    y1 = island["y1"]
    x2 = island["x2"]
    y2 = island["y2"]
    x3,y3 = (x1+x2+y2-y1)/2,(y1+y2+x1-x2)/2
    x4,y4 = (x1+x2+y1-y2)/2,(y1+y2+x2-x1)/2
    distance =min(manhattan(x1,y1,a,b),manhattan(x2,y2,a,b),manhattan(x3,y3,a,b),manhattan(x4,y4,a,b))
    return (distance,island["index"])


islands = []
for index in range(T):
    x1, y1, x2, y2 = list(map(int, input().split(" ")))

    curr_island = {
        "x1": x1,
        "y1": y1,
        "x2": x2,
        "y2": y2,
        "index": index+1
    }
    islands.append(curr_island)
a, b = list(map(int, input().split(" ")))

islands.sort(key=lambda x: distance_warship(x, a, b))

for island in islands:
    print(island["index"], end=' ')
