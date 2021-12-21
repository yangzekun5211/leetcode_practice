# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:18:18 2021

@author: zyang672
"""

from copy import deepcopy

class Solution(object):
    def findSubstring(self, s, words):
        """
        records = deepcopy(words)
        result = []
        if not s or not words:
            return
        
        fst = 0
        snd = 0
        n = len(words[0])
        while fst <= len(s)-len(words)*n and snd < len(s):
            while records:
                if s[snd:snd+n] in records:                    
                    records.remove(s[snd:snd+len(words[0])])
                    snd += n
                elif s[snd:snd+n] in words:
                    records = deepcopy(words)
                    snd = fst + n
                    fst += n
                else:
                    break
            if not records:
                result.append(fst)
                records = [s[fst:fst+n]]
                fst += n
            elif snd == fst:
                snd += 1
                fst += 1
                records = deepcopy(words)
            else:
                fst = deepcopy(snd)
                records = deepcopy(words)
        return result
    """                    
        nb_words = len(words)
        len_word = len(words[0])
        target_len = len_word * nb_words
        word_counter = Counter(words)
        result = []
        for i in range(0, len(s) - target_len + 1):
            sub_string = s[i : i + target_len]     
            is_solution = True
            for word in word_counter:
                current_count = 0
                for j in range(0, target_len, len_word):
                    if sub_string[j : j + len_word] == word:
                        current_count += 1
                if current_count != word_counter[word]:
                    is_solution = False
                    break
            if is_solution:
                result.append(i)
        return result
        
    
if __name__ == '__main__':
    p = "foobarfoobar"
    q = ["foo","bar"]

#    q.right.right = TreeNode(0)
    print Solution().findSubstring(p, q) 