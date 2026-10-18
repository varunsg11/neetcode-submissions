class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeros = 0
        final_res = []
        multi = 1
        for i in nums:
            if i == 0:
                zeros += 1
                if zeros > 1:
                    return [0] * len(nums)
                continue
            multi *= i

        for i in nums:
            if zeros == 1:
                if i == 0:
                    final_res.append(multi)
                else:
                    final_res.append(0)
            else:
                final_res.append(int(multi // i))

        return final_res