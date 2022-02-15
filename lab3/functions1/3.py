def solve(numheads,numlegs):
    chicken=0
    rabbit=0
    
    if(numheads>=numlegs):
        print("It is wrong")
    elif(numlegs%2!=0):
        print("It is wrong")
    else:
        rabbit=(numlegs-2*numheads)/2
        chicken=numheads-rabbit
        print(int(chicken),int(rabbit))
        
solve(35,94)
