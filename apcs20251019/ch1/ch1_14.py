#請設計一個 BMI 計算題目
#公式為「體重 ( 公斤 ) 除以身高 ( 公尺 ) 的平方」。
#顯示BMI數值
##請輸入身高 輸入體重
height = float(input("身高:"))
weight = int(input("體重:"))
bmi = weight / (height/100) ** 2
print("bmi:",f"{bmi:.2f}")
