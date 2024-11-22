def date_input():
    dateInput = input('Please enter a date (MM/DD/YYYY): ')
    # 03/23/1999
    # 0123456789
    month = int(dateInput[0:2])
    day = int(dateInput[3:5])
    year = int(dateInput[6:10])

    if month == 9 or month == 4 or month == 6 or month == 11:
        print('30 day month')
        if day < 1 or day > 30:
            print('Invalid Date')
        else:
            print('Valid Date')
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print('31 day month')
        if day < 1 or day > 31:
            print('Invalid Day')
        else:
            print('Valid Day')
    elif month == 2:
        print('February')
        if day >= 1 and day < 29:
            print('Valid Day')
        elif day == 29:
            print('Leap Year??')
            if year % 4 == 0:
                print('Poss Leap Year')
                if year % 400 == 0:
                    print('leap year, valid date')
                elif year % 100 == 0:
                    print('Cant be Leap year')
                else:
                    print('leap year, valid date')
            else:
                print('Not a leap year, invalid year')
        else:
            print('Invalid Day')
    elif month <= 0 or month > 12:
        print('Bad Month')

date_input()