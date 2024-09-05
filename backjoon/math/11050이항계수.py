'''
문제
자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램을 작성하시오.

# 입력
첫째 줄에 N과 K가 주어진다. 1 ≤ N ≤ 10, 0 ≤ K ≤ N

# 출력
이항 계수를 출력
'''

a, b = map(int, input().split(' '))
num = 1
for i in range(a-b +1, a+1):
    num *= i
div = 1
for i in range(1, b+1):
    div *= i

print(num//div)
