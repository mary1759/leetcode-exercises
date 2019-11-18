class Solution:         #Brute Force Method.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = i+1
            for j in range(len(nums)):
                if(nums[j] == target-nums[i]):
                    l = [i, j]
                    return l
            
            
s = Solution()      
p = s.twoSum([2, 7, 9, 11, 15], 9)
print(p)
