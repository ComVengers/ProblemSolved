a = input("쇠막대기와 레이저의 배치를 입력하세요")
arange = list(a)

stick = 0
total = 0


for i in range(len(arange)):
   
    if arange[i]=='(':
        stick+=1
        stack.append('(')
    
    else :
        if arange[i-1]=='(' :
            stick-=1
            total+=stick
    
        else : 
            stick-=1
            total+=1
                      
print(total)