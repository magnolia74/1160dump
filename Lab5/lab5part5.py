

def string(s):
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for i in s if i.islower())
    print("No. of Upper case characters : %s,No. of Lower case characters : %s" % (upper,lower))

string(input("Enter a string: "))
