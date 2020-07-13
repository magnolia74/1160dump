

#1 - Basic List

list = [1,2,4,5,6,7] # for TUPLES SECTION
#slice the list
list = list[slice(1,4)]

print(list)

#find 6 and 8 in the list
num = 6, 8
if num in list:
    print(list)
else:
    print("error")

#Append 8 to the list

list.append(8)
print(list)

#Find index of 5 in the list obtained from c
list.index(5)
print(list)

#insert number 9 at index 4 in the list from c.
list.insert(4,9)
print(list)

#Sort the list obtained in e.
list.sort()
print(list)

#Reverse the list
list.sort(reverse=True)
print(list)

#PROCESSING LISTS

list2 = [20,30,50,80]
#calculate the total
def listtotal(numList):
   total = 0
   for i in numList:
       total = total + i
   return total

#write to a text file
with open('list.txt', 'w') as filehandle:
   for listitem in list2:
       filehandle.write('%s\n' $ listitem)

#2D LISTS
import random

columns = 3
rows = 2

def main():
    num = [[0, 0, 0],
           [0, 0, 0]]
    for r in range(rows):
       for c in range(columns):
           num[r][c] = random.randint(1, 100)
    print(num)
main()

#TUPLES

# Convert the list to a tuple
list = tuple(list)
print(list)

#Multiply the contents of the tuple

multiplied_list = list*2
print(multiplied_list)


