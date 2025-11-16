def func(theList):
    print("Func()1 list:",theList)
    theList[2] = "Hi"
    print("Func()2 list:",theList)
myList = [10,20,30]
print("全域1:",myList)
func(myList)
print("全域2:",myList)



