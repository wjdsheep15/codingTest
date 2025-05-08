"""
문제
트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.



이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.



트리의 노드는 1부터 n까지 번호가 매겨져 있다.

입력
파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

출력
첫째 줄에 트리의 지름을 출력한다.

예제 입력 1
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
예제 출력 1
45
"""

# 시간 초과
# import sys
# from collections import deque
# from itertools import combinations
#
# input = sys.stdin.readline
# max_circle = 0
#
# def dfs(start, end):
#     global max_circle
#     que = deque([(start, 0)])
#     while que:
#         now_node, distance = que.popleft()
#
#         if now_node == end:
#             if max_circle < distance:
#                 max_circle = distance
#             break
#         else:
#             for next_node, next_distance in graph[now_node]:
#                 if next_node != now_node:
#                     que.append((next_node, distance + next_distance))
#
#
# node = int(input())
# graph = [[] for _ in range(node + 1)]
# parent_node = 0
# leaf_node = []
# for _ in range(1, node):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#     graph[b].append((a, c))
#     parent_node = a
#
# for i in range(1, node + 1):
#     if len(graph[i]) == 1 and i != 1:  # 루트 제외
#         leaf_node.append(i)
#
# for com in combinations(leaf_node, 2):
#     s, e = map(int, com)
#     dfs(s, e)
#
# print(max_circle)

# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())

tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))


def dfs(start, distance):
    for next, next_d in tree[start]:
        if visited[next] == -1:
            visited[next] = distance + next_d
            dfs(next, distance + next_d)


# 시작 정점에서 임의의 정점까지의 거리를 구하고 그 중 가장 먼 거리를 구한다.
visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
# 가장 먼 노드를 시작지점으로 하여 다시 한번 가장 긴 거리를 찾는다.
last_Node = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[last_Node] = 0
dfs(last_Node, 0)

print(max(visited))

# BFS
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))


def bfs(start):
    visited = [-1] * (n + 1)
    visited[start] = 0
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for next, next_d in tree[cur]:
            if visited[next] == -1:
                queue.append(next)
                visited[next] = visited[cur] + next_d
    m = max(visited)
    return [visited.index(m), m]


print(bfs(bfs(1)[0])[1])


