"""Заменяет каждую четную букву в слове на заглавную."""
your_message = input("Please write your word: ")
formatted_message = ''
for letter, formatted_letter in enumerate(your_message):
	if letter % 2:
		formatted_message += formatted_letter.upper()
	else:
		formatted_message += formatted_letter
print(f"{formatted_message}!")