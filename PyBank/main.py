import os
import csv
# Set path for CSV file; received help from Sam to open file and upload data
csvpath = os.path.join("Resources","budget_data.csv")
# Establish empty lists to store data: dates and profits & losses
dates =[]
profitsANDlosses =[]
changes = []
# Read CSV file and specify delimiter
with open(csvpath, 'r') as file:
    # Specify delimiter in CSV
    csvreader = csv.reader(file, delimiter=",")
    # Read the first row as the header
    csv_header = next(csvreader)
   # Loop through each row of data; assisted by Xpert Learning Assistant
    for row in csvreader:
        dates.append(row[0]) # Store month & year data into dates list
        profitsANDlosses.append(int(row[1])) # Store profits and losses data into profitsANDlosses list
    # Print total number of months, assisted by Xpert Learning Assistant
    print(f"Total months: {len(dates)}")
    # Print total sum of profits and losses; assisted by Xpert Learning Assistant
    print(f"Total: ${sum(profitsANDlosses)}")
    for i in range(1,len(profitsANDlosses)):
        change = profitsANDlosses[i] - profitsANDlosses[i - 1]
        changes.append(change)
    # Calculate mean of average change
    mean = sum(changes) / len(changes)
    # Print calculation of average change
    print(f"Average Change: ${mean}")
    # Zip dates list with change list
    datesANDchanges = list(zip(dates, changes))
    # Print zipped list 
    # print(datesANDchanges)
    # Print greatest increase in profits
    print(f"Greatest Increase in Profits: {max(datesANDchanges)}")
    # Print greatest decrease in profits
    print(f"Greatest Decrease in Profits: {min(datesANDchanges)}")
    # Export results to text file
    data = [
        "Total months: 86"
        "Total: $22564198"
        "Average Change: $-8311.105882352942"
        "Greatest Increase in Profits: Sep-16, $1627245"
        "Greatest Decrease in Profits: Apr-10, $1581126"
    ]
    # Establish file path for text file output
    output_file = "main_output.txt"

