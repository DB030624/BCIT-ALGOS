def bubble_sort(seq):
    for j in range(len(seq) - 1, 0, -1):
        for i in range(0, j):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]


def selection_sort(seq):
    
    for i in range(len(seq)):
        
        curr_min = i

        for j in range(i + 1 , len(seq)):
            if seq[j] <  seq[curr_min]:
                curr_min = j

        if curr_min != i:
            seq[i], seq[curr_min] = seq[curr_min], seq[i]

    

def insertion_sort(seq):

    for i in range(1,len(seq)):
        j = i

        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]

            j = j -1


    
    
        
            



