mylist = [22,70,46,33,19,77,80,90,111,245]
import math


# Bubble sort
def bubble_sort(mylist):
    for i in range(len(mylist)-1):
        for j in range(len(mylist)-1):
            if mylist[j] > mylist[j+1]:
                mylist[j] , mylist[j+1] = mylist[j+1] , mylist[j]
    return mylist

# print(bubble_sort(mylist))

# Selection sort
def selection_sort(mylist):
    for i in range(len(mylist)):
        min_index = i
        for j in range(i+1 , len(mylist)):
            if mylist[min_index] > mylist[j]:
                min_index = j
        mylist[i] , mylist[min_index] = mylist[min_index] , mylist[i]
    return mylist

# print(selection_sort(mylist))


# Insertion sort
def insertion_sort(mylist):
    for i in range(1 , len(mylist)):
        j = i
        while mylist[j-1] > mylist[j] and  j > 0:
            mylist[j-1] , mylist[j] = mylist[j] , mylist[j-1]
            j = j-1
    return mylist

# print(insertion_sort(mylist))



# Bucket sort
def bucket_sort(mylist):
    numberOfBucketSort = round(math.sqrt(len(mylist))) #import math
    max_value = max(mylist)

    arr = []

    for i in range(numberOfBucketSort):
        arr.append([])

    for j in mylist:
        index = math.ceil(j * numberOfBucketSort / max_value)
        arr[index-1].append(j)

    for i in range(numberOfBucketSort):
        arr[i] = insertion_sort(arr[i])

    combined_list = [item for sublist in arr for item in sublist]
    return combined_list

# print(bubble_sort(mylist))




# Merge sort
def merge_two_list(left, right):
    new = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    new.extend(left[i:])
    new.extend(right[j:])
    return new
def merge_sort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        return merge_two_list(left, right)
    else:
        return mylist
    
# print(merge_sort(mylist))




# Quick sort
def quick_sort(mylist):
    if len(mylist) <= 1:
        return mylist
    else:
        pivot = mylist.pop()

        left = []
        right = []

        for item in mylist:
            if item < pivot:
                left.append(item)
            else:
                right.append(item)
        
        return quick_sort(left) + [pivot] + quick_sort(right)
    
print(quick_sort(mylist))
