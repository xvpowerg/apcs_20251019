list1 = ["10","20","30","40"]
total = 0
for v in list1:
    total += int(v) 
print("total:",total)
total = 0
intList = list(map(int,list1))
for v in intList:
    total += v
print(total)    
