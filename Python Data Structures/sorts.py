# selection sort

toSort = [2, 9, 7, 11, 23, 4, 5, 69, 44, 234, 3222, 3, 7]

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


# insertion sort

def insert(l, x, y):
    assert(y < x)
    tmp = l[x]
    for i in range(x, y, -1):
        l[i] = l[i - 1]
    l[y] = tmp
    
def insertionSort(l):
    