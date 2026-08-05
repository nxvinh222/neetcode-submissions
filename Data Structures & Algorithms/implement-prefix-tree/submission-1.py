class TrieNode():
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for character in word:
            if character in node.children:
                node = node.children[character]
            else:
                node.children[character] = TrieNode()
                node = node.children[character]
        node.wordEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for character in word:
            if character in node.children:
                node = node.children[character]
            else:
                return False
        if not node.wordEnd:
            return False
        return True
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for character in prefix:
            if character in node.children:
                node = node.children[character]
            else:
                return False
        return True