N = int(input())
for i in range(N):
    stringList = (list(map(str, input().split())))
    for word in stringList:
        print(''.join(list(word)[::-1]), end=' ')
    print()