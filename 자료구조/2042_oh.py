# 이것도 시간초과.. 참나
# 결과는 맞음.

import sys

def input():
    return sys.stdin.readline().rstrip()

n_m_k = list(map(int, input().split()))
print(n_m_k)
n = n_m_k[0]
m = n_m_k[1]
k = n_m_k[2]

num_list = [0]*n
for i in range(n):
    num_list[i] = int(input())
    

for j in range(m+k):
    option_input = list(map(int, input().split()))
    if option_input[0] == 1:
        num_list[option_input[1]-1] = option_input[2]

    elif option_input[0] == 2:
        sum_list = []
        for k in range(option_input[1]-1,option_input[2]):
            sum_list.append(num_list[k])
        
        print(sum(sum_list))
