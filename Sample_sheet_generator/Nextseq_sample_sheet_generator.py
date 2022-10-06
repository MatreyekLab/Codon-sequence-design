import os
import pandas as pd
import numpy as np
import random
import csv
from numpy import savetxt

# A method to generate the reverse index from an input forward index
def revIndices(fwdIndices):
    revIndex = ""
    for element in range(0, len(fwdIndices)):
        if fwdIndices[element] == "A": revIndex = revIndex + "T"
        if fwdIndices[element] == "T": revIndex = revIndex + "A"
        if fwdIndices[element] == "G": revIndex = revIndex + "C"
        if fwdIndices[element] == "C": revIndex = revIndex + "G"
    revIndex2 = revIndex[::-1]
    return revIndex2

# Set up the pathway where the csv file will be created
os.getcwd()

# Import the google sheet listing what the indices are
r = "https://docs.google.com/spreadsheets/export?id=1tL8aaCp6qqtRCn92cJBbG-F01Oz_p-MEdSQTFA_LfEQ&exportFormat=csv&gid=945877896"

# Select the row "index_seq_fwd" and load the data in the panda dataframe
# create a list alreadyUse[] that contains all the indices in the above row
# drop (delete) the first 11 rows which only have 8-base sequences
col_list = ["index_seq_fwd"]
#df = pd.read_csv("MatreyekLab_Illumina - Indices.csv", usecols=col_list)
df = pd.read_csv(r)
df = df.drop(range(0,12))
primer = []
itype = []
primer_strand_index = []
primer_revcomp_index = []
for index, row in df.iterrows():
    primer.append(row["primer_name"])
    itype.append(row["type"])
    primer_strand_index.append(row["index_seq_fwd"])
    primer_revcomp_index.append(revIndices(row["index_seq_fwd"]))
    #alreadyUse.append(row["index_seq_rev"])
#print(alreadyUse)

#print(primer)
#print(primer_strand_index)
#print(primer_revcomp_index)


primer_df = pd.DataFrame(list(zip(primer, itype, primer_strand_index, primer_revcomp_index)),
               columns =["Primer_name", "type", "index_seq_fwd", "index_seq_rev"])
#print(primer_df)

samplegooglesheet_name = input("What is the NextSeq kit number?: ") #3
samplegooglesheet_sheet_id = input("What is the GID of the googlesheet?: ") #937771412
r2 = "https://docs.google.com/spreadsheets/export?id=1_JNV3crx33WMexKpFgCle54Ftxx1pqIQAT00_gy120U&exportFormat=csv&gid={}".format(samplegooglesheet_sheet_id)

df2 = pd.read_csv(r2)
#print(df2)

sample_name = []
p5_primer = []
p7_primer = []
volume_list = []
concentration_list = []
comments = []

for index, row in df2.iterrows():
    sample_name.append(row["num2"])
    temp_p5_primer = row["p5_primer"]
    p5_primer.append((primer_df.loc[primer_df['Primer_name'] == temp_p5_primer])["index_seq_rev"].values[0])
    temp_p7_primer = row["p7_primer"]
    p7_primer.append((primer_df.loc[primer_df['Primer_name'] == temp_p7_primer])["index_seq_rev"].values[0])
    volume_list.append(row["volume_given"])
    concentration_list.append(row["concentration"])
    comments.append("")

output_df = pd.DataFrame(list(zip(sample_name, p7_primer, p5_primer, volume_list, concentration_list, comments)),
               columns =["Sample Name", "i7 Index Barcode", "i5 Index Barcode", "Volume given", "Concentration", "Comments"])

output_df.to_csv("Nextseq"+samplegooglesheet_name+"_Output_samplesheet.csv", encoding='utf-8', index=False)
