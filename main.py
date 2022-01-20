from calendar import month
import os   
import csv
path = r"C:\Users\mlive\OneDrive\Documents\NU Bootcamp\Homework\NU-VIRT-DATA-PT-11-2021-U-C-main-02-Homework\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv"
with open (path) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
rows = 0
total = 0
Profit = 0
Loss = 0
row_profit = 0
row_loss = 0
Max = 0
Min = 0

PL_change = 0
Total_PL_list = []
Month_change = 0
PL_change_list = []
Total_months_list = []
current_PL = 0
last_PL = 0

for row in path:
    rows += 1

    total = total + int(row[1])

if (int(row[1]) > 0):
    Profit = Profit + int(row[1])
    row_profit += 1
else:
    Loss = Loss + int(row[1])
    row_loss += 1

Total_months_list.append(row[0])
Total_PL_list.append(int(row[1]))












