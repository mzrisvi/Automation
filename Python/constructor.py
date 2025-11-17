# This is for Constructor Demonstration
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id
        
# Example usage
if __name__ == "__main__":
    person = Person(first_name="John", last_name="Doe")
    print(f"Full Name: {person.full_name()}")
    
    employee = Employee(first_name="Jane", last_name="Smith", employee_id="E123")
    print(f"Employee Full Name: {employee.full_name()}, ID: {employee.employee_id}")
    
