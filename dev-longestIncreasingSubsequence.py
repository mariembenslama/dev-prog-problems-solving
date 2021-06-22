def devlongestIncreasingSubsequence(arr):
    if(not arr):
        return 0
    
    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if(arr[i] > arr[j]):
                cache[i] = max(cache[i], cache[j] + 1)
        
    print(cache)
    print(max(cache))

#change here
devlongestIncreasingSubsequence([1,2,5,4,3,6])