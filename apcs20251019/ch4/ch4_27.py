list1 = [1,2,3,5,8,13,21,34,55,89]
print(list1)
result = []
for i in list1:
    if i % 2 == 0:
        result.append(i)
print(result)        

fboj = filter(lambda x : x % 2 == 0,list1)
print(list(fboj))
