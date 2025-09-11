def group_by_signature(words: list) -> list:
    words = [word for word in words if word]
    same = [''.join(sorted(a)) for a in words]
    pick = [i for i in set(same)]
    result = {}
    for i in pick:
        result[i] = []
        for word in words:
            if i == ''.join(sorted(word)):
                result[i] += [word]
    return list(result.values())

if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]