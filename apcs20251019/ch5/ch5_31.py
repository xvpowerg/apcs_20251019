try:
    for i in range(1,4):
        print("i Start:",i)

        for k in range(1,4):
            print("k",k,end=" ")
            if i == 2:
                raise Exception#跳離所有迴圈
            
        print()    
        print("i End:",i)
        print("="*50)
except:    
    pass
