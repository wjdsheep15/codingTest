'''
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.

1+1+1+1
2+1+1 (1+1+2, 1+2+1)
2+2
1+3 (3+1)
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
'''

'''
풀이 방법 점화식 사용하기 


'''

# # 2, 1 로만 판단하기
# def div2(number):
#     num2 = number // 2
#     return num2
#
#
# def div3(number):
#     count = 0
#     num3 = number // 3
#     for i in range(1, num3+1):
#         min_num = number - (3 * i)
#         if min_num >= 2:
#             count += div2(min_num)
#             count += 1
#         else:
#             count += 1
#     return count
#
#
# n = input()
# for _ in range(int(n)):
#     m = int(input())
#     cnt = 0
#     cnt += div3(m)
#     cnt += div2(m)
#     cnt += 1
#
#     print(cnt)

t = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i - 2]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])
