def cheat_sort(seq):
    seq.sort()

def cheat_merge(left, right):
    return sorted(left + right)


def merge(left,right):
    l = r = 0 
    res = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    
    res.extend(left[l:])
    res.extend(right[r:])

    return res

def merge_sort(unsorted_list):

    def _recursive_sort(splice_unsorted_list):

        if (len(splice_unsorted_list) <= 1):
            return splice_unsorted_list
        
        mid = len(splice_unsorted_list) // 2
        list_one = _recursive_sort(splice_unsorted_list[:mid])
        list_two = _recursive_sort(splice_unsorted_list[mid:])

        return merge(list_one,list_two)
    
    sorted_res = _recursive_sort(unsorted_list)

    unsorted_list[:] = sorted_res
    
    

    


