def linear_search(needle, haystack):
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i
    return None

        
def binary_search(needle, haystack):
    l = 0
    haystack = sorted(haystack)
    r = len(haystack) - 1

    while l <= r:
        mid = (l + r) // 2
        if haystack[mid] == needle:
            return mid
        elif haystack[mid] < needle:
            l = mid + 1
        else:
            r = mid - 1
    return None


print(linear_search(8, [6, 2, 8, 4])) 
print(linear_search(4, [6, 2, 8, 4])) 
print(linear_search(5, [6, 2, 8, 4]))  

print(binary_search(8, [2, 4, 6, 8]))  
print(binary_search(2, [2, 4, 6, 8]))  
print(binary_search(1, [2, 4, 6, 8]))  
print(binary_search(99, [2, 4, 6, 8])) 


def linear_search_multi(needle, haystack):
    indexes = []
    for i in range(len(haystack)):
        if needle == haystack[i]:
            indexes.append(i)
    return indexes


def linear_seach_binary_multi(needle,haystack):
    indexes = []
    l = 0
    r = len(haystack) - 1
    while l <= r:
        mid = (r + l) // 2
        if haystack[mid] == needle:
            indexes.append(mid)

            i = mid - 1
            while i >= 0 and haystack[i] == needle:
                indexes.append(i)

                i-= 1
            
            i = mid + 1
            while i <= len(haystack) - 1 and haystack[i] == needle:
                indexes.append(i)
                i+= 1
            return sorted(indexes)
        elif haystack[mid] < needle:
            l = mid + 1
        else:
            r = mid - 1


    return indexes




