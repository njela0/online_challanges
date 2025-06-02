"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

"""

def canConstruct(ransomNote: str, magazine: str): # -> bool:
    ransomNote_list = []
    magazine_list = list(magazine)

    for chr in ransomNote:
        if chr in magazine_list:
            ransomNote_list.append(chr)
            magazine_list.remove(chr)
        else:
            break

    if "".join(ransomNote_list) == ransomNote:
        return True
    else:
        return False


ransomNote = "abbca"
magazine = "baacdb"

print(canConstruct(ransomNote, magazine))