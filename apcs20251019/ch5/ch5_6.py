myList = ["Ken","Vivin","Lucy","Joy"]
#根據myList幫我產生一個字串 Ken,Vivin,Lucy,Joy
'''
result = ""
for name in myList:
    result += name+","

print(result[:-1])
'''

result2 = ""
dataLen = len(myList)
print(dataLen)
for i in range(dataLen):
    result2 += myList[i]
    if i != dataLen - 1:
        result2 += ","
print(result2)
