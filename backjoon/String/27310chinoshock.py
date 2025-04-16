"""
sait2000은 아니메컵 서버를 열고 나서 가장 먼저 이모지 :chino_shock:부터 추가했다. :chino_shock:를 비롯한 여러 이모지를 사용해보던 sait2000은 :chino_shock:와 같이 이름에 언더바(_)가 들어간 이모지가 :chinoaww:와 같이 이름에 언더바가 들어가지 않은 이모지보다 더 타이핑하기 어렵다는 사실을 알게 되었다.

이모지는 하나의 콜론(:)으로 시작해서 하나의 콜론으로 끝나며, 콜론 사이의 문자들은 모두 영어 소문자 혹은 언더바(_) 중 하나로 주어진다. sait2000은 이모지의 입력 난이도를 이모지의전체길이콜론의개수언더바의개수
$(\text{이모지의 전체 길이}) +(\text{콜론의 개수}) +(\text{언더바의 개수})\times 5$로 정의했다. 이 정의에 따르면 :chino_shock:의 전체 길이는
$13$이고 콜론이
$2$개, 언더바가
$1$개이므로 입력 난이도가
$13+2+1\times 5=20$이 된다.

이모지가 주어졌을 때 이모지의 입력 난이도를 계산해 출력해보자.

입력
첫 번째 줄에 이모지가 주어진다. 주어지는 이모지는 항상 :chino로 시작하고 :로 끝나며, 전체 길이가
$7$ 이상
$32$ 이하이다.

출력
이모지의 입력 난이도를 출력한다.

예제 입력 1
:chino_shock:
예제 출력 1
20
예제 입력 2
:chinoaww:
예제 출력 2
12
예제 입력 3
:chino_very_shock:
예제 출력 3
30
"""
import sys
input = sys.stdin.readline

emoji = input()
emoji_len = len(emoji) -1
col_cnt = 0
under_cnt = 0
for i in emoji:
    if i == ':':
        col_cnt += 1
    elif i == '_':
        under_cnt += 1
    else:
        continue
print(emoji_len + col_cnt + (under_cnt * 5))
