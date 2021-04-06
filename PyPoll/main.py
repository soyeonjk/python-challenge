import os
import csv
import collections
from collections import Counter

# define variables
voters_candidates = []
votes_per_candidate = []

# create path
election_data_csv_path = os.path.join("..", "Resources", "election_data.csv")

with open(election_data_csv_path) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    
    csv_header = next(csvfile)

    for row in csv_reader:

        voters_candidates.append(row[2])

    
    sorted_list = sorted(voters_candidates)

    arrange_list = sorted_list

    #count votes per candidate in most common outcome order and append to a list
    count_candidate = Counter (arrange_list) 
    votes_per_candidate.append(count_candidate.most_common())

    # calculate the percentage of votes per candicate in 3 digital points
    for item in votes_per_candidate:
       
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
          
    
# -->>  print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {sum(count_candidate.values())}")
print("-------------------------")
print(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})")
print(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})")
print(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})")
print(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {votes_per_candidate[0][0][0]}")
print("-------------------------")


# -->>  export a text file with the results
election_file = os.path.join("..", "Analysis", "election_data.txt")
with open(election_file, "w") as new:

    new.write("Election Results\n")
    new.write("-------------------------\n")
    new.write(f"Total Votes:  {sum(count_candidate.values())}\n")
    new.write("-------------------------\n")
    new.write(f"{votes_per_candidate[0][0][0]}: {first}% ({votes_per_candidate[0][0][1]})\n")
    new.write(f"{votes_per_candidate[0][1][0]}: {second}% ({votes_per_candidate[0][1][1]})\n")
    new.write(f"{votes_per_candidate[0][2][0]}: {third}% ({votes_per_candidate[0][2][1]})\n")
    new.write(f"{votes_per_candidate[0][3][0]}: {fourth}% ({votes_per_candidate[0][3][1]})\n")
    new.write("-------------------------\n")
    new.write(f"Winner:  {votes_per_candidate[0][0][0]}\n")
    new.write("-------------------------\n")    

