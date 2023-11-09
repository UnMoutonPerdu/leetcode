class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for letter in ransomNote:
            try:
                index_letter = magazine.index(letter)
                magazine[index_letter] = "."
            except ValueError:
                return False

        return True