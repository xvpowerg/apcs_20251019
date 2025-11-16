num1 = 10
num2 = 2
myList = ["A","B","C"]
print("Start")
try:
    print(num1 / num2)
    print(myList[99])
except ZeroDivisionError:    
    print("分母不可為零")
except:
    print("有錯誤")
print("End")
