import csv
import os

# Path to the CSV file
csvpath = os.path.join("Resources", "election_data.csv")

# Initialize variables and dictionaries
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}
candidate_percentages = {}

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)

    # Total the number of votes cast
    for row in csvreader:
        total_votes  = total_votes + 1

        # Check if the candidate is already in the dictionary
        candidate_name = row[2]
        # If the candidate's name is already within the dictionary, then add a vote to their value
        if candidate_name in candidates:
            candidates[candidate_name] = candidates[candidate_name] + 1
        # If the candidate is not within the dictionary, add their name and set the value to 1 vote
        else:
            candidates[candidate_name] = 1

        # Update the winner dictionary
        if candidates[candidate_name] > winner["votes"]:
            winner["name"] = candidate_name
            winner["votes"] = candidates[candidate_name]

# Calculate the percentage of votes each candidate won
# Iterate through key-value pairs in the candidates dictionary
for name, votes in candidates.items():
    # Calculate the percentage of votes for each candidate
    percentage = (votes / total_votes) * 100

    # Add the candidate name and percentage to the new dictionary
    candidate_percentages[name] = percentage


# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage in candidate_percentages.items():
    print(f"{candidate}: {percentage:.3f}% ({candidates[candidate]})")
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

# Export the results to a text file
output_path = os.path.join("analysis", "results.txt")
with open(output_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, percentage in candidate_percentages.items():
        output_file.write(f"{candidate}: {percentage:.3f}% ({candidates[candidate]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner['name']}\n")
    output_file.write("-------------------------\n")
