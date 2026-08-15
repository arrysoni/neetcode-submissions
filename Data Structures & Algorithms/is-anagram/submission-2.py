class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Case 1:
        if (len(s) != len(t)):
            return False
        else:
            return (sorted(s) == sorted(t))

        