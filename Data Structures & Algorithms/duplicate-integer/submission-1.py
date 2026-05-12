class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        duplicate = False
        if len(nums) != 0:
            seen.append(nums[0])
            for i in range (len(nums)):
                if i == 0:
                    continue
                if nums[i] not in seen:
                    seen.append(nums[i])
                    continue
                else:
                    duplicate = True
                    break;
        
        return duplicate