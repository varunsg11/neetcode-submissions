class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        for j in t:
            dict2[j] =  dict2.get(j, 0) + 1

    
        for j in t:
            try:
                if dict1[j] != dict2[j]:
                    return False
            except:
                return False
        return True
        