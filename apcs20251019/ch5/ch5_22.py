cars = ['honda','BMW','Toyota','audi']
print(cars)
cars.sort()
print(cars)
cars.sort(key=len)
print(cars)
cars.sort(key=lambda v : v.upper())
print(cars)


