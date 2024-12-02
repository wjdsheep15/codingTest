'''
첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답을 말해줬으면 좋겠어!!!. 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력하면 돼. 그럼 땡큐~

# 입력
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna

# 출력
Pikachu
26
Venusaur
16
14
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pockList = {}
for i in range(N):
    a = input().rstrip()
    pockList[i] = a
    pockList[a] = i

for _ in range(M):
    A = input().rstrip()
    if A[0].isdigit():
        number = int(A) - 1
        print(pockList[number])
    else:
        print(pockList[A] + 1)
