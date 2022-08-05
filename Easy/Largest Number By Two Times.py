def solve(self, nums):
    answer = False
    a = nums.pop(nums.index(max(nums)))
    b = nums.pop(nums.index(max(nums)))
    if a > 2*b:
        answer = True

    return answer