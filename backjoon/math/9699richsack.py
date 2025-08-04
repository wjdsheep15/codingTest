"""
문제
Several sacks of rice need to be transported to five Orphanage Houses. The heaviest sack will go to Orphanage House Al-Ameen because it has the most number of orphanges. The lightest will be sent to Orphanage House Mutiara due to the small number of children staying there. Given a row of rice sacks, decide which sack goes to Al-Ameen?

입력
The first line is an integer that represent the number of case. The following lines have 5 integers indicating the weights of 5 rice sacks, each separated by a blank. No sack will have a weight of more than 100 unit.

출력
For each test case, the output contains a line in the format Case #x: followed by a sequence of integers, where x is the case number (starting from 1) and an integer that indicates the weight of a rice sack that will go to Al-Ameen.

예제 입력 1
4
1 6 10 5 20
5 10 25 3 1
30 15 5 1 8
7 4 20 50 5
예제 출력 1
Case #1: 20
Case #2: 25
Case #3: 30
Case #4: 50
"""
import sys

input = sys.stdin.readline

for i in range(int(input())):
    res = max(map(int, input().split()))
    print(f"Case #{i+1}: {res}")