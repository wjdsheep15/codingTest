'''
FizzBuzz 문제는
# 입력
FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 한 줄에 하나씩 주어집니다. 각 문자열의 길이는
$8$ 이하입니다. 입력이 항상 FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열에 대응됨이 보장됩니다.

Fizz
Buzz
11

# 출력
연속으로 출력된 세 개의 문자열 다음에 올 문자열을 출력하세요. 여러 문자열이 올 수 있는 경우, 아무거나 하나 출력하세요.
Fizz
'''

a = input()
b = input()
c = input()
e = 0
if a != 'FizzBuzz' and a != 'Fizz' and a != 'Buzz':
    e = int(a)+3

if e == 0 and b != 'FizzBuzz' and b != 'Fizz' and b != 'Buzz':
    e = int(b)+2

if e == 0 and c != 'FizzBuzz' and c != 'Fizz' and c != 'Buzz':
    e = int(c)+1

if e % 3 == 0 and e % 5 == 0:
    print('FizzBuzz')
elif e % 3 == 0 and e % 5 != 0:
    print('Fizz')
elif e % 3 != 0 and e % 5 == 0:
    print('Buzz')
else:
    print(e)
