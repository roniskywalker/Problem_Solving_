class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapTS, mapST = {}, {}
        for char1, char2 in zip(s,t):
            if ((char1 in mapTS and mapTS[char1]!=char2) or (char2 in mapST and mapST[char2]!=char1)):
                return False
            mapTS[char1] = char2
            mapST[char2] = char1
        return True