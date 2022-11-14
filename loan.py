money_owed = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment = float(input("what will your monthly paymrnt be, in dollars?\n"))
months = float(input("how many months do you want to see the results for?\n"))

monthly_rate = apr/100/12

interest_paid = money_owed * monthly_rate
money_owed = money_owed + interest_paid

money_owed = money_owed - payment

print("Paid", payment, "of which", interest_paid, "was interest, end=' '")
print("Now I owe", money_owed)