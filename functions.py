

# def generate_full_name ():
#     first_name = 'Asabeneh'
#     last_name = 'Yetayeh'
#     space = ' '
#     full_name = first_name + space + last_name
#     print(full_name)
# generate_full_name () # calling a function

# def add_two_numbers ():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     print(total)
# add_two_numbers()



# def generate_full_name ():
#     first_name = 'Asabeneh'
#     last_name = 'Yetayeh'
#     space = ' '
#     full_name = first_name + space + last_name
#     return full_name
# lst = list(generate_full_name())
# print(lst)

# def add_two_numbers ():
#     num_one = 2
#     num_two = 3
#     total = num_one + num_two
#     return total
# print(add_two_numbers())


# def greetings (name):
#     message = name + ', welcome to Python for Everyone!'
#     print(message)

# name_value = input("Enter your name : ")
# greetings(name_value)

# def add_tow_numbers(num1, num2):
#     tot = num1 + num2
#     print(tot)

# number1 = int(input("Enter first number : "))
# number2 = int(input("Enter second number : "))

# add_tow_numbers(number1, number2)

# def add_tow_numbers(num1, num2):
#     tot = num1 + num2
#     return tot

# number1 = int(input("Enter first number : "))
# number2 = int(input("Enter second number : "))

# print(add_tow_numbers(num1 = number1, num2 = number2))

# def add_ten(num):
#     ten = 10
#     return num + ten
# print(add_ten(90))

# def square_number(x):
#     return x * x
# print(square_number(2))

# def area_of_circle (r):
#     PI = 3.14
#     area = PI * r ** 2
#     return area
# print(area_of_circle(10))




def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5, 6, 2, 9)) # 10













