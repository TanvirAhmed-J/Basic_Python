import re

Year = int(input("Enter the year to check it is leap year or not : "))

if re.match("^[0-9]{4,}$",str(Year)):
    if (Year%4) == 0:
        if ( Year % 100 ) == 0:
            if ( Year % 400 ) == 0:
                print(f"Entred year {Year} is leap a year")
                # print("Entred year {0} is leap a year".format(Year))
            else:
                print(f"Entred year {Year} is not leap year")
        else:
            print(f"Entred year {Year} is a leap year")
    else:
        print(f"Entred year {Year} is not leap year")
