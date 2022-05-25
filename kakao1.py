class Node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    def insert(self, string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node  = self.head
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
                print(char)
            else:
                return False

        if current_node.data != None:
            print(current_node.data)
            return True



trie = Trie()
trie.insert("apple")
trie.insert("abbcd")
trie.insert("abbc")
trie.search("abbcd")