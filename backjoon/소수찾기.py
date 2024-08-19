'''
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
'''

index = input()
numbers = list(map(int, input().split()))
count = 0
for i in numbers:
    num_count = 0
    if i == 1:
        continue
    for j in range(2,i):
        if i % j == 0:
            num_count += 1
    if num_count == 0:
        count += 1

print(count)


