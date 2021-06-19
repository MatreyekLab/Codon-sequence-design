## This python codes take in a sequence of DNA and returns a different sequence
# but still codes for the same amino acids utilizing the degeneracy of DNA

## To use this script, go to bash terminal and change directory to this file, then
## type in 'python designCodon.py [sequence]'
## For example, 'python designCodon.py GACGAAAAG' will print out 'GATGAGAAA'

import sys

sequence = str(sys.argv[1]).upper()

def F(aa):
    if aa == 'TTT': return 'TTC'
    if aa == 'TTC': return 'TTT'

def L(aa):
    if aa == 'TTA': return 'CTG'
    if aa == 'TTG': return 'CTC'
    if aa == 'CTT': return 'CTG'
    if aa == 'CTC': return 'TTA'
    if aa == 'CTA': return 'TTG'
    if aa == 'CTG': return 'TTA'


def I(aa):
    if aa == 'ATT': return 'ATC'
    if aa == 'ATC': return 'ATT'
    if aa == 'ATA': return 'ATC'


def M(aa):
    return 'ATG'


def V(aa):
    if aa == 'GTT': return 'GTG'
    if aa == 'GTC': return 'GTC'
    if aa == 'GTA': return 'GTC'
    if aa == 'GTG': return 'GTC'


def S(aa):
    if aa == 'TCT': return 'AGC'
    if aa == 'TCC': return 'AGC'
    if aa == 'TCA': return 'AGC'
    if aa == 'TCG': return 'AGC'
    if aa == 'AGT': return 'TCC'
    if aa == 'AGC': return 'TCC'


def P(aa):
    if aa == 'CCT': return 'CCC'
    if aa == 'CCC': return 'CCA'
    if aa == 'CCA': return 'CCC'
    if aa == 'CCG': return 'CCC'


def T(aa):
    if aa == 'AGT': return 'ACC'
    if aa == 'ACC': return 'AGT'
    if aa == 'ACA': return 'AGT'
    if aa == 'ACG': return 'AGT'


def A(aa):
    if aa == 'GCT': return 'GCC'
    if aa == 'GCC': return 'GCT'
    if aa == 'GCA': return 'GCC'
    if aa == 'GCG': return 'GCC'


def Y(aa):
    if aa == 'TAT': return 'TAC'
    if aa == 'TAC': return 'TAT'


def H(aa):
    if aa == 'CAT': return 'CAC'
    if aa == 'CAC': return 'CAT'


def Q(aa):
    if aa == 'CAA': return 'CAG'
    if aa == 'CAG': return 'CAA'


def N(aa):
    if aa == 'AAT': return 'AAC'
    if aa == 'AAC': return 'AAT'


def K(aa):
    if aa == 'AAA': return 'AAG'
    if aa == 'AAG': return 'AAA'


def D(aa):
    if aa == 'GAT': return 'GAC'
    if aa == 'GAC': return 'GAT'


def E(aa):
    if aa == 'GAA': return 'GAG'
    if aa == 'GAG': return 'GAA'


def C(aa):
    if aa == 'TGT': return 'TGC'
    if aa == 'TGC': return 'TGT'


def W(aa):
    return 'TGG'


def R(aa):
    if aa == 'CGT': return 'AGA'
    if aa == 'CGC': return 'AGA'
    if aa == 'CGA': return 'AGA'
    if aa == 'CGG': return 'AGA'
    if aa == 'AGA': return 'CGC'
    if aa == 'AGG': return 'CGC'


def G(aa):
    if aa == 'GGT': return 'GGC'
    if aa == 'GGC': return 'GGA'
    if aa == 'GGA': return 'GGC'
    if aa == 'GGG': return 'GGC'


def design(dna):
    arrayDNA = []
    newSequence = ''
    for i in range(0, len(dna) - 1):
        if i % 3 == 0:
            arrayDNA.append(dna[i:i + 3])
    for codon in arrayDNA:
        if codon == 'TTT' or codon == 'TTC':
            newSequence = newSequence + F(codon)
        if codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTC' or codon == 'CTA' or codon == 'CTG':
            newSequence = newSequence + L(codon)
        if codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
            newSequence = newSequence + I(codon)
        if codon == 'ATG':
            newSequence = newSequence + M(codon)
        if codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
            newSequence = newSequence + V(codon)
        if codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG' or codon == 'AGT' or codon == 'AGC':
            newSequence = newSequence + S(codon)
        if codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
            newSequence = newSequence + P(codon)
        if codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
            newSequence = newSequence + T(codon)
        if codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
            newSequence = newSequence + A(codon)
        if codon == 'TAT' or codon == 'TAC':
            newSequence = newSequence + Y(codon)
        if codon == 'CAT' or codon == 'CAC':
            newSequence = newSequence + H(codon)
        if codon == 'CAA' or codon == 'CAG':
            newSequence = newSequence + Q(codon)
        if codon == 'AAT' or codon == 'AAC':
            newSequence = newSequence + N(codon)
        if codon == 'AAA' or codon == 'AAG':
            newSequence = newSequence + K(codon)
        if codon == 'GAT' or codon == 'GAC':
            newSequence = newSequence + D(codon)
        if codon == 'GAA' or codon == 'GAG':
            newSequence = newSequence + E(codon)
        if codon == 'TGT' or codon == 'TGC':
            newSequence = newSequence + C(codon)
        if codon == 'TGG':
            newSequence = newSequence + W(codon)
        if codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
            newSequence = newSequence + R(codon)
        if codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
            newSequence = newSequence + G(codon)
    return newSequence


print(design(sequence))

