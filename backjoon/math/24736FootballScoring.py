"""
There are five ways to score points in american professional football:

Touchdown - 6 points
Field Goal - 3 points
Safety - 2 points
After touchdown
1 point (Field Goal or Safety) - Typically called the “Point after”
2 points (touchdown) - Typically called the “Two-point conversion”
(https://operations.nfl.com/the-rules/nfl-video-rulebook/scoring-plays/)

Given the box score values for two competing teams, calculate the point total for each team.

입력
There are two lines of input each containing five space-separated non-negative integers, T, F, S, P and C representing the number of Touchdowns, Field goals, Safeties, Points-after-touchdown and two-point Conversions after touchdown respectively. (0 ≤ T ≤ 10), (0 ≤ F ≤ 10), (0 ≤ S ≤ 10), (0 ≤ (P+C) ≤ T). The first line represents the box score for the visiting team, and the second line represents the box score for the home team.

출력
The single output line consists of two space-separated integers showing the visiting score and the home score respectively.

예제 입력 1
1 3 0 0 1
3 1 1 1 1
예제 출력 1
17 26
"""
import sys
input = sys.stdin.readline


def calculate_score(data):
    T, F, S, P, C = data
    return T * 6 + F * 3 + S * 2 + P * 1 + C * 2


visitor = list(map(int, input().split()))
home = list(map(int, input().split()))

visitor_score = calculate_score(visitor)
home_score = calculate_score(home)

print(visitor_score, home_score)
