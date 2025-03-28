'''
<그림>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

예제 입력 1
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3
7
8
9
'''


def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1  # 현재 단지 크기 증가

    # 상하좌우 이동
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(nx, ny)


N = int(input())  # 지도 크기
grid = [list(map(int, input().strip())) for _ in range(N)]  # 지도 입력
visited = [[False] * N for _ in range(N)]  # 방문 여부 저장
complex_sizes = []  # 단지 크기 저장

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not visited[i][j]:  # 새로운 단지 발견
            count = 0
            dfs(i, j)
            complex_sizes.append(count)  # 단지 크기 저장

# 결과 출력
complex_sizes.sort()
print(len(complex_sizes))  # 총 단지 수
for size in complex_sizes:
    print(size)