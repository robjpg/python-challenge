# First we'll import the os module
# This will allow us to create file paths across operating systems
import os 
import csv 

# Module for reading CSV files
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
# Method 1: Plain Reading of CSV files
with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler)
    next(reader)  # Skip the header row

    months = []
    profit_losses = []
    changes = []

    for row in reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
#Total number of months
    total_months = len(months)
 #Net total amount for profit/losses   
    net_total = sum(profit_losses)
#List changes in profit/losses
    for i in range(1, total_months):
        change = profit_losses[i] - profit_losses[i-1]
        changes.append(change)
#Average change
    average_change = sum(changes) / (total_months - 1)
#Greatest increase in profit
    greatest_increase = max(changes)
    greatest_increase_date = months[changes.index(greatest_increase) + 1]
#Greatest decrease in profits
    greatest_decrease = min(changes)
    greatest_decrease_date = months[changes.index(greatest_decrease) + 1]
#Print the results
    print("Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
