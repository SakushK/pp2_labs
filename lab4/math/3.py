from math import tan, pi

def area_polygon(number_of_sides, length):
    
   area = number_of_sides * (length ** 2) / (4 * tan(pi / number_of_sides)) #formula of area of regular polygon

   print("The area of the polygon is:",area)
   
n=int(input("Input number of sides:"))
l=int(input("Input the length of a side:"))

area_polygon(n,l)
