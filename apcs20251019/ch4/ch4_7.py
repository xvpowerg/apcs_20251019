def test2(a):
    an1 = a * 2
    an2 = a ** 2
    an3 = a + 2
    an4 = a ** 3
    an5 = a * 6
    return an1,an2,an3,an4,an5
v1,v2,v3,v4,v5 =  test2(5)
print(v1,v2,v3,v4,v5)

v1,v2,*_ =  test2(5)#*_ 表示其他沒接收到的所有資料我來收
print(v1,v2)
