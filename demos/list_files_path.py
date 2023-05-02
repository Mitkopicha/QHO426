import os
# go in with one dot ./
# go out with two dots ../
path = os.getcwd()
os.chdir('./demos/')
print(f"My path is {path}")
# go into the folder and list every file
for file in os.listdir(path):
    print(file)