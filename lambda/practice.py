# syntax (lambda params: expression)
add_nums = lambda a, b: a + b
print(add_nums(2,2))

# self invoked lambda expression provides arguments themselvess
subtract_nums = (lambda a,b: a-b) (2,2)
print(subtract_nums)

#multiple expressions (add, multiply and divide)
multiply = (lambda a,b: a + b ** 2 / 2) (2,2)
print(multiply)

#lambda in function self invoked
def add (x):
    return (lambda a: x + a )(2)
print(add(2))