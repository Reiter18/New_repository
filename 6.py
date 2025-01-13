class Vehicle:
    def __init__(self, make, model):
        self.make = make  # Марка
        self.model = model  # Модель

    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)  # Инициализация атрибутов базового класса
        self.fuel_type = fuel_type  # Тип топлива

    def get_info(self):
        base_info = super().get_info()  # Получение информации из базового класса
        return f"{base_info}, Тип топлива: {self.fuel_type}"

    # Пример использования классов
vehicle = Vehicle("Toyota", "Corolla")
print(vehicle.get_info())  # Ожидается: Марка: Toyota, Модель: Corolla
car = Car("Honda", "Civic", "Бензин")
print(car.get_info())  # Ожидается: Марка: Honda, Модель: Civic, Тип топлива: Бензин

'''class UserAccount:    
    def __init__(self, username, email, password):        
        self.username = username        self.email = email        
        self.password = password  # Приватный атрибут   
         
    def set_password(self, new_password):       
    # Здесь можно добавить логику для проверки сложности пароля        
    self.password = new_password   
     
    def check_password(self, password):
        return self.password == password
        
#Пример использования класса UserAccount
            
    # Создание объекта класса UserAccount
user = UserAccount("Daniil", "danila@example.com", "123")    
    # Изменение пароля
user.set_password("456")
    # Проверка пароля
print(user.check_password("wrongPassword"))  # Ожидается False
print(user.check_password("456"))  # Ожидается True'''

