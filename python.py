a1 = [[0] * 5] * 3
a1[1][1] = 99
print(a1)


a2 = [[0] * 5 for _ in range(3)]
a2[1][1] = 99
print(a2)