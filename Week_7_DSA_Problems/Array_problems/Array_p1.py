def two_sum(arr, target):
    two_sum_list = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                two_sum_list.append((i,j))
    return two_sum_list      
print(two_sum([1,2,3,4,5,6], 9))



