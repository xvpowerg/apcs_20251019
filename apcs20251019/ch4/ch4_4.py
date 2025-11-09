def testAge(age):
    if age < 0 or age >= 200:
        print("錯誤的年齡")
        return#離開函式
    
    if age >= 18:
        print("成年")
    else:
        print("未成年")
def testX():
    print("x")

v1 = testAge(200)
testAge(18)
print(v1)
v2 = testX() 
print(v2)
