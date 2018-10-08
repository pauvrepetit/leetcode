def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    line1 = "qwertyuiopQWERTYUIOP"
    line2 = "asdfghjklASDFGHJKL"
    line3 = "zxcvbnmZXCVBNM"
    lines = [line1, line2, line3]
    word_del = []
    # flag = 0
    for word in words:
        if word[0] in line1:
            flag = 0
        elif word[0] in line2:
            flag = 1
        else:
            flag = 2
        for char in word:
            if char not in lines[flag]:
                word_del.append(word)
                break
    reword = []
    for word in words:
        if word not in word_del:
            reword.append(word)
    return reword


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
