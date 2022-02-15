#calculate and display the equivalent centigrade temperature
#C = (5 / 9) * (F – 32)

def to_celsius(f):
    a=f-32
    c=(5/9)*a
    
    return c

t=int(input())

print(to_celsius(t))
