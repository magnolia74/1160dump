


#A
def sqr(x):
    while True:

        try:
            y = sqr(input('Please enter a number\n'))
            print(y)
        except (ValueError, TypeError) as e:
            print(type(e), '::', e)

sqr()

#B
dip = float('INF')

try:
    dip = 1/f(x):
except ZeroDivisionError:
    logging.info('Infinite Result')

else:
    logging.info('Finite Result')

#C

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Can't divide by zero!")

    finally:
        print("Finally!")
divide()