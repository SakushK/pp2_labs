n = int(input()) 
a = list(str()) 
ans = set() 
 
for i in range(n): 
    a.append(input()) 
 
for i in range(len(a)): 
    if a[i].isalpha(): 
        continue 
    elif a[i].isdigit(): 
        continue 
    elif a[i].isupper(): 
        continue 
    elif a[i].islower(): 
        continue 
    else: 
        ans.add(a[i]) 
 
 
print(len(ans)) 
 
ans = list(ans) 
ans.sort() 
for i in range(len(ans)): 
    print(ans[i])
