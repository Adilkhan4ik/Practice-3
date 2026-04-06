class Dog:
    type = "Animal"

    def show(self):
        print(self.type)

d = Dog()
d.show()


class Car:
    wheels = 4

    def info(self):
        print("Wheels:", self.wheels)

c = Car()
c.info()


class Student:
    school = "High School"

    def show_school(self):
        print(self.school)

s = Student()
s.show_school()


class Phone:
    brand = "Samsung"

    def show_brand(self):
        print(self.brand)

p = Phone()
p.show_brand()


class Book:
    category = "Education"

    def show_category(self):
        print(self.category)

b = Book()
b.show_category()