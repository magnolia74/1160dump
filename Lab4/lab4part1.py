


#A
lower_limit = 10
upper_limit = 50
while(lower_limit < upper_limit + 1):
    if(lower_limit % 2 != 0):
        print(lower_limit)
    lower_limit += 1

#B
p= input("Enter your input: ")
x = True
while x:
    if (len(p)<8 or len(p)>15):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Input")
        x=False
        break

if x:
    print("Not an Input")
