class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        counter = 0
        res = ''

        while i + j < len(word1) + len(word2):
            try:
                res += word1[i]
                i += 1
            except:
                pass
            try:
                res += word2[j]
                j += 1
            except:
                pass

        return res