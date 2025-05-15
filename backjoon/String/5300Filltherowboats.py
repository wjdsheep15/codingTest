"""
문제
Captain Jack decides to to take over a rival’s ship. He needs to send his henchmen over on rowboats that can hold 6 pirates each. You will help him count out pirates in groups of 6. The last rowboat may have fewer than 6 pirates. To make your task easier each pirate has been assigned a number from 1 to N.

입력
The input will be N, the number of pirates you need to send over on rowboats.

출력
The output will be the number of each pirate separated by spaces, with the word ”Go!” after every 6th pirate, and after the last pirate.

예제 입력 1
10
예제 출력 1
1 2 3 4 5 6 Go! 7 8 9 10 Go!
예제 입력 2
18
예제 출력 2
1 2 3 4 5 6 Go! 7 8 9 10 11 12 Go! 13 14 15 16 17 18 Go!

"""
import sys
input = sys.stdin.readline
n = int(input())
for i in range(1, n):
    if i % 6 == 0:
        print(i, 'Go!', end=" ")
    else:
        print(i, end=" ")
print(n, 'Go!')