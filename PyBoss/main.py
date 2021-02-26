# import shutil
# original = r'C:\Users\Minh\Downloads\PyBoss.csv'
# target = r'C:\Users\Minh\Desktop\Git\python-challenge\PyBoss\PyBoss.csv'
# shutil.copyfile(original, target)

import os
import csv

filepath = os.path.join("PyBoss.csv")

usstateabbrev = []
fullname = []
first_name = []
last_name = []
dob = []
d_o_b = []
snn = []
s_n_n = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
with open(filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:

        usstateabbrev.append(us_state_abbrev[row[4]])
        
        fullname = row[1].split(" ")
        first_name.append(fullname[0])
        last_name.append(fullname[1])

        dob = row[2].split("-")
        d_o_b.append(dob[1] + "/" + dob[2] + "/" + dob[0])

        snn = row[3].split("-")
        s_n_n.append("***_**" + "-" + snn[2])
print(d_o_b)
print(s_n_n)
