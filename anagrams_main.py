# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    if sorted(word) != sorted(anagram):
        return False

    else:
        return True

print(find_anagrams("below", "elbow"))
print(find_anagrams("hello", "check"))