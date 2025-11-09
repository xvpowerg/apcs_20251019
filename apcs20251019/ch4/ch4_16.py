def scoreSum(*score,name):
    total = 0
    for s in score:
        total += s
    print(name,":",total)
    
scoreSum(100,75,46,83,name="Kne")
scoreSum(75,65,name="Joy")
