import Bio
from Bio.Seq import Seq

snv_output_file = open("SNV_table.tsv", "w")
orf = "atgacagccatcatcaaagagatcgttagcagaaacaaaaggagatatcaagaggatggattcgacttagacttgacctatatttatccaaacattattgctatgggatttcctgcagaaagacttgaaggcgtatacaggaacaatattgatgatgtagtaaggtttttggattcaaagcataaaaaccattacaagatatacaatctttgtgctgaaagacattatgacaccgccaaatttaattgcagagttgcacaatatccttttgaagaccataacccaccacagctagaacttatcaaacccttttgtgaagatcttgaccaatggctaagtgaagatgacaatcatgttgcagcaattcactgtaaagctggaaagggacgaactggtgtaatgatatgtgcatatttattacatcggggcaaatttttaaaggcacaagaggccctagatttctatggggaagtaaggaccagagacaaaaagggagtaactattcccagtcagaggcgctatgtgtattattatagctacctgttaaagaatcatctggattatagaccagtggcactgttgtttcacaagatgatgtttgaaactattccaatgttcagtggcggaacttgcaatcctcagtttgtggtctgccagctaaaggtgaagatatattcctccaattcaggacccacacgacgggaagacaagttcatgtactttgagttccctcagccgttacctgtgtgtggtgatatcaaagtagagttcttccacaaacagaacaagatgctaaaaaaggacaaaatgtttcacttttgggtaaatacattcttcataccaggaccagaggaaacctcagaaaaagtagaaaatggaagtctatgtgatcaagaaatcgatagcatttgcagtatagagcgtgcagataatgacaaggaatatctagtacttactttaacaaaaaatgatcttgacaaagcaaataaagacaaagccaaccgatacttttctccaaattttaaggtgaagctgtacttcacaaaaacagtagaggagccgtcaaatccagaggctagcagttcaacttctgtaacaccagatgttagtgacaatgaacctgatcattatagatattctgacaccactgactctgatccagagaatgaaccttttgatgaagatcagcatacacaaattacaaaagtc".upper()

#print(orf[len(orf)-3:len(orf)])
if(orf[len(orf)-3:len(orf)] in ["TAG","TGA","TAA"]):
	orf = orf[:len(orf)-3]
	#print(orf)

snv_output_file.write("%s\t%s\t%s\t%s\t%s\t%s\n" % ("position","codon","start","end","variant","class"))

def get_snv():
	output_position = x + 1
	output_codon = temp_codon
	output_start_aa = str(Seq(codon).translate())
	if str(Seq(temp_codon).translate()) == "*":
		output_end_aa = "X"
	else:
		output_end_aa = str(Seq(temp_codon).translate())
	output_variant = output_start_aa + str(output_position) + str(output_end_aa)
	if output_end_aa == "X":
		output_variant_type = "nonsense"
	elif output_start_aa == output_end_aa:
		if temp_codon ==  codon:
			output_variant_type = "wildtype"
		else:
			output_variant_type = "synonymous"
	else:
		output_variant_type = "missense"
	snv_output_file.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (output_position,output_codon,output_start_aa,output_end_aa,output_variant,output_variant_type))


dna_len = len(orf)
protein_len = int(dna_len/3)

position_list = []
codon_list = []
start_aa_list = []
end_aa_list = []
variant_list = []
variant_type_list = []

mutation_list = ["A","C","G","T"]

for x in range(1,protein_len):
	codon = orf[(x * 3):(x * 3 + 3)]
	for y in range(0,len(mutation_list)):
		temp_codon = mutation_list[y]+codon[1:3]
		get_snv()
	for y in range(0,4):
		temp_codon = codon[0]+mutation_list[y]+codon[2]
		get_snv()
	for y in range(0,4):
		temp_codon = codon[0:2]+mutation_list[y]
		get_snv()

snv_output_file.close()