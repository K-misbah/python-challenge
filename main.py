from calendar import month
import os   
import csv


total = 0
PL_change = []
PL_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",99999999]
total_net = 0


path = os.path.join("resources.csv")
with open (path) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    first_row = next(csvreader)
    total += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])


    for row in csvreader:
        total += 1
        total_net += int(row[1])

        # tracking total

# Tracking net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        PL_change_list += [net_change]
        PL_change += [row[0]]
        # total = total + int(row[1])

# calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
          
# calculate greatest decrease          
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# calculate avg net change
avg_net_change = sum(PL_change_list) / len(PL_change_list)

# generate output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)
with open ("output.txt", "w") as txt_file:
    txt_file.write(output)










