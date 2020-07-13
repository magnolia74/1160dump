
#A
k = 1
for i in range(10, 15):
   print("%d^3" % i, end='')
   for j in range(i):
       if (j == 0):
           print(" = %d" % k, end='')
       else:
           print(" + %d" % k, end='')
       k += 2

   print("")

#B
list = [5,6,7,8,9,10,11,12,13]

even_count, odd_count = 0,0

for num in list:
   if num %2 == 0:
        even_count +=1
   else:
        odd_count +=1

print("Even numbers: ",even_count)
print("Odd numbers: ", odd_count)

#C

for i in range(6):
   print(str(i)*i)

