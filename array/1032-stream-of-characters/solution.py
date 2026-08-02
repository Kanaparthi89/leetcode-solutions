class StreamChecker:

    class TrieNode:
        __slots__ = ('children', 'is_word')

        def __init__(self):
            self.children = [-1] * 26
            self.is_word = False

    def __init__(self, words):
        self.trie = [self.TrieNode()]
        self.stream = []
        self.max_len = 0

        # Build reversed Trie
        for word in words:
            self.max_len = max(self.max_len, len(word))

            node = 0

            for ch in reversed(word):
                idx = ord(ch) - ord('a')

                if self.trie[node].children[idx] == -1:
                    self.trie[node].children[idx] = len(self.trie)
                    self.trie.append(self.TrieNode())

                node = self.trie[node].children[idx]

            self.trie[node].is_word = True

    def query(self, letter):
        self.stream.append(ord(letter) - ord('a'))

        # Keep only the part that can possibly match
        if len(self.stream) > self.max_len:
            self.stream.pop(0)

        node = 0

        # Search backwards
        for i in range(len(self.stream) - 1, -1, -1):
            idx = self.stream[i]

            next_node = self.trie[node].children[idx]

            if next_node == -1:
                return False

            node = next_node

            if self.trie[node].is_word:
                return True

        return False