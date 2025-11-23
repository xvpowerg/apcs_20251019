class Point:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):#物件要轉換成甚麼格式的字串
        return f"({self.x},{self.y})"
p1 = Point(2,3)
p2 = Point(-1,2)
st1 = str(p1)
print(st1)

print(p1)
print(p2)
