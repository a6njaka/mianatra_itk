import numpy as np

date0 = [0.4, 0.3, 3338.0, 14019]
date1 = [11.2, 12.8, 3342.8, 14054]
date2 = [52.4, 77.8, 3362.1, 14210]
date3 = [83.5, 118.7, 3381.2, 14324]
# date3 = [111.9, 145.6, 3386.8, 14408]
# date3 = [91.5, 128.9, 3383.8, 14353]

a = [date1[0] - date0[0], date1[1] - date0[1], date1[2] - date0[2]]
b = [date2[0] - date1[0], date2[1] - date1[1], date2[2] - date1[2]]
c = [date3[0] - date2[0], date3[1] - date2[1], date3[2] - date2[2]]
d = [date1[3] - date0[3], date2[3] - date1[3], date3[3] - date2[3]]

print(a)
print(b)
print(c)
print(d)

print("*" * 40)
# print(a)
# print(date1)

M = np.array([a, b, c])
c = np.array(d)
y = np.linalg.solve(M, c)

for t in y:
    print("{:.04f}".format(t))

print("*" * 40)
test = [85.1, 120.7, 3381.2]
test = [11.2, 12.8, 3342.8, 3381.2]
test = [52.4, 77.8, 3362.1]
test = [83.5, 118.7, 3381.2]


def calc_cp(curent_value, y):
    test = curent_value
    CP = (test[0] - date0[0]) * y[0] + (test[1] - date0[1]) * y[1] + (test[2] - date0[2]) * y[2] + date0[3]
    print("Compteur principale={:.0f}".format(CP))

y = [1.22, 1.22, 1.37]

calc_cp([0.4, 0.3, 3338.0], y)
calc_cp([11.2, 12.8, 3342.8, 3381.2], y)
calc_cp([52.4, 77.8, 3362.1], y)
calc_cp([83.5, 118.7, 3381.2], y)
calc_cp([85.1, 120.7, 3381.2], y)
calc_cp([4.7, 6.1, 3339.7], y)
calc_cp([91.5, 128.9, 3383.8], y)
calc_cp([111.9, 145.6, 3386.8], y)
