def pivot_naive(seq):
    return seq[-1]




def partition_naive(seq, pivot):
    
    lo,pivots,hi = [],[],[] 

    for i in range(len(seq)):
        if seq[i] < pivot:
            lo.append(seq[i])
        elif seq[i] == pivot:
            pivots.append(seq[i])
        else:
            hi.append(seq[i])
    return [lo,pivots,hi]

def quicksort_naive(seq):

    if len(seq) <= 1:
        return seq
    
    pivot = pivot_naive(seq)
    [lo,pivots,hi] = partition_naive(seq,pivot)

    quicksort_naive(lo)
    quicksort_naive(hi)
    seq[:] = lo + pivots+hi 






def pivot_upgrade(seq, lo, hi):
    pivot = (lo + hi) // 2
    return seq[pivot]


def quicksort_upgrade(seq):
    __quicksort_upgrade(seq, 0, len(seq))



def __quicksort_upgrade(seq, lo, hi):
    if hi - lo <= 1:
        return 
    
    pivot = pivot_upgrade(seq,lo,hi)

    len_lo, len_eq, len_hi = partition_upgrade(seq,pivot,lo, hi)

    __quicksort_upgrade(seq,lo, lo + len_lo)
    __quicksort_upgrade(seq, lo + len_lo + len_eq, hi)

'''def partition_upgrade(seq, pivot, lo, hi):
    [one, two, three] = partition_naive(seq[lo:hi], pivot)
    seq[lo:hi] = one + two + three
    return [len(one), len(two), len(three)]'''


def partition_upgrade(seq, pivot, lo, hi):
    writer = lo

    for i in range(lo,hi):
        if seq[i] < pivot:
            seq[i] , seq[writer] = seq[writer], seq[i]

            writer += 1
    
    len_lo = writer - lo

    starter_eq = writer
    for i in range(writer,hi):
        if seq[i] == pivot:
            seq[i] , seq[writer] = seq[writer],seq[i]
            writer += 1
    
    len_eq = writer - starter_eq
    len_hi = hi - writer

    return [len_lo,len_eq,len_hi]
        








