def swap(a,b):
    print("函數內1:",a,b)
    a,b = b,a
    print("函數內2:",a,b)
    
a,b = 5,99
print("函數外1:",a,b)
swap(a,b)
print("函數外2:",a,b)
