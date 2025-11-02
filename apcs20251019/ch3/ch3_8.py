#請寫一個程式，判斷輸入的整數為否為2或3的倍數
num = int(input("請輸入整數"))
if num % 2 == 0 and num % 3 == 0:
    print(f"{num}是2與3的倍數")
elif num % 2 == 0:
    print(f"{num}是2的倍數")
elif num % 3 == 0:
    print(f"{num}是3的倍數")
else:
    print(f"{num}不是2與3的倍數")
