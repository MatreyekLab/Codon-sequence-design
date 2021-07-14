import os
import csv

def createIndices(row,column):
    row_array = list(range(1, row+1))
    col_array = list(range(1, column+1))
    count = 0
    with open('Nihdi_Indices.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Order","Indices"])
        for row_number in range(0, len(row_array)):
            index = str(row_array[row_number])
            for col_number in range(0, len(col_array)):
                index = index + "," + str(col_array[col_number])
                count = count + 1
                writer.writerow([str(count), str(index)])
                index = str(row_array[row_number])

createIndices(6,12)