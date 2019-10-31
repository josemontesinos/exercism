MAPPING = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}


def to_rna(dna_strand):
    return ''.join(MAPPING[nucleotid.upper()] for nucleotid in dna_strand)
