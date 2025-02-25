'''
아래 <그림 1>과 같이 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다. 주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다.



전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수) 이라면 종이를 자르는 규칙은 다음과 같다.

전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 <그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다. 나누어진 종이 I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 모두 같은 색으로 칠해져 있지 않으면 같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. 이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.

위와 같은 규칙에 따라 잘랐을 때 <그림 3>은 <그림 1>의 종이를 처음 나눈 후의 상태를, <그림 4>는 두 번째 나눈 후의 상태를, <그림 5>는 최종적으로 만들어진 다양한 크기의 9장의 하얀색 색종이와 7장의 파란색 색종이를 보여주고 있다.



입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

출력
첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

예제 입력 1
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

예제 출력 1
9
7
'''

# import sys
#
# input = sys.stdin.readline
#
#
# def visited_def(f, e):
#     for x in range(f, e):
#         for y in range(f, e):
#             visited[x][y] = True
#
#
# def color_cnt(s):
#     global graph, visited, N, blue_cnt, white_cnt
#     for i in range(0, N, s):
#         graph_sum = 0
#         if visited[i][i] is False:
#             for x in range(i, i + s):
#                 for y in range(i, i + s):
#                     graph_sum += graph[x][y]
#             if graph_sum == 0:
#                 white_cnt += 1
#                 visited_def(i, i + s)
#             if graph_sum == s * s:
#                 blue_cnt += 1
#                 visited_def(i, i + s)
#
#         else:
#             continue
#     if s == 1:
#         return
#     else:
#         color_cnt(s // 2)
#
#
# N = int(input())
# blue_cnt = 0
# white_cnt = 0
#
# graph = []
# visited = [[False] * N for _ in range(N)]
# for _ in range(N):
#     flist = list(map(int, input().split()))
#     graph.append(flist)
#
# print(graph)
# print(visited)
#
# color_cnt(N)
#
# # 하얀색 색종이
# print(white_cnt)
# # 파란색 색종이
# print(blue_cnt)

import sys

input = sys.stdin.readline

def count_color(x, y, size):
    global white_cnt, blue_cnt

    # 첫 번째 칸의 색상 저장
    first_color = graph[x][y]

    # 색상이 모두 같은지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if graph[i][j] != first_color:  # 하나라도 다르면 분할
                new_size = size // 2
                count_color(x, y, new_size)  # 왼쪽 위
                count_color(x, y + new_size, new_size)  # 오른쪽 위
                count_color(x + new_size, y, new_size)  # 왼쪽 아래
                count_color(x + new_size, y + new_size, new_size)  # 오른쪽 아래
                return

    # 모두 같은 색이라면 해당 색 카운트 증가
    if first_color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1


# 입력 받기
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 색종이 개수 초기화
white_cnt = 0
blue_cnt = 0

# 분할 정복 실행
count_color(0, 0, N)

# 결과 출력
print(white_cnt)  # 하얀색 색종이 개수
print(blue_cnt)  # 파란색 색종이 개수


