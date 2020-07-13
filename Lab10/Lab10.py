



#Question 1
#a

class Rectangle:
     def __init__(self, length, width):
         self.length = length
         self.width = width

     def area(self):
         return self.length*self.width

 newArea = Rectangle(10,10)
 print(newArea.area())

# #b

class Squares:
     def __init__(self):
         self.max = 1000

     def square(self):
         n= 0
         return n**2

# Question 2
#SEE display.py and solution.py as read from the assignment.

#Question 3
#a
import pickle
import birthday
filename = 'birthdays.dat'

class Birthdays:
    output_file = open(filename, 'wb')

    birth = {}

    month = input("Enter birth month: ")
    day = input("Enter birth day: ")
    year = float(input("Enter birth year: "))

    birth = birthday.Birthdays(month, day, year)

    pickle.dump(birth, output_file)
#b
import pickle


def main():
    end_of_file = False

    input_file = open(filename, 'rb')

    while not end_of_file:
        try:
            birth = pickle.load(input_file)
            display_data(birth)
        except EOFError:

            end_of_file = True

    # Close the file.
    input_file.close()

def display_data(birth):
    print('Month: ', birth.get_month())
    print('Day:', birth.get_day())
    print('Year: ', birth.get_year())
    print()


# Call the main function.
main()
#Question 4
class Person:
    def __init__(self, firstname, lastname):
        self.__first = filename
        self.__surname = lastname

    def set_first(self,firstname):
        self.__first = firstname
    def set_surname(self, lastname):
        self.__surname = lastname

    def get_first(self):
        return self.__first
    def get_surname(self):
        return self.__surname

class Student(Person):
    def __init__(self,firstname, lastname, score):
        super().__init__(firstname, lastname)
        self.testscore = score

    def set_score(self,score):
        self.__testscore = score

    def get_score(self):
        return self.__testscore

class Teacher(Person):
    def __init__(self, firstname, lastname, years):
        super().__init__(self,firstname,lastname)
        self.yearofex = years

    def set_years(self,years):
        self.__yearofex = years
    def get_years(self):
        return self.__yearofex

#Question 5
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

class Squares:
    def __init__(self, side_length):
        self.side_length = side_length
    def sqarea(self):
        return self.side_length*self.side_length

def main():
    rect = Rectangle()
    rect.area()

    sqr = Squares
    sqr.sqarea()

def areas(area):
    area.rectangle()
    area.squares()

main()




