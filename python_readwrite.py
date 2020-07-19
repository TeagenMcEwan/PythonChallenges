# Reading and Writing Files

# Question 1

names = []

with open("names.txt") as txt_file:
    for line in txt_file:



# Question 2

import csv

colour_list = []
english_name_list = []

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colour_list.append(line)

# for colour_name in colour_list:
#    print(colour_name[4])

for (colour_name) in (colour_list):
    english_name_list.append(colour_name)
    
print(english_name_list)