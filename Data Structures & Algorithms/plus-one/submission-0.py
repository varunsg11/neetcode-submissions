class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''
        for i in digits:
            res += str(i)
        
        new_res =  int(res) + 1

        final_res = []
        
        for i in str(new_res):
            final_res.append(int(i))
        
        return final_res