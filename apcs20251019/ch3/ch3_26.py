myMax = 60
num1,num2 = 1,1
print(num1,num2,sep=", ",end="")
nextNum = num1 + num2
while nextNum < myMax:
    print(f", {nextNum}",end="")
    num1 = num2
    num2 = nextNum
    nextNum =  num1 + num2
    
