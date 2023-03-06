class SomeCar:
    def __init__(self, model = "no info", year = "no info", maker = "no info", volume = "no info",
                 color = "no info", price = "no info"):
        self.model = model
        self.year = year
        self.maker = maker
        self.volume = volume
        self.color = color
        self.price = price

    def auto_info(self):
        """Вывод полной информации об автомобиле."""
        print(f"Car's model: {self.model},\nManufactured in: {self.year},\nManufactured by: {self.maker},\n"
              f"Engine's volume: {self.volume}L,\nCar's color: {self.color},\nCar's price: {self.price}$.")

    def update_model(self, new_model):
        print(f"\nModel updated, current model - {new_model}!")
        self.model = new_model

    def update_year(self, new_year):
        print(f"\nYear updated, current year - {new_year}!")
        self.year = new_year

    def update_maker(self, new_maker):
        print(f"\nMaker updated, current maker - {new_maker}!")
        self.maker = new_maker

    def update_volume(self, new_volume):
        print(f"\nVolume updated, current volume - {new_volume}L!")
        self.volume = new_volume

    def update_color(self, new_color):
        print(f"\nColor updated, current color - {new_color}")
        self.color = new_color

    def update_price(self, new_price):
        print(f"\nPrice updated, current price - {new_price}$")
        self.color = new_price

    def all_info_keyboard(self):
        """Обновляем данные через input."""
        new_model = input("Enter vehicle model: ")
        self.update_model(new_model)
        new_year = input("Enter manufacture year: ")
        self.update_year(new_year)
        new_maker = input("Enter vehicle maker: ")
        self.update_maker(new_maker)
        new_volume = input("Enter engine volume: ")
        self.update_volume(new_volume)
        new_color = input("Enter vehicle color: ")
        self.update_color(new_color)
        new_price = input("Enter price: ")
        self.update_price(new_price)

    def __str__(self):
        """Перегруженный str."""
        return f"\n{self.model}: {self.year}, {self.maker}, {self.volume}L, {self.color}, {self.price}$."


car = SomeCar("Gachi M3", "2023", "Gachimuchi-automobili", "6.0", "Black", "300.000")
car.auto_info()
car.update_price("300.069")
print(car.__str__())
