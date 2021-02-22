# #copy 
# import shutil
# original = r'C:\Users\Minh\Downloads\PyPoll.csv'
# target = r'C:\Users\Minh\Desktop\Git\python-challenge\PyPoll\Resources\PyPoll.csv'
# shutil.copyfile(original, target)
import csv
import os
filepath = os.path.join("Resources","PyPoll.csv")
total_count = []
khan_count = 0
correy_count = 0
li_count = 0
o_count = 0

with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    header = next(csvreader)
    for row in csvreader:
        total_count.append(row[0])
        
        if row[2] == "Khan":
            khan_count = khan_count +1
        elif row[2] == "Correy":
            correy_count = correy_count +1
        elif row[2] == "Li":
            li_count = li_count +1
        else:
            o_count = o_count +1

    percentage_khan = (khan_count/len(total_count)) *100
    percentage_correy = (correy_count/len(total_count))*100
    percentage_li = (li_count/len(total_count))*100
    percentage_o = (o_count/len(total_count))*100
    
    percentage = [percentage_khan,percentage_correy,percentage_li,percentage_o]
    if max(percentage) == percentage_khan:
        winner = "Khan"
    elif max(percentage) == percentage_correy:
        winner = "Correy"
    elif max(percentage) == percentage_li:
        winner = "Li"
    else:
        winner = "O`Tooley"
    
    
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


    output = os.path.join("Analysis","Results.txt")

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
    