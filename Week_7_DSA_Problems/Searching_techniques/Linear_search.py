def Linear_search(arr, srch_val):
    for i in range(len(arr)-1, 0, -1):
        if arr[i] == srch_val:
            return f"search value found at index: '{i}'"
    return "search value not present in list"
    
# print(Linear_search([[3,4,5,[3,4,]5,7], 5]))


# arr =  [1,2,[3,4,5]
def Binary_search(arr,srch_val):
    mid_index = len(arr)//2
    mid_val = arr[mid_index]
    left = arr[:mid_index]
    right = arr[mid_index:]
    if srch_val < mid_val:
        for i in range(len(left)):
            if left[i] == srch_val:
                return i
    else:
        if srch_val >= mid_val:
            for j in range(len(right)):
                if right[j] == srch_val:
                    return j + mid_index


# print(Binary_search([2,4,6,8,10,12], 2))
# print(Binary_search([2,4,6,8,10,12], 4))
# print(Binary_search([2,4,6,8,10,12], 6))
# print(Binary_search([2,4,6,8,10,12], 8))
# print(Binary_search([2,4,6,8,10,12], 10))
# print(Binary_search([2,4,6,8,10,12], 12))



def binarySearch(arr, srch_value):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left + right) // 2
        if srch_value == arr[mid]:
            return mid
        if srch_value < arr[mid]:
            right = mid-1
        else:
            left = mid+1
    return "invalid search"

print(binarySearch([3,4,5,6,7,8], 3))
print(binarySearch([3,4,5,6,7,8], 4))
print(binarySearch([3,4,5,6,7,8], 5))
print(binarySearch([3,4,5,6,7,8], 6))
print(binarySearch([3,4,5,6,7,8], 7))
# print(binarySearch([3,4,5,6,7,8], 8))





