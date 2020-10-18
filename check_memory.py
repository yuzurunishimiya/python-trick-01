# Check memory with sys.getsizeof()

import sys

mylist = range(0, 10000)
print(sys.getsizeof(mylist))

# Woah… wait… why is this huge list only 48 bytes?
# It’s because the range function returns a class that only behaves like a list. A range is a lot more memory efficient than using an actual list of numbers.
# You can see for yourself by using a list comprehension to create an actual list of numbers from the same range:
myreallist = [i for i in range(0, 10000)]
print(sys.getsizeof(myreallist))
