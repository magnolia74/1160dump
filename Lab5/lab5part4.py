

import math
import sys

def armstrong(n):
    count = 0
    for i in range(1, sys.maxsize):
        num = i
        rem = 0
        digit = 0
        sum = 0
        num = i
        digit = int(math.log10(num)+1)

        while (num>0):
            rem = num % 10
            sum = sum + pow(rem, digit)
            num = num // 10
        if(i == sum):
            count += 1
        if (count == n):
            return i



def main():
    user = int(input("Input a number: "))
    print(armstrong(user))

main()



