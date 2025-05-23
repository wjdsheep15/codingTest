"""
문제
두 정수 n과 m이 주어졌을 때, 0 < a < b < n인 정수 쌍 (a, b) 중에서 (a2+b2+m)/(ab)가 정수인 쌍의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, n과 m이 주어진다. 두 수는 0보다 크고, 100보다 작거나 같다.

출력
각 테스트 케이스마다 문제의 조건을 만족하는 (a, b)쌍의 개수를 출력한다.

예제 입력 1
3
10 1
20 3
30 4
예제 출력 1
2
4
5
"""

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cnt = 0
    n, m = map(int, input().split())
    for a in range(1, n):
        for b in range(a+1, n):
            result = (a ** 2 + b ** 2 + m)/(a*b)
            if result % 1 == 0:
                cnt += 1
    print(cnt)
