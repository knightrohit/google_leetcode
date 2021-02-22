from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or len(beginWord) != len(endWord) or beginWord == endWord:
            return 0
        
        word_dict = defaultdict(list)
        size = len(beginWord)
        
        
        for word in wordList:
            for i in range(size):
                word_dict[word[:i] + '*' + word[i+1:]].append(word)                
                
        # BFS
        visited = set()
        queue = deque()
        queue.append((beginWord, 1))
        
        while queue:
            word, level = queue.popleft()

            for i in range(size):
                temp_word = word[:i] + '*' + word[i+1:]
                for child in word_dict[temp_word]:
                    if child == endWord and child != word:
                        return level + 1
                    if child == endWord:
                        return level

                    if child in visited:
                        continue
                    else:
                        visited.add(child)
                        queue.append((child, level + 1))
                        
        return 0