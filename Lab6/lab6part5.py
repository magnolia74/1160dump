

def main():

    cities = open('cities.txt','r')

    mega_string = ""

    for line in cities:
        mega_string = mega_string + string(line)
    print(mega_string)


    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except:
        print('An error occured.')
main()