from collections import defaultdict

class Node(object):

    def __init__(self, key, data=None):
        self.key = key
        self.data = data  # data is set to None if node is not the final char of string
        self.children = {}
        self.length = defaultdict(int)


class Trie(object):

    def __init__(self):
        self.head = Node(None)


    def insert(self, string):
        curr_node = self.head
        curr_node.length[len(string)] += 1

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node.children[char].length[len(string)] += 1
            curr_node = curr_node.children[char]

        curr_node.data = string



    def starts_with(self, prefix, length):
        curr_node = self.head

        nPrefix = prefix.replace("?", "")

        for char in nPrefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]

            else:
                return 0

        return curr_node.length[length]



def solution(words, queries):

    # 문제 정의

    answer = []

    fowardTrie = Trie()
    backwardTrie = Trie()

    for i in words:
        fowardTrie.insert(i)
        backwardTrie.insert(i[::-1])


    for i in range(len(queries)):

        if queries[i][0] != "?":

            answer += [fowardTrie.starts_with(queries[i], len(queries[i]))]

        else:
            answer += [backwardTrie.starts_with(queries[i][::-1], len(queries[i]))]

    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))