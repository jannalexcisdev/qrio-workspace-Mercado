"""class Car:
    def __init__ (self, model, year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive (self):
        print(f"You drive the {self.model}")

    def stop (self):
        print(f"You Stop the {self.model}")


car = Car("Maserati", 2024,"Red", True)
car.drive()
print(car.color)"""




                                    #CLASS VARIABLES
'''
class Student:
    
    class_year = 2024
    num_of_students = 0

    def __init__(self,name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1


student1 = Student("Spongebob", 13)
student2 = Student("Partick", 17)
student3 = Student("Squidward", 21)
student4 = Student("Sandy", 14)


print(f"The graduation date of {student1.name} is {student1.class_year}")
print(f"The graduation date of {student2.name} is {Student.class_year}") #<- better practice
print(Student.num_of_students)

print (f"Graduating class: {Student.class_year}. Total stud ents: {Student.num_of_students}.")
print (f"{student1.name}, {student2.name}, {student3.name}, {student4.name}")
'''


                                        #INHERITANCE
"""                                 
class Animal:
    def __init__(self, name, is_alive):
        self.name = name
        self.is_alive = is_alive    #<- di pala required na nasa parameter yung variable

        if self.is_alive == True:
            self.is_alive = "Alive and Kicking"
        elif self.is_alive == False:
            self.is_alive = "Dead"
        else:
            print("Invalid Input")


    def eat(self):
        print(f"{self.name} is Eating")
    
    def sleep(self):
        print(f"{self.name} is Sleeping")

class Dog(Animal):
    def speak (self):
        print("WOOF!")

class Fox(Animal):
    def speak (self):
        print("SCREAM!!")


dog = Dog("douglas",True)
dog.eat()
print(f"\n{dog.name} is {dog.is_alive}")
dog.speak()

fox = Fox("jobert", True)
fox.sleep()
"""



                                #MULTIPLE INHERITANCE
"""
class Animal:
    pass

class Predator(Animal):
    def hunt (self):
        print (f"This {self.name} hunts")

class Prey(Animal):
    def flee (self):
        print ("This animal flees")

class Dog (Predator):
    def __init__(self,name):
        self.name = name


class Cat (Prey):
    pass


dog = Dog("douglas")
dog.hunt() """


#ABSTRACT
'''
from abc import ABC, abstractmethod

class Vehecle (ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop (self):
        pass

class Car(Vehecle):
    def start(self):
        print("Car Starts")

    def stop(self):
        print("Car Stops")


car = Car()
car.start()
'''









#SUPER
'''
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and is {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self,color,is_filled, radius):
        self.radius = radius
        super().__init__(color, is_filled)

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def area(self):
        print(f"The area of square is {self.width*self.width}")
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def area(self):
        print(f"The area of triangle is {(self.width * self.height)/2}")

square = Square(color="Red",is_filled=True,width=10)
square.area()
square.describe()

triangle = Triangle(color="Yellow",is_filled=False,width=10,height=10)
triangle.area()
triangle.describe()

'''






#POLYMORPHISM with abstract
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius,name):
        self.radius = radius
        self.name = name
    
    def area(self):
        return 3.14 * self.radius ** 2

class Pizza(Circle):
    def __init__(self, toppings,radius, name):
        super().__init__(radius, name)
        self.toppings = toppings


shapes = [Circle(10,"circle"), Pizza("Pepperoni", 12, "pizza")]

for shape in shapes:
    print(f"The area of {shape.name} is {shape.area()}cm^2")





#DUCK TYPING
#if it looks like a duck, quacks like a duck, it must be a duck.

class Animal:
    is_alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car:

    is_alive = False
    def speak(self):
        print("BEEP")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.is_alive)