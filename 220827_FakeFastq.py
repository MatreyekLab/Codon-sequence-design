import sys
import codecs

file_name = sys.argv[1]

outfilename = file_name[0:len(file_name)-4]+".fastq"
outfile = codecs.open(outfilename, "w", "utf-8", "replace")

counter = 1
with open(file_name, 'r') as datafile:
	for line in datafile:
		line_len = len(line)
		if counter == 1:
			outfile.write("@GWNJ-1013_{}\n{}{}\n{}".format(counter,line,"+","F"*(line_len-1)))
		if counter != 1:
			outfile.write("\n@GWNJ-1013_{}\n{}{}\n{}".format(counter,line,"+","F"*(line_len-1)))
		counter = counter + 1
outfile.close()
