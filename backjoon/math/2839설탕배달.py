'''
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

3, 5
'''

import sys

input = sys.stdin.readline

num = int(input())
value = num // 5
five = 0
three = 0
while value > -1:
    inner = num - (value*5)
    if num < 5:
        if num == 3:
            three = 1
            break
        else:
            three = -1
            break
    elif inner % 3 == 0:
        five = value
        three = inner // 3
        break
    else:
        three = -1
    value -= 1

print(five + three)
