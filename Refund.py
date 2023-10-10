"""
Your module description
"""
days_since_purchase = int(input('How many days ago have you purchased the item? '))
item_used = input('Have you used the item at all [y/n]? ')
damaged = input('Has the item broken down on its own [y/n]? ')

if (days_since_purchase <= 10 and item_used == 'n') or damaged == 'y':
    print('You can get a refund.')
else:
    print('You cannot get a refund.')