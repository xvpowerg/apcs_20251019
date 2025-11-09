def func1(*v1,call):
    result = []
    for v in v1:
        result.append(call(v))
    return  result

def myCall(x):
    return x * 3
def myCall2(x):
    return x ** 3

print(func1(2,3,4,5,call=myCall))
print(func1(2,3,4,5,call=myCall2))
print(func1(2,3,4,5,call=lambda x : x + 6))
