number = input("Please enter a number! ")
number = int(number)

if number % 10 == 0:
	print(str(number) + " is a multiple of ten.")
else:
	print(str(number) + " is not a multiple of ten.")