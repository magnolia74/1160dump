


temp = int(input("Enter the temperature: "))


if temp > 93:
    print("VERY HOT")

elif temp < 93 or temp > 80:
    print("HOT")

elif temp <= 79 or temp > 68:
    print("WARM")

elif temp < 68:
    print("COLD")