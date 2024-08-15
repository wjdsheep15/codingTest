'''
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.
'''

def remove_node(num):
    if node_list[num] == -1:
        node_list.clear()
        return
    node_list[num] = -2
    for i in range(len(node_list)):
        if num == node_list[i]:
            remove_node(i)


def count_leave(node):
    global node_count
    visited[node] = True
    is_leaf = True  # 리프 노드인지 여부를 판단할 변수
    for i in range(len(node_list)):
        if node_list[i] == node and not visited[i]:
            count_leave(i)
            is_leaf = False  # 자식이 있으면 리프 노드가 아님
    if is_leaf and node_list[node] != -2:  # 자식이 없는 경우 리프 노드로 카운트
        node_count += 1


a = int(input())
node_list = list(map(int, input().split(' ')))
c = int(input())

# 필요 없는 노드 제거 :  -2
remove_node(c)
start_node = 0
node_count = 0
if len(node_list) > 0:
    for i in range(a):
        if node_list[i] == -1:
            start_node = i
    visited = [False for _ in range(a)]
    count_leave(start_node)

print(node_count)