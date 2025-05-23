'''
문제
다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
fibonacci(0)은 0을 출력하고, 0을 리턴한다.
fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

출력
각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

예제 입력 1
3
0
1
3

예제 출력 1
1 0
0 1
1 2
'''


# def fibonacci(N):
#     global zeroCount
#     global oneCount
#     if N == 0:
#         zeroCount += 1
#         return 0
#     elif N == 1:
#         oneCount += 1
#         return 1
#     else:
#         return fibonacci(N - 1) + fibonacci(N - 2)
#
# import sys
# input = sys.stdin.readline
#
# for _ in range(int(input())):
#     zeroCount = 0
#     oneCount = 0
#     fibonacci(int(input()))
#     print(zeroCount, oneCount)

import sys
input = sys.stdin.readline

# 메모이제이션을 위한 배열 초기화
dp = [(0, 0)] * 41  # 최대 N이 40이라 가정 (문제에 따라 조정 가능)

# 초기 값 설정
dp[0] = (1, 0)  # fibonacci(0)의 결과: (zeroCount, oneCount)
dp[1] = (0, 1)  # fibonacci(1)의 결과: (zeroCount, oneCount)

# 모든 피보나치 수의 zeroCount와 oneCount 미리 계산
for i in range(2, 41):
    dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])

# 입력 처리 및 결과 출력
for _ in range(int(input())):
    N = int(input())
    print(dp[N][0], dp[N][1])


