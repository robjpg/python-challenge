# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

# Log file address in py_poll_csv
py_poll_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Add variables
total_votes = 0

# Add lists
candidates = []

# Scan CSV file
with open(py_poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    next(csvreader)

    # Loop through the file
    for row in csvreader:
        # Count number of total votes
        total_votes += 1

        # Capture unique candidates names
        if row[2] not in candidates:
            candidates.append(row[2])

# Initialize vote counts for each candidate
candidate_votes = [0] * len(candidates)

# Scan CSV file again to count votes for each candidate
with open(py_poll_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header row
    next(csvreader)

    # Loop through the file
    for row in csvreader:
        candidate_index = candidates.index(row[2])
        candidate_votes[candidate_index] += 1

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for i in range(len(candidates)):
    vote_percentage = (candidate_votes[i] / total_votes) * 100
    print(f"{candidates[i]}: {vote_percentage:.3f}% ({candidate_votes[i]})")
print("-------------------------")
print(f"Winner: {candidates[candidate_votes.index(max(candidate_votes))]}")
print("-------------------------")
