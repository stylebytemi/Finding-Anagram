# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "helop") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    result = True
    if len(word) != len(anagram):
        return False
    for x in word:
        if x not in anagram:
            result = False
        else:
            anagram.replace(x, "")
    return result

print(find_anagram("below", "began"))