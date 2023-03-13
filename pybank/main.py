import os
import csv

# find .csv file in directory
budget_data = "pybank/Resources/budget_data.csv"

# Define variables to find Total Months
num_months = 0
# Define Variables to find Total of profit/losses
profit_loss = 0
# Define variables to find Average Change
previous_pl = 0
change_list = []
# Define variables to find greatest increase in profit & month
greatest_increase = 0
    #set gi_month as string to return row[0] value
gi_month = ""
# Define variables to find greatest decrease in profit & month
greatest_decrease = 0
    #set gd_month as string to return row[0] value
gd_month = ""

# csv reader
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
       
        # Calculate number of months
        num_months += 1
        
        # Calculate net total amount of "Profit/Losses"
        profit_loss += int(row[1])
        
        # Calculate change in "Profit/Losses"
        current_pl = int(row[1])
        #find greatest increase and decrease; track monthly change
        ## If previous_pl ≠ 0
        if previous_pl != 0:
            monthly_change = current_pl - previous_pl
            change_list.append(monthly_change)
            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                gi_month = row [0]
            if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                gd_month = row[0]
        #reset previous_pl for next iteration
        previous_pl = current_pl

# Find average monthly change in profit/loss values
average_change = sum(change_list) / len(change_list)

# Print values
print("Financial Analysis")
print("----------------------------")
print("Total Months: ", num_months)
print("Total: $", profit_loss)
print("Average Change: $", round(average_change, 2))
print("Greatest Increase in Profits:", gi_month, "($", greatest_increase, ")")
print("Greatest Decrease in Profits:", gd_month, "($", greatest_decrease,")")

#select folder for text file output
analysis_folder = "pybank/Analysis"
text_file = os.path.join(analysis_folder, "budget_data.txt")
#create and open text file
with open (text_file, 'w') as file:
    #print output as text file
    file.write("Financial Analysis")
    #'/n' added to ensure each value is recorded on a new line in the text file
    file.write("------------------------\n")
    file.write("Total Months: " + str(num_months) + "\n")
    file.write("Total: $" + str(profit_loss) + "\n")
    file.write("Average Change: $" + str(round(average_change,2)) + "\n")
    file.write("Greatest Increase in Profits: " + gi_month + "($" + str(greatest_increase) + ")" + "\n")
    file.write("Greatest Decrease in Profits: " + gd_month + "($" + str(greatest_decrease) + ")" + "\n")


