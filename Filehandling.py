import os
from os import path


#Assignments on File Handling


#1) Wap to accept a file name and directory name from user and create a backup of this file in same directory

filename=raw_input("Enter filename")
Directoryname=raw_input("Enter directory name")

if path.exists(filename):
    # get the path to the file in the current directory
    src = path.realpath(filename);
    print src

    # rename the original file
    os.rename(filename+'.bak', filename
              )




#3) Wap to find out total no of lines total no of words total no of characters in file

fname = "File.txt"
no_line = 0
no_words = 0
no_char = 0

with open(fname,'r') as f:
    for line in f:
        words = line.split()
        print words
        no_line += 1
        no_words += len(words)
        no_char += len(line)


print no_line

print no_words

print no_char

