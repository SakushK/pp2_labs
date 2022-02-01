num=int(input())
s=input()

if(s=="b"):
    
    print(num*1024)
    quit()
    
c=int(input())

if (s=="k"):
        
        kilo=float(num/1024)
        
        print(round(kilo,c))