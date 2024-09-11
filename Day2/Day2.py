class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    arr.append(i)
                    arr.append(j)
                    break
        return arr


# Or.. Another solution can be:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        last_ele = len(nums) - 1
        for i in range(0, len(nums)):
            for j in range(last_ele, i, -1):
                if nums[i] + nums[j] == target:
                    print(i, j)
                    lst.append(i)
                    lst.append(j)
        return lst
