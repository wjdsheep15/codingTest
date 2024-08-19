'''
입력
입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

출력
각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.
'''
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    max_num = max(a, b, c)
    num1, num2, num3 = 0, 0, 0
    if a != max_num:
        num1 = a
    if b != max_num:
        num2 = b
    if c != max_num:
        num3 = c

    if max_num ** 2 == num1 ** 2 + num2 ** 2 + num3 ** 2:
        print('right')
    else:
        print('wrong')
