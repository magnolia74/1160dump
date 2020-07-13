

def number():
    while True:
        n=int(input("Enter a number: "))
        if n in range(20,100):
            print("Your number is within the range")
            return n
        else:
            print("Your number is not within the range")
number()