a1 = [3] * 8
a2 = [3 for i in range(8)]
print(a1)
print(a2)

b1 = [*range(8)]
b2 = [i for i in range(8)]
print(b1)
print(b2)

c = [i + 10 for i in range(8)]
print(c)

d = [i ** 2 for i in range(8)]
print(d)

e1 = [[1] * 4] * 3 #주위! 이 방식으로 다차원 리스트 생성은 지양할 것
e2 = [[1] * 4 for _ in range(3)]
e3 = [[1 for _ in range(4)] for _ in range(3)]

print(e1)
print(e2)
print(e3)


a = [2, 4, 7, 5, 1, 8, 6, 3]
for i in a:
	even_or_odd = '짝' if i % 2 == 0 else '홀'
	print(i, even_or_odd)

b = [1 if j % 2 else 0 for j in a]
print(b)
