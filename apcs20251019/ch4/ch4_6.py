def test1(a):
    an1 = a * 2
    an2 = a ** 2
    an3 = a + 2
    return an1,an2,an3

v1,v2,v3 =  test1(5)
print(v1,v2,v3)
print(test1(5))
#v1,v2 =  test1(6)
#print(v1,v2)
tp1 = ("A","B","C")
x1,x2,x3 = tp1
print(x1,x2,x3)
x1,x2,_ = tp1
print(x1,x2)

