# selection sort

toSort = [2, 9, 7, 11, 23, 4, 5, 69, 44, 234, 3222, 3, 7]
toSort2 = [2, 9, 7, 11, 23, 4, 5, 69, 44, 234, 3222, 3, 7]


def swap(l, x, y):
    tmp = l[x]
    l[x] = l[y]
    l[y] = tmp

def selectionSort(l):
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            if(l[i] > l[j]):
                swap(l, i, j)

selectionSort(toSort)
print(toSort)


def merge(l1, l2):
    mergedArr = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if(l1[i] <= l2[j]):
            mergedArr.append(l1[i])
            i += 1
        else:
            mergedArr.append(l2[j])
            j += 1
    mergedArr.extend(l1[i:])
    mergedArr.extend(l2[j:])
    return mergedArr
    
def mergeSort(l):
    if(len(l) <= 1):
        return l
    
    mid = len(l) // 2
    leftHalf = mergeSort(l[:mid])
    rightHalf = mergeSort(l[mid:])
    
    return merge(leftHalf, rightHalf)
    

toSort2 = mergeSort(toSort2)
print(toSort2)