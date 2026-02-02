

# class Person:
#       def __init__ (self, name):
#         # self allows to attach parameter to the class
#           self.name =name

# p = Person('Asabeneh')
# print(p.name)
# print(p)


# class Person:
#       def __init__(self, firstname, lastname, age, country, city):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city


# p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
# print(p.firstname)
# print(p.lastname)
# print(p.age)
# print(p.country)
# print(p.city)


# class Person:
#       def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
#           self.firstname = firstname
#           self.lastname = lastname
#           self.age = age
#           self.country = country
#           self.city = city
#           self.skills = []

#       def person_info(self):
#         return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
#       def add_skill(self, skill):
#           self.skills.append(skill)

# p1 = Person()
# print(p1.person_info())
# p1.add_skill('HTML')
# p1.add_skill('CSS')
# p1.add_skill('JavaScript')
# p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
# print(p2.person_info())
# print(p1.skills)
# print(p2.skills)



# try:
#     print(76/0)
# except Exception as e:
#     # print(e)
#     print("the denominator value is 0 - Zero Division Error")



#1. Write a program to remove the duplicates from the list without using set()


# def remove_duplicates(lst):
#     result = []

#     for num in lst:
#         if num not in result:
#             result.append(num)
#     return result


# lst = []

# n = int(input("Enter the length of list : "))

# for i in range (n):
#     values = int(input(f"Enter the {i} element of you list : "))
#     lst.append(values)


# print(f"your final list is {lst}")

# result = remove_duplicates(lst)

# print("Final list without duplicates : ", result)


# Write a program to create a dictinory in run-time

dct = {}

n = int(input("Enter the length of you Dict : "))

for i in range(n):
    key = input(f"Enter the {i+1} Key : ")
    value = input(f"Enter the {i+1} value: ")

    dct[key] = value

print(dct)






