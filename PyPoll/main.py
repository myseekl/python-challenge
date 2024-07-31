import os
import csv
# Set path for CSV fle
csvpath = os.path.join("Resources","election_data.csv")
#Establish lists; Xpert Learning Assitant assisted with lists for voting
voterID = []
county = []
candidate =[]
CCS_votes = 0
DG_votes = 0
RAD_votes = 0
with open(csvpath, 'r') as file:
    # Specify delimiter in CSV
    csvreader = csv.reader(file, delimiter=",")
    # Read the first row as the header
    csv_header = next(csvreader)

   # Loop through each row of data
    for row in csvreader:
        voterID.append(row[0]) # Store voter ID into the list
        county.append(row[1]) # Store county into the list
        candidate.append(row[2]) #Store candidate into the list
    # Loop through data for candidate for candidate findings; Xpert Learning Assitant fixed by adding row[2] and removed reference of candidate list to possibly remove redundancy
        if row[2] == "Charles Casper Stockham":
            CCS_votes += 1
        elif row[2] == "Diana DeGette":
            DG_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            RAD_votes += 1
    # Create variable for TOTALvotes; relocated this line due to suggestion from XpertLearning Assistant
    TOTALvotes = len(voterID)
    # Calculate each candidate's voting percentage
    CSS_percent = CCS_votes/TOTALvotes*100
    DG_percent = DG_votes/TOTALvotes*100
    RAD_percentage = RAD_votes/TOTALvotes*100
    # Print results
    print("Election Results")
    print("--------------------------------------------")
    print(f"Charles Casper Stockham: {CSS_percent}% ({CCS_votes})")
    print(f"Diana DeGette: {DG_percent}% ({DG_votes})")
    print(F"Raymon Anthony Doane: {RAD_percentage}% ({RAD_votes})")
    print("--------------------------------------------")
    print(f"Winner: Diana DeGette")