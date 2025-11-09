def func1(x):
    return x * 5
#map用來做轉換
list1 = [5,6,7,8]
mapObj = map(lambda x:x ** 2,list1)
print(list(mapObj))

mapObj2 = map(func1,list1)
print(list(mapObj2))
