'''

문제
2020년에 입학한 헌내기 도연이가 있다. 도연이는 비대면 수업 때문에 학교에 가지 못해 학교에 아는 친구가 없었다. 드디어 대면 수업을 하게 된 도연이는 어서 캠퍼스 내의 사람들과 친해지고 싶다.

도연이가 다니는 대학의 캠퍼스는 N x M 크기이며 캠퍼스에서 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다. 예를 들어, 도연이가 (
x, y)에 있다면 이동할 수 있는 곳은 (x+1, y), (x, y+1), (x-1, y), (x, y-1)이다. 단, 캠퍼스의 밖으로 이동할 수는 없다.

불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램을 작성해보자.

입력
첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수
N (1 <= N <= 600),
M (1 <= M <= 600)이 주어진다.

둘째 줄부터
N개의 줄에는 캠퍼스의 정보들이 주어진다. O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.

출력
첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 TT를 출력한다.
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def meet_friends(x, y):
    global graph, cnt, N, M, visited

    if x < 0 or x >= N or y < 0 or y >= M:
        return
    if visited[x][y] or graph[x][y] == 'X':
        return

    visited[x][y] = True

    if graph[x][y] == 'P':
        cnt += 1

    meet_friends(x + 1, y)
    meet_friends(x - 1, y)
    meet_friends(x, y + 1)
    meet_friends(x, y - 1)





N, M = map(int, input().split())
graph = []
visited = [[False] * M for _ in range(N)]
cnt = 0
for _ in range(N):
    graph.append(list(map(str, input().strip())))

start_x, start_y = 0, 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            start_x = i
            start_y = j
            break

meet_friends(start_x, start_y)

print(cnt if cnt > 0 else 'TT')