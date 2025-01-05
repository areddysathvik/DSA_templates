class Node:
    
    def __init__(self):
        self.children = [None] * (26)
        self.countPrefixs = 0
        self.countEndsWith = 0
    
    def get_index(self, ch):
        return ord(ch) - ord('a')

    def get(self, ch):
        return self.children[self.get_index(ch)]

    def contains(self, ch):
        return self.children[self.get_index(ch)] is not None
    
    def put(self, ch, node):
        self.children[self.get_index(ch)] = node
    
    def increment_prefix(self):
        self.countPrefixs += 1
    
    def increment_ends_with(self):
        self.countEndsWith += 1
    
    def decrement_prefix(self):
        self.countPrefixs -= 1
    
    def decrement_ends_with(self):
        self.countEndsWith -= 1

class Trie:

    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        curRoot = self.root
        for ch in word:
            if not curRoot.contains(ch):
                curRoot.put(ch, Node())

            curRoot = curRoot.get(ch)
            curRoot.increment_prefix()

        curRoot.increment_ends_with()
    
    def get_longest_prefix_helper(self, word, totalWords):
        prefix = ''
        curRoot = self.root
        for ch in word:
            if not curRoot.contains(ch):
                return prefix

            curRoot = curRoot.get(ch)
            
            if curRoot.countPrefixs >= totalWords:
                prefix += ch
            else:
                return prefix
        
        return prefix
    
    def erase(self, word):
        curRoot = self.root
        for ch in word:
            if curRoot.contains(ch):
                curRoot = curRoot.get(ch)
                curRoot.decrement_ends_with()

        curRoot.decrement_ends_with()
