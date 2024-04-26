def  heapify(arr , n ,i):
    left = i * 2 + 1
    right = i * 2 + 2
    largest = i
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if i != largest:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        heapify(arr , n , largest)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 -1 , -1 , -1 ):
        heapify(arr , n , i)
    
    for i in range(n - 1 , 0, -1):
        arr[0] , arr[i] = arr[i] ,arr[0]
        heapify(arr, i  , 0)

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("排序后")
for i in range(n):
    print(arr[i])