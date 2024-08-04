'''
아래의 가중치 방향그래프에서 1번 정점(출발정점)에서 특정 정점(도착정점)까지의 최소 거리 비용을 출력하는 프로그램을 작성하세요. (경로가 없으면 -1를 출력한다)

# 입력
매개변수 n에 정점의 수 N(1<=N<=20)주어지고, 매개변수 edges에 간선정보가 주어집니다. [1, 2, 12]는 1번 정점에서 2번 정점으로 가는 비용이 12라는 뜻입니다. 각 간선의 비용값은 20을 넘지 않습니다.
매개변수 end에 도착정점이 주어집니다.


6, [[1, 2, 12], [1, 3, 4], [2, 1, 2], [2, 3, 5], [2, 5, 5], [3, 4, 5], [4, 2, 2], [4, 5, 5], [6, 4, 5]], 5

정점의 수 : 6
간선 정보 [[시작, 끝, 비용값]
도착정점 : 5
®
# 출력
14
'''

# 함수
def startMinist(startNode, grap, endNode, sumDist):
    global globalMinDists
    global visited
    if visited[startNode] == True:
        return

    if startNode == endNode:
        if globalMinDists > sumDist:
            globalMinDists = sumDist
            return
    visited[startNode] = True
    for i in grap[startNode]:
        if not visited[i[0]]:
            startMinist(i[0], grap, endNode, sumDist + i[1])

    visited[startNode] = False  # 백트래킹 시 방문 기록을 되돌림

#입력 받는 존
input_list = eval(input())
n = input_list[0]
t = input_list[1]
ep = input_list[2]
globalMinDists = float('inf')
# 그래프 만드는 존
grap = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for s, e, cost in t:
    grap[s].append((e, cost))

startMinist(1, grap, ep, 0)
print(globalMinDists)