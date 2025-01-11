#-- 🍃🍀
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

arr = [2, 3, 4, 5, 7, 9, 12, 16, 22, 28, 38, 50, 66, 88, 116, 154, ]
x = 88
print(binary_search(arr, x)-1)

#-- written by Pratham 🍂🍁 