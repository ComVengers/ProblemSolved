N = int(input())
i = 1
num = 666
while True: #1이면 666, 2이면 1666..., 6이면 5666, 7이면 6660
    if '666' in str(num):
        if i == N:
            break
        i += 1
    num += 1
print(num)