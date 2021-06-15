import os
import pandas as pd
import random
import csv

os.getcwd()
os.chdir("/Users/tiena/OneDrive/Documents/Java,Pymol,Rproj/Codon-sequence-design")
os.getcwd()

csv_file = 'MatreyekLab_Illumina - Indices.csv'

col_list = ["index_seq_fwd"]
df = pd.read_csv("MatreyekLab_Illumina - Indices.csv", usecols=col_list)
df = df.drop(range(0,12))
alreadyUse= []
for index, row in df.iterrows():
    alreadyUse.append(row["index_seq_fwd"])

def revIndices(fwdIndices):
    revIndex = ""
    for element in range(0, len(fwdIndices)):
        if fwdIndices[element] == "A": revIndex = revIndex + "T"
        if fwdIndices[element] == "T": revIndex = revIndex + "A"
        if fwdIndices[element] == "G": revIndex = revIndex + "C"
        if fwdIndices[element] == "C": revIndex = revIndex + "G"
    return revIndex

def differenceByTwo(fwdIndex, usedIndex):
    difference = 0
    for element in range(0, len(fwdIndex)):
        if fwdIndex[element] != usedIndex[element]:
            difference = difference + 1
    if difference < 3:
        return False
    else:
        return True

def checkIfUsed(fwdIndex):
    for usedIndex in alreadyUse:
        if differenceByTwo(str(fwdIndex),str(usedIndex)) == False:
            return False
    return True

def checkIfRepeated(fwdIndex):
    for element in range(2, len(fwdIndex)):
        if (fwdIndex[element] == fwdIndex[element-1]) & (fwdIndex[element] == fwdIndex[element-2]):
            return False
    return True

def fwdIndices():
    fwdIndex = random.choice(["A", "T", "C"])
    for element in range(0, 9):
        base = random.choice(["A", "T", "G", "C"])
        fwdIndex = fwdIndex + base
    return fwdIndex

def createFwdIndex():
    while True:
        fwdIndex = fwdIndices()
        if (checkIfRepeated(fwdIndex) == True) & (checkIfUsed(fwdIndex) == True):
            return fwdIndex

def generateIndices(total):
    with open('generatedIndices.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Fwd Indices", "Rev Indices"])
        for aa in range(0, total):
            fwdIndex = createFwdIndex()
            revIndex = revIndices(str(fwdIndex))
            writer.writerow([str(fwdIndex), str(revIndex)])

generateIndices(20)
