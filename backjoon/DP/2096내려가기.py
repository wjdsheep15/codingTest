"""
문제
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 이 제약 조건을 그림으로 나타내어 보면 다음과 같다.



별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다. 숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.

입력
첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.

출력
첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.

예제 입력 1
3
1 2 3
4 5 6
4 9 0
예제 출력 1
18 6
예제 입력 2
3
0 0 0
0 0 0
0 0 0
예제 출력 2
0 0
"""
import sys
input = sys.stdin.readline

# T = int(input())
# graph = [list(map(int, input().split())) for _ in range(T)]
# max_vaule = 0
# min_value = int(1e9)
# dp = [[0, 0] for _ in range(3)]
# dp[0][0], dp[0][1] = graph[0][0], graph[0][0]
# dp[1][0], dp[1][1] = graph[0][1], graph[0][1]
# dp[2][0], dp[2][1] = graph[0][2], graph[0][2]
#
# for i in range(1, T):
#     for j in range(3):
#         dp[j][0] = dp[j][0] + max(graph[i][j-1 if j != 0 else j], graph[i][j], graph[i][j + 1 if j != 2 else j])
#         dp[j][1] = dp[j][1] + min(graph[i][j - 1 if j != 0 else j], graph[i][j], graph[i][j + 1 if j != 2 else j])
#
# max_vaule = max(dp[0][0], dp[1][0], dp[2][0])
# min_value = min(dp[0][1], dp[1][1], dp[2][1])
# print(max_vaule, min_value)




N = int(input())
# 맨 처음 세개의 숫자를 입력받아 DP의 초기 값을 설정한다.
arr = list(map(int, input().split()))
maxDP = arr
minDP = arr
for _ in range(N - 1):
    arr = list(map(int, input().split()))
    # 세가지 값을 입력받을 때마다, DP에 새롭게 갱신한다.
    maxDP = [arr[0] + max(maxDP[0], maxDP[1]), arr[1] + max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]
    minDP = [arr[0] + min(minDP[0], minDP[1]), arr[1] + min(minDP), arr[2] + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))