N, K=map(int, input().split(' '))
unit_list=list()
ans=0

for i in range(N): #0부터 N-1까지 총 N개
    unit=int(input())
    unit_list.append(unit)
unit_list.reverse() #입력을 오름차순으로 받았으니 reverse 시키면 내림차순이 됨

i=0
while K>0: 
    ans += K//unit_list[i] 
    K %= unit_list[i] #거스름돈
    i += 1
print(ans)

    
    
