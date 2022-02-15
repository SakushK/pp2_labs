
#create a function to convert grams to ounces. 
#ounces = 28.3495231 * grams
    
def how_many(g):
    
    ounce=float(28.3495231 * g)
    
    return ounce

mass=int(input())

print(how_many(mass))
