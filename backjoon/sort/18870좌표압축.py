'''
문제
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

입력
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력
첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

예제 입력 1
5
2 4 -10 4 -9

예제 출력 1
2 3 0 3 1
'''

import sys
input = sys.stdin.readline

N = int(input())
num_li = list(map(int, input().split()))
s = sorted(set(num_li))

index_dict = {value: index for index, value in enumerate(s)}
print(' '.join(map(str, (index_dict[num] for num in num_li))))


