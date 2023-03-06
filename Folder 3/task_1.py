class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def show_info(self):
        print(f"Stadium called {self.name} is located in {self.country} in city {self.city}.\nFirst it was "
              f"opened {self.opening_date} and it has capacity of {self.capacity} seats.")

    def update_name(self, new_name):
        self.name = new_name
        print(f"Name have been changed to {new_name}!")

    def update_opening_date(self, new_date):
        self.opening_date = new_date
        print(f"Name have been changed to {new_date}!")

    def update_country(self, new_country):
        self.country = new_country
        print(f"Name have been changed to {new_country}!")

    def update_city(self, new_city):
        self.city = new_city
        print(f"Name have been changed to {new_city}!")

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity
        print(f"Name have been changed to {new_capacity}!")


stadium = Stadium("Dungeon", "27.02.2023", "Russia", "Krasnoyarsk", "300")
stadium.show_info()
stadium.update_name("Gym")
stadium.show_info()
