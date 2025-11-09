def testFunc1(*v1,v2=0,v3=0):
    print(v1,v2,v3)
    
testFunc1(1,2,3,4,5,v2=12,v3=75)
