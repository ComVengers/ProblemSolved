n = int(input())
i = 0
num = 666
while True:
    if '666' in str(num):
        i += 1
    if i == n:
        print(num)
        break
    num += 1
