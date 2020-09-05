from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        print("Input: nums = %s, target = %s" % (nums, target))
        for value in nums:
            another = target - value
            i = nums.index(value)
            if another in nums:
                if another != value:
                    output = [i, nums.index(another)]
                elif another == value:
                    nums_m = nums[i+1:]
                    if another in nums_m:
                        output = [i, i+1+nums_m.index(another)]
                    else:
                        continue
                else:
                    print("There is not valid values.")
                    output = []

        print("Output: %s" % output)
        return output


example = Solution()
outlist = example.twoSum([3, 2, 4], 6)