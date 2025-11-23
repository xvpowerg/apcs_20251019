class Point:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):#物件要轉換成甚麼格式的字串
        return f"({self.x},{self.y})"
    def __len__(self):
        return self.x ** 2 + self.y ** 2
    def __lt__(self,other):
        return len(self) < len(other)
p1 = Point(9,1)
p2 = Point(-2,-3)
p3 = Point(5,7)
p4 = Point(2,4)
myList = [p1,p2,p3,p4]
print(len(p1))
print(p1 > p2)
myList.sort()
for p in myList:
    print(p)
