height = float(input('請輸入身高，單位為公分: '))
weight = int(input('請輸入體重，單位為公斤: '))
bmi = weight/((height/100)**2)
print("bmi: %.2f, 判定結果: " %(bmi), end='')

if 0 < bmi  <= 18.5:
    print("過輕")
elif 18.5 < bmi <= 25:
    print("正常")
elif 25 < bmi <= 30:
    print("過重")
elif  30 < bmi:
    print("胖胖")
else:
    print("錯誤")
    
    
