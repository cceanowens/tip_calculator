
# Prompting user to input meal cost information
cost_food = float(input("Enter the cost of the food: "))
num_people = int(input("Enter the number of people: "))
percentage = float(input("Enter the percentage of the tip: "))

# Calculating tip and tax amounts
tip_amount = cost_food * (percentage/100)
tax_amount = cost_food * 0.1

# Calculating split of total bill
total_bill = cost_food + tip_amount + tax_amount
per_person = total_bill / num_people

# Displaying results in currency format
print("Total bill: ${:,.2f}".format(total_bill))

if num_people > 1:
    print("Each person should pay ${:,.2f}".format(per_person))