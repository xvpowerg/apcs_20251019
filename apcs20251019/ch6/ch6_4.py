class Student:
    def __init__(self,name,score=0):
        self.name = name
        self.score = score
    def printInfo(self):
        print(self.name,self.score)
st1 = Student("Ken",85)
st2 = Student("Joy",72)
#print(st1.name,st1.score)
#print(st2.name,st2.score)
st1.printInfo()
st2.printInfo()
