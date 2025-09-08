def linear_search(needle,haystack):
    for i in haystack:
        if i == needle:
            return True
        else:
            return False
        
def binary_search(needle,haystack):
    l = 0
    r = len(haystack) - 1
    haystack = sorted(haystack)
    while l <= r:
        mid = (l + r) // 2

        if haystack[mid] == needle:
            return True
        elif haystack[mid] < needle:
            l = mid + 1
        else:
            r = mid - 1
    return False



        
