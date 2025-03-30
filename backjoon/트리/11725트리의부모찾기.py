"""
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

예제 입력 1
7
1 6
6 3
3 5
4 1
2 4
4 7
예제 출력 1
4
6
1
3
1
4
"""
import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())
graph = [[] for _ in range(T + 1)]
parent = [0] * (T + 1)

for _ in range(T - 1):
    i, n = map(int, input().split())
    graph[i].append(n)
    graph[n].append(i)

queue = deque([1])
while queue:
    node = queue.popleft()
    for next_node in graph[node]:
        if parent[next_node] == 0:  # 아직 부모가 정해지지 않은 경우
            parent[next_node] = node
            queue.append(next_node)

# 부모 출력
for i in range(2, T + 1):
    print(parent[i])