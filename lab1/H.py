s=input()
d=input()
result=""

first=s.find(d)

if(not(first==-1)):
    result+=str(first)
    
    last=s.rfind(d)
    if(last==first):
        print(result)
        quit()
    
        
        
    else:
        result+=" "
        result+=str(last)
        
        if len(result)!=0:
            print(result)
