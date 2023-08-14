import numpy as np


def unit_vector(vector):
    if np.linalg.norm(vector) == 0:
        return np.array([0, 0])
    return vector / np.linalg.norm(vector)


def angle(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def in_hull(points, target):
    res = 0
    for i in range(len(points)):
        first = points[i]
        if i + 1 >= len(points):
            second = points[0]
        else:
            second = points[i + 1]
        v1 = np.array([first.x - target.x, first.y - target.y])
        v2 = np.array([second.x - target.x, second.y - target.y])
        res += angle(v1, v2)
    if round(res, 2) == 6.28:
        return True
    return False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def Left_index(points):
    res = 0
    for i in range(1, len(points)):
        if points[i].x < points[res].x:
            res = i
        elif points[i].x == points[res].x:
            if points[i].y > points[res].y:
                res = i
    return res


def convexHull(points, n):
    res = []
    l = Left_index(points)
    hull = []
    p = l
    while 1:
        hull.append(p)
        q = (p + 1) % n
        for i in range(n):
            if (points[i].y - points[p].y) * (points[q].x - points[i].x) - (points[i].x - points[p].x) * (
                    points[q].y - points[i].y) < 0:
                q = i
        p = q
        if p == l:
            break
    for each in hull:
        res.append(Point(points[each].x, points[each].y))
    return res


n = int(input())
points = [None, None, None, None]
points[0] = []
points[1] = []
points[2] = []
points[3] = []
users = [None, None, None, None]
users[0] = []
users[1] = []
users[2] = []
users[3] = []
u = [None, None, None, None]
u[0] = u[1] = u[2] = u[3] = 0
usersR2 = [None, None]
usersR2[0] = []
usersR2[1] = []
uR2 = [None, None]
uR2[0] = uR2[1] = 0
for j in range(4):
    for i in range(n):
        inputt = np.array(input().split()).astype(float)
        points[j].append(Point(inputt[0], inputt[1]))
    users[j] = convexHull(points[j], len(points[j]))
usersR2[0] = convexHull(points[0] + points[1], len(points[0] + points[1]))
usersR2[1] = convexHull(points[2] + points[3], len(points[2] + points[3]))
for j in range(2):
    for p in points[j * 2] + points[j * 2 + 1]:
        if in_hull(usersR2[j], p):
            uR2[j] = uR2[j] + 1
for j in range(4):
    for p in points[j]:
        if in_hull(users[j], p):
            u[j] = u[j] + 1
if uR2[0] > uR2[1]:
    if u[0] > u[1]:
        print("Winner = 1")
        print("Score = ", uR2[0])
    else:
        print("Winner = 2")
        print("Score = ", uR2[0])
else:
    if u[2] > u[3]:
        print("Winner = 3")
        print("Score = ", uR2[1])
    else:
        print("Winner = 4")
        print("Score = ", uR2[1])
