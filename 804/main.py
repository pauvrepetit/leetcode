class Solution:
    def uniqueMorseRepresentations(self,  words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        chars = list("abcdefghijklmnopqrstuvwxyz")
        morsedict = dict(zip(chars, morse))
        morsewords = []
        for word in words:
            morseword = ''
            for char in word:
                morseword = morseword + morsedict[char]
            if morseword not in morsewords:
                morsewords.append(morseword)
        return len(morsewords)
