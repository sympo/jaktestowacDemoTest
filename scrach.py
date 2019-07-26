
#for tester in "Michal": print(tester); print("hello"); print ("It's me")

# python -m pytest testsuite_all_tests.py --alluredir ./results     //commandline tests
# libs\allure-2.11.0\bin\allure serve ./results


"""my_age = 17

if my_age > 17:
    print(f'Age {my_age}: You can enjoy very dramatic movie')
else:
    print(f'Age {my_age}: Sorry young person - you are not allowed to see dramatic content')

if my_age >= 18:
    print(f'Age {my_age}: You can enter to exclusive bar property')
else:
    print(f'Age {my_age}: Beer is not for you')

if my_age < 18:
    print(f'Age {my_age}: You can dance in supermarket')
else:
    print(f'Age {my_age}: Adult person - behave yourself')

if my_age <= 17:
    print(f'Age {my_age}: Write a poem')
else:
    print(f'Age {my_age}: Go to work you lazybones')

if my_age != -18:
    print(f'Age {my_age}: Sorry, no 18th party this year')
else:
    print(f'Age {my_age}: It\'s time for party') """

# a = 0
# b = 1
#
# try:
#     result = a / b
#     print(result)
# except ZeroDivisionError as zero_error:
#     print(zero_error)
#     print("Error! ZeroDivision Error!")
# except TypeError as type_error:
#     print(type_error)
#     print("error! type error!")
# else:
#     try:
#         result = b / a
#         print(result)
#     except:
#         print("Nope....")
# finally:
#     print("Im always here!\n")


# nominator = 100.21
# denominator = 'a string'
#
# try:
#     result = nominator / denominator
# except TypeError:
#     print("An exception TypeError Occurred!")
#     print('')
# else:
#     print('No errors!')
#     print(result)
#     print('')
#
#
# def calculate_percent(value, total):
#     try:
#         percent = value * 100 / total
#     except TypeError:
#         print(f'Invalid Values! "{value}" and "{total}" must be a valid number')
#     except ZeroDivisionError:
#         print(f'Invalid Values! "{value}" and "{total}" must be a valid number')
#     else:
#         print(f'{value} from {total} is {percent}%')
#
#
# calculate_percent(1, 2)
# calculate_percent(2, 1)
# calculate_percent('1', 2)
# calculate_percent('a', None)
# calculate_percent(28, 0)
# calculate_percent(50, 99)
#
#
# def fun():
#     a = 1
#     b = 2
#
#     try:
#         result = a / b
#         print(result)
#         return (result)
#     except:
#         print('Error')
#         return None
#     finally:
#         print('Finally!')
#
#
# fun()

# from selenium import webdriver
# import selenium
#
#
# driver = webdriver.Chrome(executable_path=r"C:\TestFiles\chromedriver.exe")
# driver.get('https://antoogle.testoneo.com/')
#
# xpath_list = ['*yolo_this_is_not_xpath*', '//*[@class="this xpath cannot be found"]',
#               '//*[@class="h6 mb-3 font-weight-normal"]']
#
# for xpath in xpath_list:
#    try:
#       elem = driver.find_element_by_xpath(xpath)
#    except selenium.common.exceptions.InvalidSelectorException as error:
#       print(f'XPath {xpath} is broken!')
#       print(error)
#    else:
#       print(f'XPath {xpath} is fine and element was found - good job!')
#
#    driver.quit()


# class Calculator(object):
#    def multiply(value_1, value_2):
#        return value_1 * value_2
#
#    def add(value_1, value_2):
#        return value_1 + value_2
#
#    def divide(value_1, value_2):
#        raise NotImplementedError('Not implemented yet!')
#
#
# raise NotImplementedError('Any message')
#
# print(Calculator.multiply(2, 6))
# print(Calculator.add(2, 6))
# print(Calculator.divide(2, 6))


# def unsafe_calculate_percent(value, total):
#    try:
#        return value * 100 / total
#    except TypeError:
#        raise ValueError(f'Invalid values! "{value}" and "{total}" must be a valid number!')
#    except ZeroDivisionError:
#        raise ValueError(f'Invalid values! "{value}" and "{total}" must be a valid number!')
#
#
# def safe_calculate_percent(value, total):
#     try:
#         percent = unsafe_calculate_percent(value, total)
#     except ValueError as value_error:
#         print(value_error)
#     else:
#         print(f'{value} from {total} is {percent}%')
#
#
# safe_calculate_percent(1, 2)
# safe_calculate_percent('1', 2)
# safe_calculate_percent('a', None)
# safe_calculate_percent(28, 0)
# safe_calculate_percent(50, 99)


# class Animal:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#         print(f'Animal!')
#
#     def increase_age(self):
#         self.age += 1
#         print(f'My name is {self.name} and my age is: {self.age}')
#
#
# class Mammal(Animal):
#     def __init__(self, age, name):
#         Animal.__init__(self, age, name)
#         print("mammal!")
#
#
#     def introduce_yourself(self):
#         print(f'My name is {self.name}!')
#
#
# class Cat(Mammal):
#     def __init__(self, age, name, master):
#         Mammal.__init__(self, age, name)
#         self.master = master
#         print("Cat!")
#
#     def purr(self):
#         print('purr!')
#
#     def introduce_yourself(self):
#         super().introduce_yourself()
#         print(f'My master is {self.master}')
#
#
# class Dog(Mammal):
#     def __init__(self, age, name, master, favorite_toy):
#         Mammal.__init__(self, age, name)
#         self.master = master
#         self.favorite_toy = favorite_toy
#         print('Dog!')
#         self.
#
#     def introduce_yourself(self):
#         super().introduce_yourself()
#         print(f'My master is {self.master} my favorite toy is: {self.favorite_toy}')
#
#
# cat_1 = Cat(2, 'mrczuek', 'michal')
# cat_1.introduce_yourself()
# cat_1.purr()
# cat_1.increase_age()
#
# dog_1 = Dog(2, 'Burek', 'Michal', 'Piłka do tenisa')
# dog_1.introduce_yourself()
# dog_1.increase_age()
import data as data
import faker
import xlwt

date = faker.Faker()
wk = xlwt.Workbook()
ws = wk.add_sheet("Sheet1")

for i in range(0, 1000):
    ws.write(i, 0, data.name())
    ws.write(i, 1, data)



