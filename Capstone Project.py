# imports random module
import random
# imports os module
import os
# imports datetime
import datetime
# Display user profile
user_profile = os.getenv('USERPROFILE')
# print(user_profile)
os.chdir(r"C:\Users\Student\Desktop\Year Up Work\Mod 3\CIS 403 Python")
cwd = os.chdir(r"C:\Users\Student\Desktop\Year Up Work\Mod 3\CIS 403 Python")
working_directory = os.getenv('PWD')
print(user_profile, cwd)
# print(os.getcwd())
# prints name of Programmer
print("Programmer: Jonathan Hill")
# Prints out the date and time of program run
time = datetime.datetime.now()
print(time.strftime(f"Capstone Project %B %d, %Y @ %I:%M:%S\n"))

# Main function
def main():
    # Get user's name
    name = input("Hi! Keep track of your company sales statistics here. \nEnter your name: ")
    sales = ["Sales Period #1", "Sales Period #2", "Sales Period #3", "Sales Period #4", "Sales Period #5",
             "Sales Period #6", "Sales Period #7", "Sales Period #8", "Sales Period #9", "Sales Period #10",
             "Sales Period #11", "Sales Period #12"]
    total_sales_amount = 0
    highest_sales_amount = -99999999
    lowest_sales_amount = 99999999
    sales_list = []

    for i in range(12):
        sale = sales[i]
        sales_amount = float(input(f"What was your sales total for " + sale + "? : "))
        total_sales_amount += sales_amount
        sales_list.append(sales_amount)
        if sales_amount > highest_sales_amount:
            highest_sales_amount = sales_amount
        if sales_amount < lowest_sales_amount:
            lowest_sales_amount = sales_amount
    print()

    average_sales = total_sales_amount / 12
    print(f"{name}, here are your sales statistics for the past 12 Sales Periods: ")
    print(f"Total sales amount:   ${total_sales_amount:,.2f}")
    print(f"Average sales amount:  ${average_sales:,.2f}")
    print(f"Highest sales amount: ${highest_sales_amount:,.2f}")
    print(f"Lowest sales amount:   ${lowest_sales_amount:,.2f}\n")

    print(f"Thank you for recording your sales numbers.\nYour stats are looking great!\n")
    print(f"Keep up the good work, {name}.")

main()
