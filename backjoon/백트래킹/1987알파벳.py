'''
문제
세로
칸, 가로
칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (
행
열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에
과
가 빈칸을 사이에 두고 주어진다. (
1 ≤ R,C ≤ 20) 둘째 줄부터
개의 줄에 걸쳐서 보드에 적혀 있는
개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

예제 입력
2 4
CAAB
ADCB

예제 출력
3
'''
from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

R, C = map(int, input().split())
board = [input() for _ in range(R)]
chk = [[set() for _ in range(C)] for _ in range(R)]
ans = 0

def is_valid_coord(y,x):
    return 0 <= y < R and 0 <= x < C

dq = deque()
chk[0][0].add(board[0][0])
dq.append((0, 0, board[0][0]))
while dq:
    y, x, s = dq.popleft()
    ans = max(ans, len(s))

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if is_valid_coord(ny, nx) and board[ny][nx] not in s:
            ns = s + board[ny][nx]
            if ns not in chk[ny][nx]:
                chk[ny][nx].add(ns)
                dq.append((ny, nx, ns))

print(ans)

