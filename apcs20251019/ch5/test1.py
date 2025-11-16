myList = [5,6,8,9]
print(myList)
def test(v):
    return v + 2
mapObj = map(test,myList)
print(list(mapObj))
