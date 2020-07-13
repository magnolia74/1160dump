

#String basics

#A

str = "Programming"

for a in str:
    print(a)

#B
count = 0
for ch in str:
    if ch == 'r':
        count += 1
print(count)

#C

str = str + ' is fun'
print(str)

#Processing strings:

str = "CS1160 Introduction to Programming "
#A
con = str[7:-1]

print(con)

#B
def count(str):
    upper, lower, digits = 0,0,0

    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z':
            upper += 1
        elif str[i] > 'a' and str[i] <= 'z':
            lower += 1
        elif str[i] > '0' and str[i] <= '9':
            digits += 1
    print(upper)
    print(lower)
    print(digits)

count(str)

#String methods:

str = "XxxXXCS1160 Introduction to programminggggg"
#A
#remove the X's and G's
remove = str[5:-4]
print(remove)
#B
str = str[5:27] + ' is the course code for the class, ' + str[12:-4]

print(str)
