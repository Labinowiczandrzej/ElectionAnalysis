# access the data that we need to inspect
#issues with encoding

import csv
import os


#open election results and read the file with 'r' gives a variable on where to load
file_to_load = os.path.join("Resources/election_results.csv")
#created a file to write in data in analysis folder
file_to_save = os.path.join("analysis", "election_analysis.txt")
#votes accumulator
total_votes=0
#getting the candidates into a list
candidate_options=[]
#getting the candidate votes put together
candidate_votes={}
#creating Winning candidate and Winning Count tracker outside of any loops 
winning_candidate=""
winning_count=0
winning_percentage=0
#Open the election results and read the file
with open(file_to_load) as election_data:
    
#Read the file object with the reader function in csv directory
    file_reader=csv.reader(election_data)
    #print header row into results
    headers=next(file_reader)
    print (headers)
    #Print each row into the file
    for row in file_reader:
        total_votes += 1
        #Printing the candidate name from the 3rd column
        candidate_name=row[2]
        #adding the name to options only if it is unique
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #starting to track votes for each candidate
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
#saving the results to election_analysis
with open(file_to_save,"w") as txt_file:       
#Printing the final vote count to terminal
    election_results = (
        f"\n Election Results \n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    #Saving the final vote count to text
    txt_file.write(election_results)

    
#coding in candidate percentage goes through the dictionary and creates a variable votes for the f string formula
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float (total_votes)*100
        candidate_results =(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        #set the winning_count and percentage to votes and percentage if true# winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            winning_count =votes
    #print the winner and the stats
    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n")
    print(winning_candidate_summary)
    #writing summary to txt file
    txt_file.write(winning_candidate_summary)




    


