'''
영어 알파벳과 특수문자로 구성된 문자열이 주어지면 영어 알파벳만 뒤집고,
특수문자는 자기 자리에 그대로 있는 문자열을 만들어 반환하는 프로그램을 작성하세요.
'''
# 첫 번째 풀이 방식 그냥 뒤집어서 사용 그러나 이 방식은 시간이 오래걸리는 문제점 이있음
'''
풀이 : [~ , #, a, b, c, ^, *]  이렇게 문자열을 입력 받으면 인덱스 2개를 둔다
startIndex, endIndex
while 문으로 처음 문자와 마지막 문자를 비교하면서 인덱스를 하나씩 이동하여 풀이, 조건( startIndex < endIndex )
'''


# 첫 번째 풀이
# # 알파벳 판별
# def is_alphabet(s):
#     for i in s:
#         if i.isalpha():
#             chrList.append(i)
#
#
# # 프린트하기
# def is_print(s):
#     chrList.reverse()
#     index = 0
#     for i in range(len(s)):
#         if s[i].isalpha():
#             s[i] = chrList[index]
#             index += 1
#         print(s[i], end='')

# 두번째 풀이
def is_alphabet(s):
    start_index = 0
    end_index = len(s) - 1
    while start_index < end_index:
        if s[start_index].isalpha() is False:
            start_index += 1
        elif s[end_index].isalpha() is False:
            end_index -= 1
        else:
            s[start_index], s[end_index] = s[end_index], s[start_index]
            start_index += 1
            end_index -= 1


s = list(input())
chrList = []is_alphabet(s)
print(''.join(s))
