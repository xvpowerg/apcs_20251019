def func1(*v1):
    result = []
    for v in v1:
        result.append(v**2)
    return  result

print(func1(2,3,4,5))
