import numpy as np

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def angle(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


n = int(input())
for i in range(n):
    p1 = np.array(input().split()).astype(np.float_)
    p2 = np.array(input().split()).astype(np.float_)
    p3 = np.array(input().split()).astype(np.float_)
    target = np.array(input().split()).astype(np.float_)
    start = np.array(input().split()).astype(np.float_)
    v = np.array(input().split()).astype(np.float_)
    # inja khodamam nemidoonam che gohi mikhoram
    v1 = p3 - p1
    v2 = p2 - p1
    cp = np.cross(v1, v2)
    a, b, c = cp
    d = np.dot(cp, p3)
    #  print('The equation is {0}x + {1}y + {2}z = {3}'.format(a, b, c, d))

    tempSoorat = d - a * start[0] - b * start[1] - c * start[2]
    tempMakhraj = a * v[0] + b * v[1] + c * v[2]
    if tempMakhraj == 0:
        print("outside the triangle!")
        continue
    t = tempSoorat / tempMakhraj
    finalPoint = np.array([t * v[0] + start[0], t * v[1] + start[1], t * v[2] + start[2]])
    #  print(finalPoint)
    v1 = np.array(p1 - finalPoint)
    v2 = np.array(p2 - finalPoint)
    v3 = np.array(p3 - finalPoint)
    if round(angle(v1, v2) + angle(v1, v3) + angle(v2, v3), 2) == 6.28:
        dist = np.linalg.norm(finalPoint - target)
        result = ' '.join(map(str, list(np.round_(finalPoint, 1))))
        print('[' + result + ']', round(dist, 1))

    else:
        print("outside the triangle!")
        continue
