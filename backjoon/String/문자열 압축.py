'''
문자열 압축
알파벳 대문자로 이루어진 문자열을 입력받아 같은 문자가 연속으로 반복되는 경우 반복되는 문자 바로 오른쪽에 반복 횟수를 표기하는 방법으로 문자열을 압축하는 프로그램을 작성하세요.
단 반복횟수가 1인 경우 생략합니다.
'''

charList = []

# 검출하기
def solved(s):
    for i in s:
        if len(charList) == 0:
            charList.append(i)
        elif charList[len(charList) - 1] != i:
            charList.append(i)
        else:
            continue


# 출력하기
def printNumber():
    for i in charList:
        print(i + str(s.count(i)), end='')


# 메인 로직
s = input()
solved(s)
printNumber()
