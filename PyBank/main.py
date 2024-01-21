import csv
import os

csvpath = os.path.join("Resources", "budget_data.csv")

# Initalize variables and lists
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Identify date and profit/loss in dataset 
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total number of months
        total_months = total_months + 1

        # Calculate net total amount of profit/losses
        net_total = net_total + profit_loss

        # Calculate change in profit/loss and store in the list
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            # Add change and date to respective lists to call upon later
            changes.append(change)
            dates.append(date)

        # Update previous profit/loss for the next row
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

# Identify greatest increase and decrease
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export results to the results text file
output_path = os.path.join("analysis", "results.txt")
with open(output_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${round(average_change, 2)}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

