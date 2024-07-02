'''
상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

폭발은 다음과 같은 과정으로 진행된다.

문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.

폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.
'''

'''
풀이 방식 현제 먼제 만든 로직은 복잡도 O(nxm)이 되는 방식으로 시간에서 문제가 발생하였다.
그래서 다른 풀이법을 보니 stack을 사용하며, 빼야하는 마지막 글자가 들어가면 그때부터 비교하여 문자를 빼는 형식으로 진행이 되었다.
그점 기억을하자
'''
# import sys
#
# # main
# strlist = list(sys.stdin.readline().rstrip())
# removeChar = sys.stdin.readline().rstrip()
# index = len(removeChar)
# cnt = 0
# while cnt < index:
#     if removeChar[cnt] in strlist:
#         strlist.remove(removeChar[cnt])
#     else:
#         cnt += 1
# if strlist:
#     print(''.join(strlist))
# else:
#     print("FRULA")


import sys
x = list(sys.stdin.readline().strip())
M = list(sys.stdin.readline().strip())
m = len(M)
stack = []
for i in x:
    stack.append(i)
    if stack[len(stack)-m:len(stack)] == M: #스택의 끝부터 M의 글자열 크기까지 자른게 M과 같다면
        for _ in range(m): # m의 길이만큼
            stack.pop() # stack에서 꺼내준다!
if stack:
    print(*stack, sep='')
else:
    print("FRULA")

