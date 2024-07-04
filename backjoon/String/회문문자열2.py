'''
문자열 s가 주어지면 s가 최대 문자 1개까지 지워서 회문문자열이 되면 “YES"를 출력하고, 그 렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요.
'''

s = list(map(str, input()))
startIndex = 0
endIndex = len(s)-1

cnt = 0

while startIndex < endIndex:
    if s[startIndex] == s[endIndex]:
        startIndex += 1
        endIndex -= 1
    elif s[startIndex + 1] == s[endIndex]:
        cnt += 1
        startIndex += 1
    else :
        cnt += 1
        endIndex -= 1

if cnt >= 2:
    print("NO")
else:
    print("YES")