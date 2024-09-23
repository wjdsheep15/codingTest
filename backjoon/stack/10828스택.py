'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
'''


def stack_Obj(M):
    global stack

    if M == 'top':
        if len(stack) > 0:
            print(stack[-1])
            return
        else:
            print(-1)
            return
    if M == 'pop':
        if len(stack) > 0:
            print(stack.pop())
            return
        else:
            print(-1)
            return

    if M == 'size':
        print(len(stack))
        return
    if M == 'empty':
        if len(stack) > 0:
            print(0)
            return
        else:
            print(1)
            return

import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    in_li = list(map(str, input().split()))
    if 'push' in in_li:
        stack.append(in_li[1])
    else:
        stack_Obj(in_li[0])
