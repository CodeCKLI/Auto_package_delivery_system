# Student Name: CHUN KAI LI, Student ID: 010875202
import Delivery
import Lookup

select = ''
isRun = False

# Total
# Time complexity: O(1)
# Space complexity: O(1)

# Program starts in main.py
# Keep asking for selection until user end it
while select != 'e':
    print("Welcome to Western Governors University Parcel Service (WGUPS)! What would you like to do today?")
    print("d -> Start delivery simulation")
    print("e -> Exit program")

    # The lookup feature shows after the simulation has been run
    if isRun:
        print("l -> Lookup function")
    select = input('---> ')

    # Delivery simulation feature
    if select == 'd':
        Delivery.start()
        print()
        print('What would you like to do next?:')
        print('(b)--> Back to Menu ')
        print('(l)--> Look up package information ')
        print('(e)--> Exit the program ')
        select = input('--->')
        if select == 'l':
            Lookup.start()
            select = input('Back to main menu?(y/n): ')
            if select == 'n':
                select = 'e'
        isRun = True

    # Look up feature
    if select == 'l':
        Lookup.start()
        print()
        select = input('Back to main menu?(y/n): ')
        if select == 'n':
            select = 'e'

