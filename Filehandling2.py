import os,time,sys
import csv
import shutil
import glob

from os import path

#4) Wap to convert the content of files in reverse order.

#5) Wap to convert each n every word in upper case in file
#FileUpperCase

with open("FileUpperCase", "r+b") as file:
    content = file.read()
    file.seek(0)
    file.write(content.upper())


#6) Find count of each and every word in file
fname = "File.txt"
no_line = 0
no_words = 0
no_char = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        print words
        no_line += 1
        no_words += len(words)
        no_char += len(line)


print no_line

print no_words

print no_char


#7) Wap to read csv file which contain following columns emp id, emp name, empsal, empdept
with open('EmployeeData.csv','rt') as infile:
    data = csv.reader(infile)
    for row in data:
        print row


#a) Find out the avg salary of ITdept
empsal_list = []
with open('EmployeeData.csv','rt') as infile:
    data = csv.reader(infile)
    for row in data:
        salary = row["empsal"]
        empsal_list.append(float(row["empsal"]))
avgSal = sum(empsal_list) / len(empsal_list)
print "avg of Salary:", avgSal

#8)Wap to accept directory name from user and remove if it is modify 30days older and if size is 100kb(use fun m10)

path = input("Enter Directory")
now = time.time()
if os.stat(path).st_mtime < now - 7 * 86400 and os.path.getsize(path)> 100:
    os.removedirs(path)


#Wap to find out count of all the python files in any specific directory and subdirectory
path = input("Enter Directory")
os.chdir(path)
for fileName in glob.glob("*.py"):
 print fileName.count()

# Wap to accept directory name from user and remove all the empty files, from that directory. (os.path.getsize)

path = input("Enter Directory")
for root, dirs, files in os.walk(path):
    for name in files:
        filename = os.path.join(root, name)
        if os.stat(filename).st_size == 0:
            print(" Removing ", filename)
            os.remove(filename)





