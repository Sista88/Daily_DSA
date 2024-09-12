class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        min_len = min(word1_len, word2_len)
        st = ""
        for i in range(min_len):
            st = st + word1[i] + word2[i]
        final_i = i
        if word1_len > word2_len:
            st = st + word1[final_i + 1 :]
        else:
            st = st + word2[final_i + 1 :]
        return st
