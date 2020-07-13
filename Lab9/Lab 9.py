

#Question 1

grd = {'Math':'81', 'Physics':'83','Chemistry':'87','Biology':'90','Python':'75'}

#pop, popitem(), del functions
#a
pop = grd.pop('Math', 'Entry not found')
print(pop)
popit = grd.popitem()
print(popit)
#b
grd["Chemistry"] = 88
print(grd)
get = grd.get('Physics', 'Entry not found')
print(get)
#c
grd.get('Biology','NOT FOUND')

print(grd)

#Question 2
grades = dict()
#
studname = grades.keys()
studgrd = grades.values()
# #a
for count in range(5):
   studname = input("Enter student name: ")
   studgrd = input("Enter grade: ")
   grades[studname] = studgrd
#
# #b
for key in grades.keys():
    print(key)
    print(grades[key])
# #c
for value in grades.values():
    print(value)
# #d
for item in grades.items():
    print(key, value)
#Question 3

city_and_state = {'New York':'NY',
                  'Dayton ':'OH',
                  'Maryville': 'MO',
                  'Georgia': 'AL',
                  'San Franc': 'CA',
                  'Seattle': 'AL'
                  }

print('Key' '\t' '\t' ' Value')
print('===============')
for key, value in city_and_state.items():
    print(key,'\t', value)
#a
city_and_state.__len__(dict)
city_and_state['Seattle'] = 'WA'
#b
#list = []
for dict_key, dict_value in d.items():
   list = dict_key + dict_value
   list.append()

#c

if 'Paris' in city_and_state.keys():
    print("It is present")
elif 'Lucerne' not in city_and_state.keys():
   print("It is not present")

#Question 4

data = {
        "Tweet1": {
            "Likes": 100,
           "follows": 110,
            "followed_by": 120
       },
     "Tweet2": {
            "Likes": 200,
             "follows": 210,
            "followed_by": 220
        },
        "Tweet3": {
            "Likes": 300,
             "follows": 310,
             "followed_by": 320
         },
         "Tweet4": {
             "Likes": 400,
             "follows": 410,
             "followed_by": 420
         },
         }
#a
for x in data.items():
      tup = [(v) for v in data.items()]
      print(tup)
#b
try:
    del data["Tweet 5"]
except KeyError:
    print("key error exception is raised due to accessing an absent key")
finally:
    data.update({"Tweet5":{"Likes": 500,"Follows":510,"followed_by": 520}})

#Question 5

myset = set(range(1,10,2))

for val in myset:
    myset.discard(-1)
    print(val)

#Question 6
import pickle
#a
def main():
    again = 'y'

    cities = open('cities.dat', 'wb')

    while again.lower() == 'y':
        save_data(cities)
        again = input('Enter more? (y/n): ')

    cities.close()
#
def save_data(file):
    city = {}

    city['City_name'] = input('City name: ')
    city['City_state'] = input('City state: ')
    city['ZIPCode'] = input('ZIP Code: ')

    pickle.dump(city, file)

main()
# #b
def main():
    end_of_file = False

    input = open('cities.dat', 'rb')

    while not end_of_file:
        try:
            city = pickle.load(input)

            display(city)
        except EOFError:
            end_of_file = True

def display(city):
    print('City name: ', city['City_name'])
    print('City state: ', city['City_state'])
    print('ZIP Code: ', city['ZIPCode'])
    print()

main()












