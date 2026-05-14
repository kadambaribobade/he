# Selection Sort using Greedy Method with User Input
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print("Original Array:")
print(arr)
for i in range(n):
    min_index = i
    for j in range(i+1, n):  
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Pass", i+1, ":", arr)
print("Sorted Array:")
print(arr)
