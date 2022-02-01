
str1 = input()
li=[] 
li[:0]=str1 
result=[]

for i in range(len(li)):
    result.append(ord(li[i]))
    result = list(set(result))
      
final=sum(result)

if final>300 :
    print("It is tasty!")
    
else: 
    print("Oh, no!")
     
     
     
     
    
    
