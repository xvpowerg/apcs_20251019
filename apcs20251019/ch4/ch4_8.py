def get_sum(a,b):
    return a + b
def get_sum(a,b,c): #覆蓋了get_sum(a,b)
    return a + b + c
print(get_sum(2,5))#會錯
