import math

def volume_sphr(radius):
    
    return 4/3*float(math.pi)*pow(radius,3)


r=int(input())
      
print(volume_sphr(r))
