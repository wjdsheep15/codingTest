'''
첫 번째 줄에 문제의 개수N(1<=N<=20)과 제한 시간 M(10<=M<=300)이 주어집니다.
두 번째 줄부터 N줄에 걸쳐 문제를 풀었을 때의 점수와 푸는데 걸리는 시간이 주어집니다.
'''


def solved(index, sumScore, sumTime):
    global maxSum

    if maxSum < sumScore:
        maxSum = sumScore

    if index >= n:
        return

    if sumTime + problemList[index][1] > 20:
        solved(index + 1, sumScore, sumTime)

    else:
        sumScore += problemList[index][0]
        sumTime += problemList[index][1]

    solved(index + 1, sumScore, sumTime)


n, m = map(int, input().split())
problemList = []
for _ in range(n):
    problemList.append(list(map(int, input().split())))
print(problemList)
maxSum = 0
solved(0, 0, 0)
print(maxSum)
