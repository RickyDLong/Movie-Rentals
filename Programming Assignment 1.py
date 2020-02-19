#!/usr/bin/python3



#Receipt header print statement stored in variable banner
banner = '''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
*        BlockBankrupt Movie Rentals          *
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

 * * * * * * * * * * * * * * * * * * * * * * *
 *     Welcome! We have a wide variety of    *
 *   movies to rent for $6.00 per day. Just  *
 *  enter the title and release year to find *
 *                 a movie!                  *
 * * * * * * * * * * * * * * * * * * * * * * *

============= RENTAL INFORMATION  =============
'''
print(banner)

#variables to hold the title, release year, and how many days to be rented
title = input('Enter movie title: ')
year_released = input('Enter release year: ')
print()
days_to_rent = (int(input('Enter the number of days to rent: ')))
print()

print('============== ORDER INFORMATION ==============\n')
print('- Rent "'+title+'"''('+year_released+') for '+(str(days_to_rent)+' days(s).\n'))
print('============= PAYMENT INFORMATION =============\n')

#calculating subtotal and totals
rental_fee = float(6.0)
sub_total = rental_fee * days_to_rent
tax = sub_total * .11
total = sub_total + tax

print('''
---------------------
      Receipt
---------------------
''')
print('  '+title+'('+year_released+')')
print(' $'+(str(rental_fee)+' x '+str(days_to_rent)+' days(s)'))
print('---------------------')
print('Subtotal: '+(str(sub_total)))
print('Tax:      '+(str(tax)))
print('Total:    '+(str(total)))
print('---------------------\n')
print('''
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
         Thank you! Please come again!
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
''')
