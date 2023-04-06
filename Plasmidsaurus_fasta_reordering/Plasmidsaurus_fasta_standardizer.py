## This will reorder your fasta file so that the junction between the stop codon of AmpR will be at the breakpoint of the sequence
## To run the script, type in "python3 Plasmidsaurus_fasta_standardizer.py", but also drag the file that you want to reorder into the terminal so the actual command ends up being something like "python3 Plasmidsaurus_fasta_standardizer.py /Users/kmatreyek/Library/CloudStorage/GoogleDrive-kmatreyek@gmail.com/My\ Drive/_MatreyekLab/Data/Plasmidsaurus/PSRS033/Matreyek_f6f_results/Matreyek_f6f_1_G1118A.fasta



import sys
import codecs

file_name = sys.argv[1]

outfilename = file_name[0:len(file_name)-6]+"_reordered.fasta"
outfile = codecs.open(outfilename, "w", "utf-8", "replace")

counter = 1
with open(file_name, 'r') as datafile:
	for line in datafile:
		#print(line)
		print("Assessing line number: " + str(counter))
		if counter == 1:
			header = line
			counter = 2
			continue
		if counter == 2:
			if line.find("TTACCAATGCTTAATCAGTG") != -1:
				print("The fasta file is in the fwd orientation")
				temp_index = line.find("TTACCAATGCTTAATCAGTG")
				reordered_seq = ((line[temp_index:len(line)] + line[0:temp_index]).replace("\n",""))
			if line.find("TTACCAATGCTTAATCAGTG") == -1:
				print("The fasta file is in the rev orientation")
			if line.find("CTGTCAGACCAAGTTTACTC") != -1:
				temp_index = line.find("CTGTCAGACCAAGTTTACTC")
				reordered_seq = ((line[temp_index:len(line)] + line[0:temp_index]).replace("\n",""))
			break

outfile.write(header)
outfile.write(reordered_seq)
outfile.close()