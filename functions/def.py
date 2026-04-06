def show_info(name, age):
    print(name, age)

show_info("Dana", 18)


def add(a, b):   # parameters
    print(a + b)

add(2, 3)        # arguments


def find_square(n):
    square = n * n
    print(square)

find_square(6)

def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

sum1 = my_sum(1, 2, 3, 4, 5)
sum2 = my_sum(1, 2, 3)
print(sum1)  # 15
print(sum2)  # 6


def func(**kwargs):
    print(kwargs)  # kwargs is a dict
    for key in kwargs:
        print(key, kwargs[key])

func(fname = "Adilkhan", lname = "Kumar")