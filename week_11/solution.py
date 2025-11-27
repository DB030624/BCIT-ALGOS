def cheat_sort(seq):
    seq.sort()

def cheat_merge(left, right):
    return sorted(left + right)


def merge(left,right):

    sort = []
    l, r = 0,0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sort.append(left[l])
            l += 1
        else:
            sort.append(right[r])
            r += 1
        
    sort.extend(left[l:])
    sort.extend(right[r:])

    return sort





def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    
    left = merge_sort(seq[:len(seq)//2])
    right = merge_sort(seq[len(seq)//2:])

    seq[:] = merge(left,right)
    return seq




    

    


