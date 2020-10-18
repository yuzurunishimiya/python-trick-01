# basic syntax
# [ expression for item in list if conditional ]
# example

mylist = [i for i in range(10)]
print(mylist)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# squares even only
squares = [i**2 for i in range(10) if i % 2 == 0 ]
print(squares)

# Or even call an external function
def some_function(arg):
    return (arg + 5) / 2

my_formula = [some_function(i) for i in range(10)]
print(my_formula)

# Conditional odd only
conditionalList = [i for i in mylist if i % 2 != 0]
print(conditionalList)
