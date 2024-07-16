class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashCounter = {}
        for letter in s:
            if letter in hashCounter:
                hashCounter[letter] += 1
            else:
                hashCounter[letter] = 1
        
        for letter in t:
            if letter in hashCounter:
                if hashCounter[letter] == 0:
                    return False
                hashCounter[letter] -= 1
            else:
                return False
        
        for num in hashCounter.values():
            if num != 0:
                return False
        
        return True
                