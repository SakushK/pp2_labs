def Isprime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    
    return True

n,f=map(int,input().split())

if Isprime(n)==True and n<500 and f%2==0:
    print("Good job!")
    
else:
    print("Try next time!")
