'''
앞에서 읽을 때나 뒤에서 읽을 때나 같은 문자열을 회문 문자열이라고 합니다.
문자열이 입력되면 해당 문자열이 회문 문자열이면 "YES", 회문 문자열이 아니면 “NO"를 출력 하는 프로그램을 작성하세요.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.
'''

s = input()
s = s.upper()
count = 0
for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        count += 1

if count > 0:
    print('NO')
else:
    print('YES')

