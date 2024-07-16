class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            hashString = [0]*26 
            for letter in s:
                hashString[ord(letter) - ord('a')] += 1
            
            groups[tuple(hashString)].append(s)
            
        return list(groups.values())
            