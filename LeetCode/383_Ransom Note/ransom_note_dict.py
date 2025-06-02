def canConstruct(ransomNote: str, magazine: str): # -> bool:
    letters_dict = {}

    for chr in magazine:
        if chr in letters_dict:
            letters_dict[chr] += 1
        else:
            letters_dict[chr] = 1

    print(letters_dict)

    for chr in ransomNote:
        if chr in letters_dict.keys() and ransomNote.count(chr) <= letters_dict[chr]:
            result = True
        else:
            result = False
            break

    return result


ransomNote = "aabccdc"
magazine = "acddcabca"

print(canConstruct(ransomNote, magazine))