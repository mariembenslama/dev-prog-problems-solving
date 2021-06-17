def findPythagoreanTriplets(nums):
    squares = set([n * n for n in nums])
    for a in nums:
        for b in nums:
            if (a * a + b * b) in squares:
                return True
    
    return False

print(findPythagoreanTriplets([3, 5, 12, 5, 13]))
print(findPythagoreanTriplets([3, 5, 17, 5, 13]))