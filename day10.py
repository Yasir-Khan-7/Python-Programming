import os
os.mkdir("data")#it will make a folder name data

# now if i want to make 100 days of file in a folder name 'data'

for x in range(0,100):# this will create 100 folders with day 1 ,day 2 etc
    os.mkdir(f"data/day{x+1}")
    
# if you want to rename the folders use rename()

for i in range(0,100):
    os.rename(f"data/day{i+1}",f"data/tutorial{i+1}") #first source and then destination
    
if not os.path.exists("data"):# twhen we want to check whether this already exists or not
    for x in range(0,100):# this will create 100 folders with day 1 ,day 2 etc
        os.mkdir(f"data/day{x+1}")

#now if you want to check how many folder you have 

folder = os.listdir("data")
for folder in folder:
    print(folder)
    print(os.listdir(f"data/{folder}"))
    
#if you want to see your current working directory
print(os.getcwd())

#if you want to change your current working directory
os.chdir(r"C:\Users\Administrator\Desktop\Coding")
print(os.getcwd())