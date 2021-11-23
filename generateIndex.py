import os
import pandas as pd
import random
import csv
## This python script creats a CSV file that generates random sequence for the indices used
## in Illuminia Sequencing. It createa a 10-base sequence that has the following features:
## It must be at least 3-position different from already used indices stored in the MatreyekLab_Illumina-Indices google sheet
## e.g. If ATCG is already used, then ATAT is not accepted, but AGTT is accepted
## It must not have 3 or more repeated continuous bases
## e.g. AAATGC is not accepted, not AATTCC is accepted
## Its first base cannot be G, i.e. only A, T, or C is accepted as the first base
## To use this script, download the google sheet MatreyekLab_Illumina - Indices.csv in csv format
## and put it in the same folder as this script, then modify the generateIndices(input) in the
## last line with the number of sequences you want to generate. It then create a csv containing
## both the forward and reverse indices that can be copied onto the online google sheet

# Set up the pathway where the csv file will be created
os.getcwd()
#os.chdir("/Users/tiena/OneDrive/Documents/Java,Pymol,Rproj/Codon-sequence-design")
#os.getcwd()

# The csv file contains all already used indices sequences
csv_file = 'MatreyekLab_Illumina - Indices.csv'

# Sheet ID
sheet_id = "1tL8aaCp6qqtRCn92cJBbG-F01Oz_p-MEdSQTFA_LfEQ"
r = "https://docs.google.com/spreadsheets/export?id={}&exportFormat=csv&gid=945877896".format(sheet_id)

# Select the row "index_seq_fwd" and load the data in the panda dataframe
# create a list alreadyUse[] that contains all the indices in the above row
# drop (delete) the first 11 rows which only have 8-base sequences
col_list = ["index_seq_fwd"]
#df = pd.read_csv("MatreyekLab_Illumina - Indices.csv", usecols=col_list)
df = pd.read_csv(r)
df = df.drop(range(0,12))
alreadyUse= []
for index, row in df.iterrows():
    alreadyUse.append(row["index_seq_fwd"])

# A method to generate the reverse index from an input forward index
def revIndices(fwdIndices):
    revIndex = ""
    for element in range(0, len(fwdIndices)):
        if fwdIndices[element] == "A": revIndex = revIndex + "T"
        if fwdIndices[element] == "T": revIndex = revIndex + "A"
        if fwdIndices[element] == "G": revIndex = revIndex + "C"
        if fwdIndices[element] == "C": revIndex = revIndex + "G"
    return revIndex

# A method that return True if the difference in position base of two compared indices
# is larger than or equal to 3, otherwise return False
def differenceByTwo(fwdIndex, usedIndex):
    difference = 0
    for element in range(0, len(fwdIndex)):
        if fwdIndex[element] != usedIndex[element]:
            difference = difference + 1
    if difference < 3:
        return False
    else:
        return True

# A method that return True if the index is not already used or the difference is less than 3
# Otherwise return False
def checkIfUsed(fwdIndex):
    for usedIndex in alreadyUse:
        if differenceByTwo(str(fwdIndex),str(usedIndex)) == False:
            return False
    return True

# A method that return True if the index does not have repeated continuous bases of 3 or more
# Otherwise return False
def checkIfRepeated(fwdIndex):
    for element in range(2, len(fwdIndex)):
        if (fwdIndex[element] == fwdIndex[element-1]) & (fwdIndex[element] == fwdIndex[element-2]):
            return False
    return True

# A method to generate the 10-bases forward index with the first index cannot be G
def fwdIndices():
    fwdIndex = random.choice(["A", "T", "C"])
    for element in range(0, 9):
        base = random.choice(["A", "T", "G", "C"])
        fwdIndex = fwdIndex + base
    return fwdIndex

# A method to generate the 10-bases forward index that satisfy all the conditions described above
def createFwdIndex():
    while True:
        fwdIndex = fwdIndices()
        if (checkIfRepeated(fwdIndex) == True) and (checkIfUsed(fwdIndex) == True):
            return fwdIndex

# A method to generate a csv file containing both the forward and reverse indices
def generateIndices(total):
    with open('generatedIndices.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Fwd Indices", "Rev Indices"])
        for aa in range(0, total):
            fwdIndex = createFwdIndex()
            revIndex = revIndices(str(fwdIndex))
            writer.writerow([str(fwdIndex), str(revIndex)])

# Modify the input to generate desired number of indices
# e.g. 20 means 20 forward and reverse indices are generated
generateIndices(4)
