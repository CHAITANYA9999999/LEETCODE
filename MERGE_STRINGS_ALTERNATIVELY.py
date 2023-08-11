class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_str = ""
        i=0
        while(i<len(word1) and i<len(word2)):
            merged_str = merged_str + word1[i] + word2[i]
            i+=1
        if(i<=len(word1)):
            merged_str += word1[i:len(word1)]
        
        if(i<=len(word2)):
            merged_str += word2[i:len(word2)]
        return merged_str