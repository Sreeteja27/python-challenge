#Importing the required modules
import os
import csv

#Creating an object out of the CSV file
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the header row and then first row
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    #looping through each row of data after the header & first row 
    for row in csvreader:

        dates.append(row[0])
        
     #Calculating the change and then adding it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
    #Total number of months in the dataset
        total_months += 1

    #The net total amount of "Profit/Losses" over the entire period
        total_pl = total_pl + int(row[1])
    
    #The Average change in "Profit/Losses" over the entire period
    avg_change = sum(profits)/len(profits)

    #The Greatest increase in profits over the entire period
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #The Greatest decrease(lowest increase) in profits over the entire period
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]


print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "-------------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

