"""
Problem Link: https://leetcode.com/problems/word-ladder-ii/

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord 
-> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences 
from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of 
the words [beginWord, s1, s2, ..., sk].

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 
Constraints:
1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 1000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
from collections import defaultdict

# BFS
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        word_list = set(wordList)
        
        level = {}
        level[beginWord] = [[beginWord]]
        
        while level:
            new_level = defaultdict(list)
            
            for word, ladder in level.items():
                if word == endWord:
                    return level[word]
            
            
                for i in range(len(word)):
                    for char in alphabets:
                        new_word = word[:i] + char + word[i+1:]

                        if new_word in word_list:
                            new_level[new_word].extend([l + [new_word] for l in ladder])
                            
            word_list -= set(new_level.keys())
            
            level = new_level
        
        return []


# TLE
class Solution1:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.res = []
        self.res_length = float('inf')
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        self.count = {}
        
        def make_ladders(begin_word, end_word, word_list, cur_list):
            if len(cur_list) > self.res_length:
                return
            
            if begin_word == end_word:
                if len(cur_list) < self.res_length:
                    self.res = []
                    self.res_length = len(cur_list)
                    
                self.res.append(cur_list)
                return
            
            for i in range(len(begin_word)):
                for char in alphabets:
                    new_word = begin_word[:i] + char + begin_word[i+1:]
                    
                    if new_word in word_list:
                        self.count[new_word] = self.count.get(new_word, 0) + 1
                        word_list.remove(new_word)
                        make_ladders(new_word, end_word, word_list, cur_list + [new_word])
                        word_list.add(new_word)
        
        make_ladders(beginWord, endWord, set(wordList), [beginWord])
        
        return self.res
