import csv
import os
file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        print(row)

import csv
import os
file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
print(total_votes)

import csv
import os
file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
print(candidate_options)

import csv
import os
file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0
candidate_options = []
candidate_votes = {}
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
print(candidate_votes)

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)