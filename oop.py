
class Human():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name 
        self.last_name = last_name 
        self.age = age 

    def get_fullname(self):
        return self.first_name + " " + self.last_name
    
    def set_names(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self):
        return f"{self.first_name} {self.last_name} {self.age}"

fada = Human(
    first_name="Fada",
    last_name="Paul",
    age=65
)
michael = Human(
    first_name="Michael",
    last_name="Appiah",
    age=120
)
print(type(fada))
print(type({"name":"Fada"}))
print(michael.get_info())
print(fada.get_info())