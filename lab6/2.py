word=input()

upper=0
lower=0

for i in word:
    
    if i.isupper():
        upper+=1
        
    if i.islower():
        lower+=1
        

print(upper)
print(lower)
