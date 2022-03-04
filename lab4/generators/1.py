def squares(n):
    for i in range(n):
        yield i ** 2
        
n=int(input())

for i in squares(n):
    
    print(i)
