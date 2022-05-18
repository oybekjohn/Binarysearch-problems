# Leetcode
* [Easy](#easy)
* [Medium](#medium)
* [Hard](#hard)

## Easy
- 1389 Create Target Array in the Given Order

```python3
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        new_list = []
        
        for i in range(len(index)):
            new_list.insert(index[i], nums[i])
            
        return new_list
```
### --------------------------------------------------------------------------------------------------------
- 1 Two Sum

```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = {}
        for i in range(len(nums)):
            if (target - nums[i]) in complement:
                return [i, complement.get(target - nums[i])]
            else:
                complement[nums[i]] = i
```
### --------------------------------------------------------------------------------------------------------



## Medium




## Hard
