"""Выводит наибольшее число или сообщение о равенстве."""
while True:
	try:
		a = int(input("Please enter 1st number: "))
		b = int(input("Please enter 2nd number: "))
		if a > b:
			print(f"{a} is greater number then {b}!")
			break
		elif b > a:
			print(f"{b} is greater number then {a}!")
			break
		else:
			print("Given numbers are equal!")
			break
	except ValueError:
		print("Operate numbers only!")
		continue
