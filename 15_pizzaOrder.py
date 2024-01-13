#Pizza order program
'''
   small Pizza = 100
   Medium Pizza = 200
   Large Pizza = 300
Papperoni for small pizza = 30
Papperoni for medium or large pizza = 50
Extra cheese for any size pizza =20'''

size = input('What is the size of your pizza?(S/M/L)')
bill = 0
if size =='s' or size == 'S':
    bill+= 100
elif size == 'm' or size == 'M':
    bill +=200
else:
    bill += 300
want_paperani = input('Do you want paperani?(Y/N)')
if want_paperani == 'Y' or want_paperani == 'y':
    if size == 'small':
       bill += 30
    else:
        bill += 50
want_extracheese = input('Do you want extra cheese?(Y/N)')
if want_extracheese == 'Y' or want_extracheese == 'y':
    bill += 20
print(f'Your total bill is {bill} Rs')
print('Thank you')
   
