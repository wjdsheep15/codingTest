'''
Queue 테스트
'''

import heapq

h = []

heapq.heappush(h, 123)
heapq.heappush(h, 789)
heapq.heappush(h, 456)
while len(h):
    print(heapq.heappop(h))