'''
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 입력
3 16

#출력
3
5
7
11
13
'''
# 에라토스테네스의 체


import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())
li = [i for i in range(a, b + 1)]
sqrt_b = int(math.sqrt(b))

# 소수를 찾기 위한 리스트
primes = []

for num in li:
    if num < 2:  # 2보다 작은 수는 소수가 아님
        continue
    is_prime = True
    # num이 sqrt_b보다 작거나 같은 경우
    for j in range(2, int(math.sqrt(num)) + 1):  # num의 제곱근까지 확인
        if num % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

for prime in primes:
    print(prime)
