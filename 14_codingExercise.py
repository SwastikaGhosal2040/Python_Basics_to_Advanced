height = int(input('What is your height in feet?'))
bill = 0
if height>=3:
    print('You can ride')
    age = int(input('What is your age?'))
    if age<12:
        bill += 150
        print('Ticket Price 150 Rs')
    elif age<=18:
        bill += 250
        print('Ticket Price 250 Rs')
    else:
        bill += 500
        print('Ticket Price 500 Rs')
    
    want_photo = input('Do you want to take photo(Y/N)?')
    if want_photo == 'y' or want_photo == 'Y':
        bill = bill + 50
    print(f'Your total bill is {bill}')
else:
    print('Can\'t ride ')
print('Thank you')