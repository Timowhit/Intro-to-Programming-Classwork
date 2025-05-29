import time
import random

data_set = []
mrrandom = ["Mr.", "Mrs.", "Ms.", "Mr."]

print()
print()
print("This is a life expectancy database presented by yours truly.")
time.sleep(3)

answer_1 = None
while answer_1 not in range(40,80):
    answer_1 = int(input("How many years do you think you will live? "))
    if answer_1 < 40:
        print()
        print(f"{answer_1} is kinda young...")
    elif answer_1 > 80:
        print()
        print(f"{answer_1} is kinda stretching it...")
print()
time.sleep(2)
print("Sounds about right.")
time.sleep(3)
print(f"Fun fact {random.choice(mrrandom)}{answer_1}!")
time.sleep(1)
print("...")
print()
time.sleep(9)

with open('Coding_Class_Work/life-expectancy.csv') as data_file:

    for line in data_file:

        if line.startswith("Entity"): continue

        row = line.split(",")
        row[2] = int(row[2])
        row[3] = float(row[3])

        data_set.append(row)

min_years = 9999
min_year = None
min_country = None

for i in data_set:
    if i[3] < min_years:
        min_years = i[3]
        min_year = i[2]
        min_country = i[0]


max_years = 1
max_year = None
max_country = None

for i in data_set:
    if i[3] > max_years:
        max_years = i[3]
        max_year = i[2]
        max_country = i[0]

print(f"{min_country} in {min_year} has the lowest life expectancy of {min_years} years.")
print(f"{max_country} in {max_year} has the highest life expectancy of {max_years} years.")

time.sleep(3)
print()
input_year = None
while input_year not in range(1949,2020):
    input_year = int(input("Pick a year between 1950-2019: "))

    if input_year not in range(1949,2020):
        print("Please input a valid Year")

year_list = []
for i in data_set:
    if i[2] == input_year:
        year_list.append(i)

min_years = 9999
min_year = None
min_country = None

for i in year_list:
    if i[3] < min_years:
        min_years = i[3]
        min_year = i[2]
        min_country = i[0]


max_years = 1
max_year = None
max_country = None

for i in year_list:
    if i[3] > max_years:
        max_years = i[3]
        max_year = i[2]
        max_country = i[0]

for i in year_list: #i don't think the math is coming out right on this
    sumyears =+ i[3] #something is stopping this from adding up all the numbers: ref line 105
#print(sumyears)
#print(len(year_list))

avg = sumyears / len(year_list)
print()
print(f"For year: {input_year}")
print(f"{max_country} has the highest life expectancy of {max_years} years.")
print(f"{min_country} has the lowest life expectancy of {min_years} years.")
print(f"The average life expectancy was {avg} years.")
