def calcBMI(h,w):
    pass
def diagnose(bmi):
    pass    
height = float(input('請輸入身高，單位為公分: '))
weight = int(input('請輸入體重，單位為公斤: '))
bmi = calcBMI(height, weight)

print(f"{bmi:.2f}",":",diagnose(bmi))
