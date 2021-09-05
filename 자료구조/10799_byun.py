a = input()
arange = list(a)

stick = 0
total = 0


for i in range(len(arange)):
   
    if arange[i]=='(':
        stick+=1
       
    else :
        if arange[i-1]=='(' :
            stick-=1
            total+=stick
    
        else : 
            stick-=1
            total+=1
                      
print(total)