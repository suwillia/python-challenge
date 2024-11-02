# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""
# sunil williams
# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data

total_months = 0 # initialiaze to 0  to hold months
total_net = 0 # initialiaze to 0 to hold the sum of the totals
monthly_changes = [] # we need to create a list so we can track the cahnges to net and 
grdec=["",0] # store each month as well as the value for greatest decrease
grinc=["", 0] # store each month as well as the value for greatet increase

# read csv file
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net changes
    firstnet = next(reader) #  we need to start at the row below the header for the net 

    # total revenue for column 2 /index 1
    total_net += int(firstnet[1])
    
    previous_net = int(firstnet[1]) # hold the starting point for calculation
    
    total_months += 1 # add months using counter
    
    for row in reader:
        # calculate the months totals
        total_months += 1 # add months using counter
        # total revenue for column 2 /index 1, we need to change from as text too
        total_net += int(row[1])
  
        # Track the total and net change 
        netchange = int(row[1]) - previous_net
        # append to monthly changes so we can track each month difference
        monthly_changes.append(netchange)

        # previous net needs to be changed to the next row by adding 1 
        previous_net = int(row[1])

         # Calculate the greatest increase in profits (month and amount)
        if netchange > grinc[1]:
            grinc = [row[0], netchange]

        # Calculate the greatest decrease in losses (month and amount)
        if netchange < grdec[1]:
            grdec = [row[0], netchange]


# Calculate the average net change across the months
    avg_net_change = int(sum(monthly_changes) / len(monthly_changes)) if monthly_changes else 0

# Generate the output summary
output =(
"Financial Analysis\n"
f"{'--' * 16}\n"    
f"Total Months : {total_months}\n" 
f"Total :$ {total_net:,.2f}\n"
f"Average change :$ {avg_net_change:,.2f}\n"
f"Greatest Increase in Profits: {grinc[0]} (${grinc[1]})\n"
f"Greatest Decrease in Profits: {grdec[0]} (${grdec[1]})\n"
)
# Print the output
print(output) 
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
 