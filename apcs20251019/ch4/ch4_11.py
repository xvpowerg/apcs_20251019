def weight_sum(c,e=80,m=60):
    return c + e*2 + m*3

x = weight_sum(100)
print(x)
y = weight_sum(100,20)
print(y)
z = weight_sum(100,20,10)
print(z)

v1 = weight_sum(100,m=10)#命名參數
print(v1)
v2 = weight_sum(100,m=10,e=30)
print(v2)
v3 = weight_sum(m=10,c=20,e=15)#只要使用命名參數 接下來的參數都必須是命名參數
print(v3)
