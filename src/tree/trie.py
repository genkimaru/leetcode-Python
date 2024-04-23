class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Trie:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
                if node.is_end:
                    return True
            else:
                return False


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
word = 'apple'
prefix = 'apps'
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
print(param_2)
param_3 = obj.startsWith(prefix)
print(param_3)