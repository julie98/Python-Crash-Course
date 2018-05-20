# print(list(range(1,21)))

numbers = list(range(1,1000001))
# for number in numbers:
# print(number)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

print("The first three items in the list are:")
for number in numbers[:3]:
	print(number)

print("\nThree items from the middle of the list are:")
for number in numbers[100:103]:
	print(number)

print("\nThe last three items in the list are:")
for number in numbers[-3:]:
	print(number)

