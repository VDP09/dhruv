import time

print('Hello Buyer!')
time.sleep(1)
item = str(input('Do you want to buy Big Macs, Ferraris or Cruise Ships? \n'))
money = int(input('How much money do you have? Enter only a whole number. \n'))
if item.lower() == 'big macs':
    bigmacs = money/2
    print('With $', money, 'you can buy', bigmacs, 'Big Macs')
else:
    if item.lower() == 'cruise ships':
        cruiseships = money/930000000
        print('With $', money, 'you can buy', cruiseships, 'Cruise Ships')
    else:
        ferraris = money/300000
        print('With $', money, 'you can buy', ferraris, 'Ferraris')
