class Yogurt:
    def __init__(self, topping = None):
        self.topping = topping

    def show_my_eat(self):
        if self.topping is not None:
            print(f"Your yogurt contains {self.topping} topping!")
        elif self.topping is None:
            print(f"Tasteless yogurt.")


your_food = Yogurt("chocolate")
your_food.show_my_eat()
your_food2 = Yogurt()
your_food2.show_my_eat()
