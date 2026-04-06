numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]


a = [1, 2, 3]
b = [4, 5, 6]
sum_list = list(map(lambda x, y: x + y, a, b))
print(sum_list)  # [5, 7, 9]



students = [("Ali", 18), ("Dana", 17), ("Zara", 19)]
students.sort(key=lambda x: x[1])  # sort by age
print(students)  # [('Dana', 17), ('Ali', 18), ('Zara', 19)]



names = ["Ali", "Dana", "Zara", "Omar"]
long_names = list(filter(lambda x: len(x) > 3, names))
print(long_names)  # ['Dana', 'Zara']