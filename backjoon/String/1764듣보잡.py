'''
문제
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

출력
듣보잡의 수와 그 명단을 사전순으로 출력한다.

# 입력
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

# 출력
2
# baesangwook
# ohhenrie
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
noListenArry = set([])
result_arry = []
for _ in range(N):
    noListenArry.add(input().strip())
for _ in range(M):
    noWatch = input().strip()
    if noWatch in noListenArry:
        result_arry.append(noWatch)

result_arry.sort()
print(len(result_arry))
for i in result_arry:
    print(i)


