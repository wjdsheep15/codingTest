"""
문제
Different countries use different coin denominations. For example, the USA uses 1, 5, 10, and 25. A desirable property of coin denominations is to have each coin at least twice the amount of its previous coin in sorted order. For example, the USA denominations have this property, but the coin denominations {1, 5, 6} do not (6 is not at least twice 5).

Given the coin denominations, you are to determine if the set has the above property.

입력
The first input line contains a positive integer, n, indicating the number of denomination sets to check. The sets are on the following n input lines, one set per line. Each set starts with an integer d (1 ≤ d ≤ 10), which is a count of various coin amounts in the set; this is followed by d distinct positive integers (each less than 1,000) giving each coin amount (assume the coin amounts are given in increasing order).

출력
At the beginning of each test case, output “Denominations: v” where v is the input values. Then, on the next output line, print a message indicating whether or not the set has the above property. Leave a blank line after the output for each test case. Follow the format illustrated in Sample Output.

예제 입력 1
2
4 1 5 10 25
3 1 5 6
예제 출력 1
Denominations: 1 5 10 25
Good coin denominations!

Denominations: 1 5 6
Bad coin denominations!
"""
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    result = True
    li = list(map(int, input().split()))
    for i in range(2, len(li)):
        if li[i] >= li[i-1] * 2:
            continue
        else:
            result = False
            break
    print("Denominations:", ' '.join(str(s) for s in li[1:]))
    if result:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()
