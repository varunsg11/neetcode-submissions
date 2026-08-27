class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        for i in s:
            print(stck)
            if stck == []:
                stck.append(i)
            elif i == "(" or i == "[" or i == "{"   :
                stck.append(i)
            else:
                if i == ")" and stck[-1] == "(":
                    stck.pop()
                elif i == "]" and stck[-1] == "[":
                    stck.pop()
                elif i == "}" and stck[-1] == "{":
                    stck.pop()
                else:
                    return False
        if stck == []:
            return True
        return False