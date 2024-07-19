'''
철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태 울수가 없다. 철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램을 작성하세요.


# 입력
첫 번째 줄에 자연수 C(1<=C<=100,000,000)와 N(1<=N<=30)이 주어집니다. 둘째 줄부터 N마리 바둑이의 무게가 주어진다.

# 입력 예제 1
259 5
81
58
42
33
61

# 출력 에제 1
242
'''
# def solved(pondList, s):
#     maxSum = 0
#     for i in range(pondList):
#         maxSum += i
#         pondList.pop(i)
#         if maxSum <= ln:
#             for i in range(pondList):
#                 solved(pondList, i)
#     return
#
# ln, n = map(int, input().split())
# pondList = []
# visitedList = [False for _ in range(n)]
# for _ in range(n):
#     pondList.append(int(input()))

# solved(pondList,  0)


def DFS(L,subTotal,tsum):
    #subTotal:태운 바둑이들 무게 합
    #tsum:지금까지 판별한 바둑이들 무게 합(안태웠을수도있음)
    global maximum
    if subTotal>c or total-tsum+subTotal<maximum:
        return
    if L==n:
        if maximum<subTotal:
            maximum=subTotal
    else:
        DFS(L+1,subTotal+a[L],tsum+a[L])
        DFS(L+1,subTotal,tsum+a[L])

c,n=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
total=sum(a)
maximum=0
DFS(0,0,0)
print(maximum)
