'''
입력
첫 줄에 과일의 개수
N이 주어집니다.
(1 <= N <= 200,000)

둘째 줄에 탕후루에 꽂힌 과일을 의미하는


출력
문제의 방법대로 만들 수 있는 과일을 두 종류 이하로 사용한 탕후루 중에서, 과일의 개수가 가장 많은 탕후루의 과일 개수를 첫째 줄에 출력하세요.

예제 입력 1
5
5 1 1 2 1
예제 출력 1
4
'''
from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
num_li = list(map(int, input().split()))

fruit_count = defaultdict(int)  # 과일 개수를 저장하는 딕셔너리
left = 0  # 왼쪽 포인터
max_length = 0  # 최대 길이

for right in range(N):
    fruit_count[num_li[right]] += 1  # 새로운 과일 추가

    while len(fruit_count) > 2:  # 과일 종류가 2개를 초과하면
        fruit_count[num_li[left]] -= 1  # 왼쪽 과일 개수 감소
        if fruit_count[num_li[left]] == 0:
            del fruit_count[num_li[left]]  # 0이 되면 삭제
        left += 1  # 왼쪽 포인터 이동

    max_length = max(max_length, right - left + 1)  # 최대 길이 갱신

print(max_length)