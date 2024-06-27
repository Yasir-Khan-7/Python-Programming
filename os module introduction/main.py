import os
os.mkdir("data")#it will make a folder name data

#now if i want to make 100 days of file in a folder name 'data'

for x in range(0,100):
    os.mkdir(f"data/day{x+1}")