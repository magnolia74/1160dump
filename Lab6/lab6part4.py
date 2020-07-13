
import os
def add_record():
    another = 'y'
    cities = open('cities.txt', 'a')

    while another == 'y' or another == 'Y':
        print('Enter the following city data: ')
        name = input('City name: ')
        zip = input('ZIP Code: ')

        cities.write(name + '\n')
        cities.write(zip + '\n')
    print('Do you want to add another record?')
    another = input('Y = yes, anything else = no: ')

    cities.close()

add_record()

def show_record():
    cities = open('cities.txt', 'r')

    name = cities.readline()

    while name != '':
        zip = float(cities.readline())
        name = name.rstrip('\n')

        print('City Name: ', name)
        print('Zip Code: ', zip)

        name = cities.readline()
    cities.close()
show_record()

def search():

    found = False
    search = input('Enter a city to search for: ')

    cities = open('cities.txt', 'r')
    name = cities.readline()

    while name != '':
        zip = float(cities.readline())
        name = name.rstrip('\n')

    if name == search:
        print('City name: ', name)
        print('ZIP Code: ', zip)
        print()
        found = True
    name = cities.readline()

    cities.close()
    print('That item was not found in the file.')
search()

def modify():

     found = False
     search = input('Enter a city to search for: ')
     new_zip = int(input('Enter the new ZIP code: '))
     new_city = input('Enter the new city name: ')

     cities = open('cities.txt', 'r')
     temp = open('temp.txt','w')

     cities = cities.readline()
     while cities != '':
         zip = float(cities.readline())
         cities = cities.rstrip('\n')

         if cities == search:
             temp.write(cities + '\n')
             temp.write(str(new_zip)+ '\n')
             temp.write(str(new_city)+ '\n')

              found = True
         else:
            temp.write(cities + '\n')
            temp.write(str(zip) + '\n')
            temp.write(str(cities) + '\n')
         cities = cities.readline()
     cities.close()
     temp.close()

     os.remove('cities.txt')
     os.rename('temp.txt', 'cities.txt')

     if found:
         print('The file is updated')
     else:
        print('The file is not found')
modify()

def delete():
    found = False

    search = input('Which city you want to delete?')

    cities = open('cities.txt', 'r')
    temp = open('temp.txt', 'w')

    cities = cities.readline()
    while cities != '':
        zip = float(cities.readline())
        cities.rstrip('\n')

        if cities != search:
            temp.write(cities + '\n')
            temp.write(zip + '\n')

        else:
            found = True

        cities = cities.readline()

    cities.close()
    temp.close()

    os.remove('cities.txt')
    os.rename('temp.txt', 'cities.txt')

    if found:
        print('The file is updated')
    else:
        print('The file is not found')
delete()




