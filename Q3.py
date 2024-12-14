def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return 0
if __name__ == '__main__':
    arr = [2,5,8,12,16,23,38,56,72,91]
    x=int(input('Enter integer to search:'))
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != 0:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
