def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    for l in set(s1):
        if not s1.count(l) == s2.count(l):
            return False
    return True

def anagrams(word, words):
    return [w for w in words if is_anagram(word, w)]

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

