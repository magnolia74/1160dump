





def volume(length, breadth, height):
    if length > 0 and breadth > 0 and height > 0:
        volume = length * breadth * height
    return volume

def main():
    length = int(input("enter length: "))
    breadth = int(input("enter breadth: "))
    height =  int(input("enter height: "))

    total_volume = volume(length,breadth,height)

    print("volume of cuboid", total_volume)

main()