"""Программа позволяет проверить какие рыбы в аквариуме,
покормить рыб в выбранном аквариуме, пересадить рыбу из
одного аквариума в другой."""
aquarium_1 = ['caribbian reef shark', 'galapalos shark', 'blue shark', 
'bull shark']
aquarium_2 = ['white shark', 'smooth hammerhead', 'lemon shark',
'whale shark']
feed_counter_a1 = 0
feed_counter_a2 = 0
import random

def see_fish(aquarium):
	"""Функция получает список обитателей аквариума и форматирует список."""
	print("\nChosen aquarium has following species: ")
	for fish in aquarium:
		print(f"\t{fish.title()}")

def move(fish):
	"""Переносит указанную рыбу из одного аквариума в другой."""
	if fish in aquarium_1:
		aquarium_1.remove(fish)
		aquarium_2.append(fish)
		print(f"\t{fish.title()} was moved to other aquarium №2!")
	elif fish in aquarium_2:
		aquarium_2.remove(fish)
		aquarium_1.append(fish)
		print(f"\t{fish.title()} was moved to other aquarium №1!")
	else:
		print("You don't have this type of fish!")

def feed(aquarium):
	"""Кормит рыбу. Покорми трижды, чтобы убить рыбу."""
	global feed_counter_a1
	global feed_counter_a2
	if aquarium == aquarium_1:
		feed_counter_a1 += 1
		if feed_counter_a1 < 3:
			print(f"You've fed your fish! Everything is fine!")
		elif feed_counter_a1 == 3:
			print(f"\nNice! You've overfed your fish!")
			chosen_aquarium = aquarium
			dead_fish = random.choice(chosen_aquarium)
			chosen_aquarium.remove(dead_fish)
			print(f"\t{dead_fish.title()} is now dead!")
			feed_counter_a1 = 0
	elif aquarium == aquarium_2:
		feed_counter_a2 += 1
		if feed_counter_a2 <3:
			print(f"You've fed your fish! Everything is fine!")
		elif feed_counter_a2 == 3:
			print(f"\nNice! You've overfed your fish!")
			chosen_aquarium = aquarium
			dead_fish = random.choice(chosen_aquarium)
			chosen_aquarium.remove(dead_fish)
			print(f"\t{dead_fish.title()} is now dead!")
			feed_counter_a2 = 0

"""Тушка программы."""
commands_6 = ["'q' to exit", "'f1' to feed fish in the first aquarium", 
"'f2' to feed fish in the first aquarium", 
"'sf1' to see fish in the first aquarium",
"'sf2' to see fish in the first aquarium",
"'move' to place fish in other aquarium"]
print("\tOur programm supports following commands: ")
for command in commands_6:
	print(f"\t-{command};")
user_command = input("Please type your command to interact with programm: ")
while user_command != 'q':
	if user_command == 'sf1':
		see_fish(aquarium_1)
		user_command = input("\nWhat else? ")
	elif user_command == 'sf2':
		see_fish(aquarium_2)
		user_command = input("\nWhat else? ")
	elif user_command == 'f1':
		feed(aquarium_1)
		user_command = input("\nWhat else? ")
	elif user_command == 'f2':
		feed(aquarium_2)
		user_command = input("\nWhat else? ")
	elif user_command == 'move':
		moving_chosen_fish = input("\nPlease type name of the fish: ")
		move(moving_chosen_fish.lower())
		user_command = input("\nWhat else? ")
	elif user_command == 'q':
		break
	else:
		user_command = input("\nProgram doesn't understand you! Pls repeat"
			"your command! ")