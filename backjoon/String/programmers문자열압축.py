'''
압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.
'''


def solution(s):
    answer = 0

    for i in range(len(s)-1):
        cnt = 0
        if s[i] == s[i+1]:
            cnt += 1
            


    return answer


s = list(input())
print(len(s))
solution(s)
