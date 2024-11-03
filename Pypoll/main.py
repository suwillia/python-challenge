# -*- coding: UTF-8 -*-
"""PyPoll Homework Sunil Williams."""

# Import necessary modules
import csv
import os
from subprocess import getoutput

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes=0
# Define lists and dictionaries to track candidate names and vote counts
Candidates=[] # holds out candidates in elections
Can_Votes={} #dictionary to hold the votes results

# Winning Candidate and Winning Count Tracker
maxvote=0 #hold the maximum vote total for the winning candidate
maxvotecan = 0 #used to hold the vote winner.

# Open the CSV file and process it
with open(file_to_load, encoding="utf-8") as election_data:
    reader = csv.reader(election_data)
 
    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:
       
        total_votes +=1 # add to total so as the get the total amount of votes 

        # to get the individual votes for each candidate and store in candidates
        if row[2] not in Candidates:
            #if the candidate is not in the  candidate list we add them to the list using append from the row index2
            Candidates.append(row[2])

            #next we need to work with the dictionary to to hold the vote counts for an individual
            #the first pass will add 1 if the candidate name is not in the list
            Can_Votes[row[2]] =1

        else:
            #this runs when the candidate name is in the list , it then uses += to add one more.
            Can_Votes[row[2]] += 1
        
        # Print a loading indicator (for large datasets)
        print(". ", end="")


#declare variable to hold our candidates + percent amount and total votes iteration
getoutput =""


for winner in Can_Votes:
    # we are using this to get names of the candidates and the % they got from the can_votes dictionary using .get
    # Loop through the candidates to determine vote percentages and identify the winner
    votes= Can_Votes.get(winner)
    voteperc= (int(votes)/ int(total_votes)) * 100
    
    #using if statement to compare max vote for each and then return the matching name
    if votes > maxvote:
        #update the variables to hold max vote and matching candidate
        maxvote = votes
        maxvotecan = winner

   

    getoutput += f"\n{winner}:{voteperc: .3f}% ({votes})\n"

 #generate the output file to be written to the text output with fancy formatting.       
output = (
    f"\nElection Results\n"
    f"\n{'--' * 16}\n" 
    f"\nTotal Votes = {total_votes}\n"
    f"\n{'--' * 16}\n" 
    f"{getoutput}"
    f"\n{'--' * 16}\n" 
    f"\n Winner: {maxvotecan}"
    f"\n{'--' * 16}\n" 

)
# Generate and print the winning candidate summary to terminal
print(output)

# Open a text file to save the output
# Save the winning candidate summary to the text file
with open(file_to_output,"w") as textfile:
    textfile.write(output)