# firstnum=int(input("Enter 1st number"))
# secondnum=int(input("Enter 2nd number"))
# thirdnum=int(input("Enter 3rd number"))
# if firstnum>secondnum:
#     print("a is greater")
# elif secondnum>thirdnum:
#     print("b is greater")
# else:
#     print("c is greater")

# firstname=input("Enter your first name")
# secondname=input("Enter your second name")
# print("Hi , firstname.upper, secondname.upper")


def table(num):
    i=1
    while i<=10:
        value=num*i
        print(f"{num} * {i} = {value}")
        i+=1
try:
    num=int(input("Enter a number"))
    table(num)
except ValueError:
    print("Please enter va valid integer")


