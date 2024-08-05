'''
매개변수 n에 도시의 수N(N<=100)과 M(M<=200)개의 간선 정보가 edges에 주어진다. 간선정보는 1번 도시와 2번도시가 연결되고 그 비용이 13이면 “1 2 13”으로 주어진다.
▣ 출력설명
모든 도시에서 모든 도시로 이동하는데 드는 최소 비용을 아래와 같이 출력해보세요. 자기자신으로 가는 비용은 0입니다. i번 정점에서 j번 정점으로 갈 수 없을 때는 비용을 “M"으 로 합니다.

▣ 매개변수 형식 1
5, [[1, 2, 6], [1, 3, 3], [3, 2, 2], [2, 4, 1], [2, 5, 13], [3, 4, 5], [4, 2, 3], [4, 5, 7]]

▣ 출력 형식 1
0, 5, 3, 6, 13
M, 0, M, 1, 8
M, 2, 0, 3, 10
M, 3, M, 0, 7
M, M, M, M, 0
'''
# 함수
def checkCost(startNode, endNode, sumCost):
    global minCost
    global grap
    global visited

    if startNode == endNode:
        if minCost > sumCost:
            minCost = sumCost
            return

    if visited[startNode] == True:
        return

    visited[startNode] = True

    if len(grap[startNode]) != 0:
        for node, costs in grap[startNode]:
            if not visited[node]:
                checkCost(node, endNode, sumCost + costs)

    visited[startNode] = False

# ndoe edges 설정하기
input_list = eval(input())
n = input_list[0]
edges = input_list[1]

# 리스트 | 그래프 설정
grap = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for n, s, cost in edges:
    grap[n].append((s, cost))

print(grap)

result = [[None for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n + 2):  # i를 n+1이 아닌 n으로 설정
    for j in range(1, n + 2):  # j도 0이 아닌 1부터 시작
        minCost = float('inf')
        checkCost(i, j, 0)  # j+1을 j로 수정
        result[i - 1][j - 1] = minCost if minCost != float('inf') else 'M'  # 인덱스 맞추기

for i in result:
    print(*i)