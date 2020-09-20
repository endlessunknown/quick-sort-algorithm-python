def quick_sort(sequence):
    if len(sequence)<=1:
        return sequence
    else:
        pivot=sequence.pop()

    items_greater=[]
    items_smaller=[]

    for i in range(len(sequence)):
        if sequence[i]>pivot:
            items_greater.append(sequence[i])
        else:
            items_smaller.append(sequence[i])
    
    return quick_sort(items_smaller)+[pivot]+quick_sort(items_greater)


print("Enter Elements : ",end="")
a=list(map(int,input().split(" ")))
print("Sorted Elemnts : ",end="")
print(quick_sort(a))