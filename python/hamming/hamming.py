def distance(strand_a, strand_b):
    hamming = 0
    if len(strand_a) != len(strand_b):
        raise ValueError('Both strands must have equal length!')
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hamming += 1
    return hamming
