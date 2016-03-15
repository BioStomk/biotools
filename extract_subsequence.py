#!/usr/bin/env python

# --.py fasta begin end

import sys
import os
import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

parser = argparse.ArgumentParser()

parser.add_argument('seq_file')
parser.add_argument('bgn', type=int)
parser.add_argument('end', type=int)
parser.add_argument('-p', '--prefix')

args = parser.parse_args()
seq_file = args.seq_file
bgn = args.bgn
end = args.end
prefix = args.prefix

read = SeqIO.read(seq_file, 'fasta')
prefix = prefix if prefix else read.id
subseq = SeqRecord(read.seq[bgn:end], id=(prefix + '_' + str(bgn) + '_' + str(end)), description='')

SeqIO.write(subseq, subseq.id + '.fa', 'fasta')


