import os
import csv

# find .csv file in directory
election_data = "pypoll/Resources/election_data.csv"

## Define variables
#Sum Total of votes
total_votes = 0
#Define Variable to track candidates
candidate_list = []
current_candidate = ""
previous_candidate = ""
#Define Variables to track candidate votes
candidate1_list = []
candidate2_list = []
candidate3_list = []
vote_percent_can1 = 0.0
vote_percent_can2 = 0.0
vote_percent_can3 = 0.0
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
#Define Variables to find winner
winner = ""

#csv reader
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    #begin 'for' loop
    for row in csvreader:
        
        #find sum total of votes
        total_votes += 1

        #update candidate list
        current_candidate = row[2]
        #add conditional to add candidates to list
        if current_candidate != previous_candidate:
            #add second conditional to prevent repeated values
            if current_candidate not in candidate_list:
                candidate_list.append(current_candidate)
        #add conditional to find vote percentages
        ## These '>=' parts of the conditional are intended to prevent an index error, so the program understands the length of the list it is searching.
        if len(candidate_list) >= 1 and current_candidate == candidate_list[0]:
            candidate1_list.append(row[0])
            candidate1_votes = len(candidate1_list)
            vote_percent_can1 = (len(candidate1_list))/total_votes
        if len(candidate_list) >= 2 and current_candidate == candidate_list[1]:
            candidate2_list.append(row[0])
            candidate2_votes = len(candidate2_list)
            vote_percent_can2 = (len(candidate2_list))/total_votes
        if len(candidate_list) >= 3 and current_candidate == candidate_list [2]:
            candidate3_list.append(row[2])
            candidate3_votes = len(candidate3_list)
            vote_percent_can3 = (len(candidate3_list))/total_votes
        
        #set conditional to find winner
    
        if vote_percent_can1 > vote_percent_can2 and vote_percent_can1>vote_percent_can3:
                winner = candidate_list[0]
        elif vote_percent_can2 > vote_percent_can1 and vote_percent_can2 > vote_percent_can3:
                winner = candidate_list[1]
        elif vote_percent_can3 > vote_percent_can1 and vote_percent_can3 > vote_percent_can2:
                winner = candidate_list[2]
        

        #reset previous_candidate variable
        previous_candidate = current_candidate
    

#print values
print("Election Results")
print("------------------------")
print("Total Votes: ", total_votes)
print(f"Candidates: {candidate_list[0]} {vote_percent_can1:.3%} {candidate1_votes}")
print(f"            {candidate_list[1]} {vote_percent_can2: .3%} {candidate2_votes}")
print(f"            {candidate_list[2]} {vote_percent_can3: .3%} {candidate3_votes}")
print("------------------------")
print("Winner: ", winner)

#select location for text file output
analysis_folder = "pypoll/Analysis"
text_file = os.path.join(analysis_folder, "election_data.txt")
# create and open text file
with open(text_file, 'w') as file:
    # print output in text file
    file.write("Election Results")
    #'/n' added to ensure each value is recorded on a new line in the text file
    file.write("------------------------\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("Candidates: " + candidate_list[0] + " " + "{:.3%}".format(vote_percent_can1) + " " + str(candidate1_votes) + "\n")
    file.write("            " + candidate_list[1] + " " + "{:.3%}".format(vote_percent_can2) + " " + str(candidate2_votes) + "\n")
    file.write("            " + candidate_list[2] + " " + "{:.3%}".format(vote_percent_can3) + " " + str(candidate3_votes) + "\n")
    file.write("------------------------\n")
    file.write("Winner: " + winner)
