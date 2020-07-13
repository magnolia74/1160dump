


def main():
    new_city = int(input('How many cities do you want to create? '))

    cities = open('cities.txt', 'w')

    for count in range(1, new_city, +1):
        print('Enter data for a city #', count, sep='')
        name = input('City name: ')
        zip = input('ZIP Code: ')

        cities.write(name + '\n')
        cities.write(zip + '\n')

        print()

    cities.close()

    print('Cities are displayed in the text file.')

main()