class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


circle = Circle(5)  # Инициализация радиуса 5
print("Исходный радиус:", circle.get_radius())

circle.set_radius(10) # Инициализация нового радиуса 10
print("Новый радиус:", circle.get_radius())


'''class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def get_info(self):
        return f'название книги: {self.title}, автор: {self.author}, год издания {self.year}'''
