from typing import List
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0

        dictionary = defaultdict(list)

        for word in wordList:
            for i, ch in enumerate(word):
                dictionary[word[:i] + '*' + word[i + 1:]].append(word)

        print(dictionary)

        def bfs(word, endWord):
            visited = list()
            queue = list()

            visited.append(word)
            queue.append([word, 0])

            while queue:
                word, count = queue.pop(0)

                if word == endWord:
                    return count+1

                for i in range(0, len(word)):
                    for value in dictionary[word[:i] + '*' + word[i + 1:]]:
                        if value not in visited:
                            visited.append(value)
                            queue.append([value, count + 1])

            return 0

        c = bfs(beginWord, endWord)
        return c

solution = Solution()

print(solution.ladderLength(beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log"]))
print(solution.ladderLength(beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log","cog"]))