'''
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

5
3 4
1 1
1 -1
2 2
3 3

# 출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
1 -1
1 1
2 2
3 3
3 4

sort하면 1인자 2인자 순으로 자동 정렬이 된다

# 첫 번째 값 기준 오른차순
li.sort(key=lambda x : x[0])

# 두번째 값 기준 오른차순
li.sort(key = lambda x: (x[1], x[0]))
'''

import sys

input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
li.sort()

for x, y in li:
    print(x, y)