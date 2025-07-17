"""
문제
You are lost in the museum and keep walking by a giant rock head that says “gum gum for jay jay” each time you walk by. Print out the number of times you have walked by the giant rock head after reading in the data file.

입력
The data file will contain an unknown number of lines.

출력
Print out the number of lines in the data file.
"""

import sys
input = sys.stdin.readline

count = 0

while True:
    a = list(str(input().strip()))
    if len(a) == 0:
        print(count)
        break
    count += 1