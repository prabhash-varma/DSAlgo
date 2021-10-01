def insertion_sort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = [12, -11, -8, -9, 100, 68, 67, -3, 88, -13, 5, 6]

print("Original array is:")
for i in range(len(arr)):
    print(arr[i], end=" ")

insertion_sort(arr)

print("\nSorted array is:")
for i in range(len(arr)):
    print(arr[i], end=" ")
