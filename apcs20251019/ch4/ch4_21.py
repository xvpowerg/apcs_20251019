def func():
    global a#宣告一個a 這個a是全域的
    a += 10
    print(a)
    
a = 5
print("a1:",a)
func()
print("a2:",a)
