"""
문제
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.

예제 입력 1
1000
예제 출력 1
517691607
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

MOD = 1000000007

dp = defaultdict(int)

dp[0] = 0
dp[1] = 1
dp[2] = 1


def fibonacci(n):
    if not dp[n]:
        if n & 1:
            fn = fibonacci(n // 2)
            fnp = fibonacci(n // 2 + 1)

            dp[n] = (fn ** 2 + fnp ** 2) % MOD
        else:
            fn = fibonacci(n // 2)
            fnm = fibonacci(n // 2 - 1)

            dp[n] = (fn * (fn + 2 * fnm)) % MOD

    return dp[n]

N = int(input())

fibonacci(N)

print(dp[N])