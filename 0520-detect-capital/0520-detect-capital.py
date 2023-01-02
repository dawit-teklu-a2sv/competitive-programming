class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_are_upper = True
        all_are_small = True
        first_letter_upper = True
        for i in range(len(word)):
            if not word[i].isupper():
                all_are_upper = False
            if not word[i].islower():
                all_are_small = False
            if i != 0 and word[i].isupper():
                first_letter_upper = False
        return all_are_upper or all_are_small or first_letter_upper
                