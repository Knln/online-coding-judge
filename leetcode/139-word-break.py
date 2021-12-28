from typing import List

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:

    if not wordList:
        return 0

    visited = list()
    queue = list()

    def oneLetterDifference(word1, word2):
        one_letter = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                if one_letter == 0:
                    one_letter += 1
                else:
                    return False

        if one_letter == 0:
            return False
        else:
            return True

    def bfs(visited, word, wordList, endWord):
        visited.append(word)
        queue.append([word, 0])

        while queue:
            word, count = queue.pop(0)

            if word == endWord:
                return count+1

            for w in wordList:
                if oneLetterDifference(word, w):
                    if w not in visited:
                        visited.append(w)
                        queue.append([w, count+1])

        return 0


    c = bfs(visited, beginWord, wordList, endWord)
    return c


print(ladderLength('hot', 'dog', ["hot","dog"]))