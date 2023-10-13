"""
Your module description
"""
import random

numbahs = [0, 1, 2, 3, 4]
numbers = range(0, 10)
numbers = list(numbers)
print(numbers)
print(numbahs)
print(dir(random))


print(dir(list))

list_of_lists = [[random.randint(0,10) for j in range(0, 5)] for i in range(0,5)]
print(list_of_lists)

