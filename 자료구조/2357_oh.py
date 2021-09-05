# 이러면 되는줄알았는데 min, max 자체가 탐색하는 알고리즘이 느린듯.
# 시간초과
# 결과는 맞음.

import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

nums = [0]*N

for i in range(N):
    num_input = int(input())
    nums[i] = num_input

for i in range(M):
    start, end = map(int, input().split())
    m_list = []
    for j in range(start-1, end):
        m_list.append(nums[j])
    print(min(m_list), max(m_list))


