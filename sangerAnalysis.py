## This python script takes in a phd.1 files from sanger sequencing data and output
## a csv file which extracted the average, median and total length of each sequence

## To use this script, go to bash terminal and change directory to this file, then
## type in 'python sangerAnalysis.py [directory]'
## For example, 'python sangerAnalysis.py C:/Users/tienanh/sangerphd' will output a csv file

import os
import csv
import sys
#os.getcwd()
#os.chdir("/Users/tiena/OneDrive/Documents/deleted/sangerphd")
#os.getcwd()
os.getcwd()
os.chdir(str(sys.argv[1]))
os.getcwd()

#directory = "/Users/tiena/OneDrive/Documents/deleted/sangerphd"
directory = str(sys.argv[1])

# A method to extract average of data
def average(lst):
    return sum(lst) / len(lst)

# A method to extract the data from the phd files
def extractScore(file):
    arrayScore = []
    file1 = open(file,"r")
    Lines = file1.readlines()
    for line in Lines:
        line.strip()
        try:
            if line[2].isnumeric() and not line[3].isnumeric():
                arrayScore.append(line[2])
            if line[2].isnumeric() and line[3].isnumeric():
                arrayScore.append(line[2] + line[3])
        except:
            pass
    for i in range(0, len(arrayScore)):
        arrayScore[i] = int(arrayScore[i])
    arrayScore.sort()
    return arrayScore

def createCSV():
    # Create the csv file and the name the columns
    with open('sangerData.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["File Name", "Average Score", "Median", "Length"])
        # Choose only phd file to be included
        for root, dirs, files in os.walk(directory, topdown=False):
            for filename in files:
                if filename.endswith("phd.1"):
                    getdata = extractScore(os.path.join(root, filename).replace("\\","/"))
                    mid = len(getdata) // 2
                    res = (getdata[mid] + getdata[~mid]) / 2
                    writer.writerow([str(filename), average(getdata), res, len(getdata)])

## Creating the CSV file
createCSV()


