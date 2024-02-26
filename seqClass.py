# This package takes as input a sequence and classifies it as DNA or RNA.

# Moreover, it given a determinate motif, it checks if it is found or not in the sequence.


import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description='Compute the percentage of each nucleotide in a DNA or RNA sequence')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()

if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq): 
        print('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T', args.seq): 
        print('The sequence is RNA')
    else:
        print('The sequence can be DNA or RNA')
    
    # Calcular el porcentaje de cada nucleótido
    total_length = len(args.seq)
    nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'U': 0}
    
    # Contar la cantidad de cada nucleótido en la secuencia
    for nucleotide in args.seq:
        nucleotide_counts[nucleotide] += 1
    
    # Calcular el porcentaje de cada nucleótido
    print("Percentage of each nucleotide:")
    for nucleotide, count in nucleotide_counts.items():
        percentage = (count / total_length) * 100
        print(f"{nucleotide}: {percentage:.2f}%")
else:
    print('The sequence is not DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
