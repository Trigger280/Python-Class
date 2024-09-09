# #Function as a First class Citizen

# def square(x):

#     return x * x #Assigning a function to a variable


# f = square
# print(f(5))  # Output: 25Passing a function as an argument


# def apply_function(func, value):
#     return func(value)
# result = apply_function(square, 4)
# print(result)  # Output: 16

# #Passing function to a function

# def double(x):

#     return x * 2
# def triple(x):
#     return x * 3
# def apply_operation(func, number):
#     return func(number)
# print(apply_operation(double, 5))  # Output: 10
# print(apply_operation(triple, 5))  # Output: 15

#MAP and Filter Function
numbers=[1,2,3,4,5]
squared=map(lambda x:x*x,numbers)
print(list(squared)) #output: [1,4,9,16,25] Using to filter to get only even numbers from the list

even_numbers=filter(lambda x:x%2==0, numbers)
print(list(even_numbers)) #output: [2,4]