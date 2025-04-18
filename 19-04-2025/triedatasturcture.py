class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False


class Trie:
    def __init__(self):
        
        self.root=TrieNode()
    def instert(self, word: str) -> None:
        """Inserts a word into the trie."""
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.endofword=True
    def serach(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.endofword
    def startsWith(self, prefix: str) -> bool:
        """Returns if there is a word in the trie that starts with the given prefix."""
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True
    def delete(self, word: str) -> None:    
        """Deletes a word from the trie."""
        def dfs(cur, word, index):
            if index==len(word):
                if not cur.endofword:
                    return False
                cur.endofword=False
                return len(cur.children)==0
            c=word[index]
            if c not in cur.children:
                return False
            can_delete=dfs(cur.children[c], word, index+1)
            if can_delete:
                del cur.children[c]
                return len(cur.children)==0 and not cur.endofword
            return False
        
        dfs(self.root, word, 0)
    def get_all_words(self, node=None, prefix='', words=None):      
        """Get all words in the trie."""
        if words is None:
            words = []
        if node is None:
            node = self.root
        if node.endofword:
            words.append(prefix)
        for char, child_node in node.children.items():
            self.get_all_words(child_node, prefix + char, words)
        return words
    
    def get_all_words_with_prefix(self, prefix: str) -> list:   
        """Get all words in the trie with a given prefix."""
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return []
            cur=cur.children[c]
        return self.get_all_words(cur, prefix)
# You can test the Trie class with the following code:
if __name__ == "__main__":
    trie = Trie()
    trie.instert("apple")
    trie.instert("app")
    print(trie.serach("apple"))  # True
    print(trie.serach("app"))    # True
    print(trie.serach("appl"))   # False
    print(trie.startsWith("app")) # True
    trie.delete("apple")
    print(trie.serach("apple"))  # False
    print(trie.get_all_words())  # ['app']
    print(trie.get_all_words_with_prefix('a'))  # ['app']
# The Trie class is a data structure that allows for efficient storage and retrieval of strings.
