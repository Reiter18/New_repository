# Определение класса Employee
class Employee:
    def init__(self, name, employee_id):
        self.name = name
        self.id = employee_id

    def get_info(self):
        return f"Employee Name: {self.name}, ID: {self.id}"

# Определение класса Manager, наследующего от Employee
class Manager(Employee):
    def init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def manage_project(self, project_name):
        return f"{self.name} is managing the project: {project_name}"

# Определение класса Technician, наследующего от Employee
class Technician(Employee):
    def init__(self, name, employee_id, specialization):
        super().__init__(name, employee_id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} is performing maintenance as a {self.specialization}"

# Определение класса TechManager, наследующего от Manager и Technician
class TechManager(Manager, Technician):
    def init__(self, name, employee_id, department, specialization):
        Manager.__init__(self, name, employee_id, department)
        Technician.__init__(self, name, employee_id, specialization)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        team_info = [employee.get_info() for employee in self.team]
        return "n".join(team_info)

# Создание объектов каждого класса
employee1 = Employee("Alice", 1)
manager1 = Manager("Bob", 2, "IT")
technician1 = Technician("Charlie", 3, "Networking")
tech_manager1 = TechManager("Dave", 4, "Development", "Software")

# Добавление сотрудников в команду TechManager
tech_manager1.add_employee(employee1)
tech_manager1.add_employee(manager1)
tech_manager1.add_employee(technician1)

# Демонстрация функциональности
print(employee1.get_info())
print(manager1.manage_project("Website Upgrade"))
print(technician1.perform_maintenance())
print(tech_manager1.get_team_info())