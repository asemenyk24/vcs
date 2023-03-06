"""Выводит наибольшее число или сообщение о равенстве."""
a = input("Please enter 1st number: ")
b = input("Please enter 2nd number: ")
while True:
	if a > b:
		print(f"{a} is greater number then {b}!")
		break
	elif b > a:
		print(f"{b} is greater number then {a}!")
		break
	else:
		print("Given numbers are equal!")
		break