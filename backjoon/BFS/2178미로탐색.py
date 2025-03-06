'''
NxM 크기의 배열로 표현되는 미로가 있다.
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
4 6
101111
101010
101011
111011

'''

from collections import deque
import sys
input = sys.stdin.readline

def bfs(maze, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]  # 방문 여부 저장
    visited[0][0] = True  # 시작점 방문 처리

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  # 거리 갱신
                visited[nx][ny] = True  # 방문 처리
                queue.append((nx, ny))

    return maze[n - 1][m - 1]


# 입력 받기
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 최소 칸 수 출력
print(bfs(maze, n, m))
