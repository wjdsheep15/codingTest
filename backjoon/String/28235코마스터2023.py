"""
문제
송도고등학교에서 주최하는 첫 중고등학생 대상 알고리즘 대회, "코드마스터 2023"이 열렸다!

이 대회가 중고등학생들에게 인기 있는 알고리즘 대회이자 오프라인 이벤트로서 자리매김할 수 있도록 운영진은 각고의 준비를 했다.

대회를 시작하며 다음 네 가지 구호에 맞춰 알맞은 응원을 하는 프로그램을 작성하여라.

구호 SONGDO에 대해 HIGHSCHOOL로 응원.
구호 CODE에 대해 MASTER로 응원.
구호 2023에 대해 0611로 응원.
구호 ALGORITHM에 대해 CONTEST로 응원.
입력
첫 번째 줄에 네 가지 구호 중 한 가지에 해당하는 문자열이 주어진다.

출력
주어진 구호에 맞춰 알맞은 응원에 해당하는 문자열을 출력한다.

예제 입력 1
SONGDO
예제 출력 1
HIGHSCHOOL
"""

import sys
input = sys.stdin.readline

st = str(input().strip())
if st == "SONGDO":
    print("HIGHSCHOOL")
elif st == 'CODE':
    print("MASTER")
elif st == '2023':
    print("0611")
else:
    print("CONTEST")