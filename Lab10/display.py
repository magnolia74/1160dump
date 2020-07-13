#Question 3 Import Display

class Display:

    def __init__(self):
        self.__value = 'max'


    def maxvalue(self):
        return int(str(num)[::-1])

    largest = None
    for y in range(1, 999):
        for x in range (1, 999):
            xy = x*y
            if xy > largest and xy == maxvalue(xy):
                largest = xy
    print(largest)
