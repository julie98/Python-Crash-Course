# import car_profile

# car = car_profile.make_car('sabaru', 'outback', tow_package = True, car_year = 5)
# print(car)

 
# from car_profile import make_car

# car = make_car('sabaru', 'outback', tow_package = True, car_year = 5)
# print(car)


# from car_profile import make_car as mc 

# car = mc('sabaru', 'outback', tow_package = True, car_year = 5)
# print(car)


# import car_profile as cp 

# car = cp.make_car('sabaru', 'outback', tow_package = True, car_year = 5)
# print(car)


from car_profile import *
car = make_car('sabaru', 'outback', tow_package = True, car_year = 5)
print(car)
