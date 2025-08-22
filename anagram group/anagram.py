

def anagram(lst):
    group = {}
    for word in lst:
        key1 = ''.join(sorted(word))
        if key1 in group:
            group[key1].append(word)
        else:
            group[key1] = [word]
    print(group)
    return list(group.values())


k=["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram(k))


        
        