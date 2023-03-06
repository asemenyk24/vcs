import json


class BookOfTheDead:
    def __init__(self, name = "no info", year = "no info", publisher = "no info", genre = "no info",
                 author = "no info", price = "no info"):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def show_info(self):
        """Вывод полной информации о книге."""
        print(f"The book {self.name} was first printed in {self.year} by {self.publisher}. It's written in"
              f" {self.genre} genre by {self.author} and you can buy it for at least {self.price}$!")

    def update_name(self, new_name):
        print(f"\nName of the book updated! Current name is {new_name}!")
        self.name = new_name

    def update_year(self, new_year):
        print(f"\nYear of the book updated! Current year is {new_year}!")
        self.year = new_year

    def update_publisher(self, new_publisher):
        print(f"\nPublisher of the book updated! Current publisher is {new_publisher}!")
        self.publisher = new_publisher

    def update_genre(self, new_genre):
        print(f"\nGenre of the book updated! Current genre is {new_genre}!")
        self.genre = new_genre

    def update_author(self, new_author):
        print(f"\nAuthor of the book updated! Current author is {new_author}!")
        self.author = new_author

    def update_price(self, new_price):
        print(f"\nPrice of the book updated! Current price is {new_price}$!")
        self.price = new_price

    def update_data_by_keyboard(self):
        """Обновление данных через input."""
        new_name = input("Enter new name of the book: ")
        self.update_name(new_name)
        new_year = input("Enter year of publish: ")
        self.update_year(new_year)
        new_publisher = input("Enter new publisher: ")
        self.publisher = new_publisher
        new_genre = input("Enter genre: ")
        self.genre = new_genre
        new_author = input("Enter author of the book: ")
        self.author = new_author
        new_price = input("Enter new price: ")
        self.price = new_price

    def __str__(self):
        """Перегруженный str."""
        return f"\n{self.name}: {self.year}, {self.publisher}, {self.genre}L, {self.author}, {self.price}$."

    def pack_data(self):
        """Пакую все в словарик."""
        dictionary = {}
        for key in self.__dict__:
            dictionary[key.replace(f"{self.__class__.__name__}", "")] = self.__dict__[key]
        return dictionary

    def save_to_json(self):
        """Читатор/загружатор .json!"""
        try:
            with open("book_info.json") as f:
                book_data = json.load(f)
                self.name = book_data['name']
                self.year = book_data['year']
                self.publisher = book_data['publisher']
                self.genre = book_data['genre']
                self.author = book_data['author']
                self.price = book_data['price']
            return self
        except FileNotFoundError:
            print("We don't have any data recorded, let me correct that!")
            book_data = self.pack_data()
            with open("book_info.json", "w") as f:
                json.dump(book_data, f)


best_book = BookOfTheDead("Gachi-bible", "2300", "Dungeon", "Deep dark fantasy", "Van Darkholme", "300")
best_book.show_info()
best_book.update_year("2077")
print(best_book.__str__())
best_book.save_to_json()
