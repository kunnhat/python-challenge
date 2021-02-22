#copy 
#import shutil
#original = r'C:\Users\Minh\Downloads\PyBank.csv'
#target = r'C:\Users\Minh\Desktop\Git\python-challenge\PyBank\Resources\PyBank.csv'
#shutil.copyfile(original, target)

#import
import csv
import os
#file locate
filepath = os.path.join("Resources","PyBank.csv")
#define variable
total_month = []
total_profit = []
month_change = []
#open csv file
with open(filepath, 'r') as csvfile:
    #store the file as csvreader
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header
    header = next(csvreader)
    #for each row in csv
    for row in csvreader:
        #append total month
        total_month.append(row[0])
        #append total profit
        total_profit.append(int(row[1]))
    
    #check range to do looping
    print(range(len(total_profit)))
    #go thru profit to get month change
    for i in range(len(total_profit)-1):
        month_change.append(total_profit[i+1]-total_profit[i])
    #determine max increase
    max_increase = max(month_change)
    #determine max decrease
    max_decrease = min(month_change)
        
    #print
    print("\n")
    print("Financial Analysis")
    print("-----------------------------")
    print(f'Total Months: {len(total_month)}')
    print(f'Net Total Amount of "Profit/Losses": {sum(total_profit)}')
    print(f'Average Change: {round(sum(month_change)/len(month_change),)}')
    print(f'Greatest increase in profit: {max_increase}')
    print(f'Greatest decrease in loss: {max_decrease}')
#output file 
output = os.path.join("Analysis","Results.txt")
#write the file
with open(output, 'w') as file:
    file.write("Financial Analytics")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f'Total Months: {len(total_month)}')
    file.write("\n")
    file.write(f'Net Total Amount of "Profit/Losses": {sum(total_profit)}')
    file.write("\n")
    file.write(f'Average Change: {round(sum(month_change)/len(month_change),)}')
    file.write("\n")
    file.write(f'Greatest increase in profit: {max_increase}')
    file.write("\n")
    file.write(f'Greatest decrease in loss: {max_decrease}')