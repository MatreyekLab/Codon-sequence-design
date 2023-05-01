import sys
import codecs

file_name = sys.argv[1]

outfilename = file_name[0:len(file_name)-6]+"_reordered.fasta"
outfile = codecs.open(outfilename, "w", "utf-8", "replace")

tempseq = ""
counter = 1
with open(file_name, 'r') as datafile:
	for line in datafile:
		if counter == 1:
			header = line
			counter = 2
			continue
		if counter == 2:
			tempseq = tempseq + line
if tempseq.find("TTACCAATGCTTAATCAGTG") != -1:
	print("The fasta file is Amp in the fwd orientation")
	temp_index = tempseq.find("TTACCAATGCTTAATCAGTG")
	reordered_seq = ((tempseq[temp_index:len(tempseq)] + tempseq[0:temp_index]).replace("\n",""))
if tempseq.find("CTGTCAGACCAAGTTTACTC") != -1:
	print("The fasta file is Amp in the rev orientation")
	temp_index = tempseq.find("CTGTCAGACCAAGTTTACTC")
	print(temp_index)
	reordered_seq = ((tempseq[temp_index:len(tempseq)] + tempseq[0:temp_index]).replace("\n",""))
if tempseq.find("GCGGGACTCTGGGGTTCGAA") != -1:
	print("The fasta file is Kan in the fwd orientation")
	temp_index = tempseq.find("GCGGGACTCTGGGGTTCGAA")
	reordered_seq = ((tempseq[temp_index:len(tempseq)] + tempseq[0:temp_index]).replace("\n",""))
if tempseq.find("TCAGAAGAACTCGTCAAGAA") != -1:
	print("The fasta file is Kan in the rev orientation")
	temp_index = tempseq.find("TCAGAAGAACTCGTCAAGAA")
	print(temp_index)
	reordered_seq = ((tempseq[temp_index:len(tempseq)] + tempseq[0:temp_index]).replace("\n",""))

outfile.write(header)
outfile.write(reordered_seq)
outfile.close()