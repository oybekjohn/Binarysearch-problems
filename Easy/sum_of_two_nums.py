def solve(nums, k):
    """ the class calculate that k equal with sum of two list elements """
    t = []
    for i in nums:
        for j in nums[nums.index(i)+1:]:
            if k==(i+j):
                t.append(k)
    
    if len(t)==0:
        return False
    else:
        return True


numbers = [11, 2, 5, 8, 10]
k=13

print(solve(numbers, k))