def toString(List): 
    return ''.join(List) 

def permutation(a, l, r): 
    if l==r:  
        print (toString(a))
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            
            permutation(a, l+1, r) 
            a[l], a[i] = a[i], a[l]
    
            
s=input()
n=len(s)
a=list(s)

print(permutation(a,0,n-1))
