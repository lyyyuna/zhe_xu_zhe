# heapify the size of the subtree index
def heapify(arr, size, index):
    largetIndex = index
    leftChild = index * 2 + 1
    rightChild = index * 2 + 2

    if leftChild < size and arr[leftChild] > arr[index]:
        largetIndex = leftChild

    if rightChild < size and arr[largetIndex] < arr[rightChild]:
        largetIndex = rightChild

    if largetIndex != index:
        arr[index], arr[largetIndex] = arr[largetIndex], arr[index]

        heapify(arr, size, largetIndex)

     

def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 