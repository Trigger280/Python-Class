## Filtering items in a dictionary

fruits = ['apple', 'banana', 'cherry']
fruit_dict = {fruit: len(fruit) for fruit in fruits}
print(fruit_dict)