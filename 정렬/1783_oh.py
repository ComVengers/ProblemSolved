import sys
n,m = map(int, input().split())

if n == 1:
    result = 1

## 두가지로 표현가능. 람다식, min
elif n == 2:
    result = lambda x : 4 if ((m-1)//2+1) >= 4 else ((m-1)//2+1)
elif m <= 6:
    result = min(4,x)
else:
    result = m-2

print(result)
