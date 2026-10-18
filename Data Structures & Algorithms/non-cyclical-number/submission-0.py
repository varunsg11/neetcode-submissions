class Solution:
    def isHappy(self, n: int) -> bool:
        number = n
        storage = []
        result = 0
        while result != 1:
            result =  self.sqr(n)
            if result in storage:
                return False
            else:
                storage.append(result)
                n = result


        return True


    def sqr(self, number: int) -> int:
        number =  str(number)
        res = 0
        for i in number:
            res = int(i)**2 + res
        
        return res