import random as ran
ans = ran.randint(1,5)
guess = int(input("請輸入1~5當中的一個數字"))
if guess == ans:
    print("猜對了")
else:
    print("猜錯了 答案是:",ans)
