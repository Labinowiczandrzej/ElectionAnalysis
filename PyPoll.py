# access the data that we need to inspect
#issues with encoding

import csv
import os


#open election results and read the file with 'r'
file_to_load = os.path.join("Resources/election_results.csv")
#created a file to write in data in analysis folder
file_to_save = os.path.join("analysis", "election_analysis.txt")

    
#Open the election results and read the file
with open(file_to_load) as election_data:
    
#Read the file object with the reader function in csv directory
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    print (headers)
    




# 1)calculate the total number of votes cast
# 2) A complete list of the candidates who recieved votes
# 3) the percentage of votes each candidate won
# 4) the total number of votes each candidate won
# 5) Who was the winning candidate by popular vote
#Close the file.
    


