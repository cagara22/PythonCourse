class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, item):
        match item:
            case "title":
                return self.title
            case "author":
                return self.author
            case "num_pages":
                return self.num_pages
            case _:
                return None


book1 = Book("The Bitch", "Dickhead", 420)
book2 = Book("The Asshole", "Jerk", 69)
book3 = Book("The Jackass", "Donkey", 153)
book4 = Book("The Jackass", "Donkey", 153)

print(book1)
print(book2)
print(book3)

print(book3 == book4)
print(book1 < book2)
print(book1 > book2)
print(book1 + book2)
print("Bitch" in book1)
print(book1["title"])

