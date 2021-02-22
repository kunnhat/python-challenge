# #copy 
# import shutil
# original = r'C:\Users\Minh\Downloads\PyPoll.csv'
# target = r'C:\Users\Minh\Desktop\Git\python-challenge\PyPoll\Resources\PyPoll.csv'
# shutil.copyfile(original, target)

#import
import csv
import os

#file location
filepath = os.path.join("Resources","PyPoll.csv")

#define variable
total_count = []
khan_count = 0
correy_count = 0
li_count = 0
o_count = 0

#open csvfile
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skip header
    header = next(csvreader)
    #each row in csv
    for row in csvreader:
        #append total count
        total_count.append(row[0])
        #if function to count the vote for every candidate 
        if row[2] == "Khan":
            khan_count = khan_count +1
        elif row[2] == "Correy":
            correy_count = correy_count +1
        elif row[2] == "Li":
            li_count = li_count +1
        else:
            o_count = o_count +1
    #percentage count
    percentage_khan = (khan_count/len(total_count)) *100
    percentage_correy = (correy_count/len(total_count))*100
    percentage_li = (li_count/len(total_count))*100
    percentage_o = (o_count/len(total_count))*100
    
    #list percentage count and then use if to find the winner
    percentage = [percentage_khan,percentage_correy,percentage_li,percentage_o]
    if max(percentage) == percentage_khan:
        winner = "Khan"
    elif max(percentage) == percentage_correy:
        winner = "Correy"
    elif max(percentage) == percentage_li:
        winner = "Li"
    else:
        winner = "O`Tooley"
    
    #print
    print("Election Results")
    print("---------------------------")
    print(f'Total Votes : {len(total_count)}')
    print("---------------------------")
    print(f'Khan: {format(percentage_khan, ".3f")}% ({khan_count})')
    print(f'Correy: {format(percentage_correy, ".3f")}% ({correy_count})')
    print(f'Li: {format(percentage_li, ".3f")}% ({li_count})')
    print(f'O`Tooley: {format(percentage_o, ".3f")}% ({o_count})')
    print("---------------------------")
    print(f'Winner : {winner}')
    print("---------------------------")

    #output file location
    output = os.path.join("Analysis","Results.txt")

    #write new file
    with open(output, 'w') as file:
        file.write("Election Results")
        file.write("\n")
        file.write("---------------------------")
        file.write("\n")
        file.write(f'Total Votes : {len(total_count)}')
        file.write("\n")
        file.write("---------------------------")
        file.write("\n")
        file.write(f'Khan: {format(percentage_khan, ".3f")}% ({khan_count})')
        file.write("\n")
        file.write(f'Correy: {format(percentage_correy, ".3f")}% ({correy_count})')
        file.write("\n")
        file.write(f'Li: {format(percentage_li, ".3f")}% ({li_count})')
        file.write("\n")
        file.write(f'O`Tooley: {format(percentage_o, ".3f")}% ({o_count})')
        file.write("\n")
        file.write("---------------------------")
        file.write("\n")
        file.write(f'Winner: {winner}')
        file.write("\n")
        file.write("---------------------------")
    