

#A
i = 2

while (i<50):
    j=2
    while(j <= (i/j)):
        if not(i%j):
            break
        j=j+1
        if(j>i/j):
            print(i, " is prime")
    i = i+1

#B

lastnumber = 6
for row in range(1, lastnumber):
    for column in range(1,row+1):
        print(column, end='')
    print("")
