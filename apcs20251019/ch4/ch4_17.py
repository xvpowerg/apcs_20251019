def personInfo(name,age,**other):
    print(name)
    print(age)
    for key in other:
        print(key,":",other[key])


personInfo("Sean",40)
personInfo("Joy",35,phone="0977556188",company="Google")        
personInfo("Amy",25,email="amy@gmal.com",company="IBM")  
