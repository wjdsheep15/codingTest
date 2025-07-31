"""
문제
There’s a pizza store which serves pizza in two sizes: either a pizza slice, with area A1 and price P1, or a circular pizza, with radius R1 and price P2.

You want to maximize the amount of pizza you get per dollar. Should you pick the pizza slice or the whole pizza?

입력
The first line contains two space-separated integers A1 and P1.

Similarly, the second line contains two space-separated integers R1 and P2.

It is guaranteed that all values are positive integers at most 103. We furthermore guarantee that the two will not be worth the same amount of pizza per dollar.

출력
If the better deal is the whole pizza, print ‘Whole pizza’ on a single line.

If it is a slice of pizza, print ‘Slice of pizza’ on a single line.

예제 입력 1
8 4
7 9

예제 출력 1
Whole pizza
"""

import sys
from math import pi
input = sys.stdin.readline

a1, p1 = map(int, input().split())
r2, p2 = map(int, input().split())

if p1/a1 < p2/(r2**2*pi):
    print("Slice of pizza")
else:
    print("Whole pizza")

