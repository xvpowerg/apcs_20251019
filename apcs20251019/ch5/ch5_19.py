cars = ['Honda','Toyota','Ford','Toyota','BMW','Toyota']
#完成一個迴圈移除所有Toyota
#cars.remove('Toyota')
print(cars)
#print('Toyota' in cars)
remove="Toyota"
while remove in cars:
    cars.remove(remove)
print(cars)    
