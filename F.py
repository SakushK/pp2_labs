n = int(input())
a=[]

for i in range(0,n):
    
    d=int(input())
    a.append(d)
    
for i in range(0,n):
    
    if (a[i]<=10):
        print("Go to work!")
        
    elif (a[i]>10 and a[i]<=25):
        print("You are weak")
        
    elif (a[i]>25 and a[i]<=45):
        print("Okay, fine")
        
    else: 
        print("Burn! Burn! Burn Young!")