str=input()
data_stack=list() 
sum=0
i=0
while i<len(str) :
    if str[i:i+2]=='()':
        sum+=len(data_stack)
        i+=2
    elif str[i]=='(':
        data_stack.append('(')
        i+=1
    elif str[i]==')':
        data_stack.pop()
        sum+=1
        i+=1
    else:
        print('잘못된 입력입니다.')
        break
print(sum)

'''
#위와 같은 코드이지만 각 단계마다 결과가 출력되게 한 것! 발표 용도!

str=input()
data_stack=list() #리스트를 스택처럼 사용할 것
sum=0
i=0
while i<len(str) :
    if str[i:i+2]=='()':
        sum+=len(data_stack)
        print("현재 스택: {0}, 현재 i: {1}, 현재 sum: {2}".format(data_stack, i, sum))
        i+=2
    elif str[i]=='(':
        data_stack.append('(')
        print("현재 스택: {0}, 현재 i: {1}, 현재 sum: {2}".format(data_stack, i, sum))
        i+=1
    elif str[i]==')':
        data_stack.pop()
        sum+=1
        print("현재 스택: {0}, 현재 i: {1}, 현재 sum: {2}".format(data_stack, i, sum))
        i+=1
    else:
        print('잘못된 입력입니다.')
        break
print(sum)
'''
