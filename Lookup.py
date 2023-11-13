import LookUpLog
import PrintColor


# Total
# Time complexity: O(n)
# Space complexity: O(1)

# Look up feature
# Time complexity: O(n)
# Space complexity: O(1)
def start():
    time = ''
    select = ''

    # Keep asking for selection until user end it
    while select != 'e':
        print('Please specify a specific point in time you wish to view package information. ')
        print('Following this format(HH:MM); Example(08:14)')
        time = input('--->')

        # Put the first two digits in hour variable and the last two digits in minute variable
        hour = time[:2]
        minute = time[3:]
        if minute[0] == '0':
            minute = minute[1]
        key = hour + minute
        log = LookUpLog.get_lookup_log().get(int(key))

        # For error handling, in case no record is found
        if log is None:
            PrintColor.prRed('There is no delivery record for this point in time')
            PrintColor.prRed('1. Try to run the simulation first')
            PrintColor.prRed('2. Or all the packages are delivered')
            return

        # Look up menu
        print('How would you like to view the package information?')
        print('a --> all packages status at', time)
        print('i --> Package id')
        print('r --> Package Address')
        print('t --> Package Deadline')
        print('c --> Package City')
        print('z --> Package Zipcode')
        print('w --> Package Mass Kilo')
        print('s --> Package Status')
        select = input('--->')

        # All package look up
        if select == 'a':
            for i in log:
                if i[8] == 'Delivered':
                    PrintColor.prGreen(i)
                if i[8] == 'EN ROUTE':
                    PrintColor.prYellow(i)
                if i[8] == 'At hub':
                    PrintColor.prRed(i)
            return True

        # Package id look up
        if select == 'i':
            p_id = input('Please enter the package id you want to search for: ')
            for i in log:
                if i[0] == p_id:
                    if i[8] == 'Delivered':
                        PrintColor.prGreen(i)
                    if i[8] == 'EN ROUTE':
                        PrintColor.prYellow(i)
                    if i[8] == 'At hub':
                        PrintColor.prRed(i)
            return True

        # Package Address look up
        if select == 'r':
            address = input('Please enter the address you want to search for: ')
            for i in log:
                if i[1] == address:
                    if i[8] == 'Delivered':
                        PrintColor.prGreen(i)
                    if i[8] == 'EN ROUTE':
                        PrintColor.prYellow(i)
                    if i[8] == 'At hub':
                        PrintColor.prRed(i)
            return True

        # Package deadline look up
        if select == 't':
            print('Please enter the package deadline you want to search for: ')
            print('Following this format(10:30 AM)')
            p_deadline = input('--->')
            for i in log:
                if i[2] == p_deadline:
                    if i[8] == 'Delivered':
                        PrintColor.prGreen(i)
                    if i[8] == 'EN ROUTE':
                        PrintColor.prYellow(i)
                    if i[8] == 'At hub':
                        PrintColor.prRed(i)
            return True

        # Package city look up
        if select == 'c':
            print('Please enter the package city you want to search for: ')
            p_city = input('--->')
            for i in log:
                if i[3] == p_city:
                    if i[8] == 'Delivered':
                        PrintColor.prGreen(i)
                    if i[8] == 'EN ROUTE':
                        PrintColor.prYellow(i)
                    if i[8] == 'At hub':
                        PrintColor.prRed(i)
            return True

        # Package zip code look up
        if select == 'z':
            print('Please enter the package zipcode you want to search for: ')
            p_zip = input('--->')
            for i in log:
                if i[4] == p_zip:
                    if i[8] == 'Delivered':
                        PrintColor.prGreen(i)
                    if i[8] == 'EN ROUTE':
                        PrintColor.prYellow(i)
                    if i[8] == 'At hub':
                        PrintColor.prRed(i)
            return True

        # Package weight look up
        if select == 'w':
            print('Please enter the package weight you want to search for: ')
            p_weight = input('--->')
            for i in log:
                if i[5] == p_weight:
                    if i[8] == 'Delivered':
                        PrintColor.prGreen(i)
                    if i[8] == 'EN ROUTE':
                        PrintColor.prYellow(i)
                    if i[8] == 'At hub':
                        PrintColor.prRed(i)
            return True

        # Package status look up
        if select == 's':
            print('Please enter the package status you want to search for: ')
            print('Following this format(Delivered, EN ROUTE, At hub)')
            p_status = input('--->')
            for i in log:
                if i[8] == p_status:
                    if i[8] == 'Delivered':
                        PrintColor.prGreen(i)
                    if i[8] == 'EN ROUTE':
                        PrintColor.prYellow(i)
                    if i[8] == 'At hub':
                        PrintColor.prRed(i)
            return True

    return True
