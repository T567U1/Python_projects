
class Trie:
    def __init__(self):
        self.dic = {}
        self._end = '_end_'

    def get_trie(self):
        return self.dic

    def add_word(self, word):
        dic = self.dic
        for char in word:
            dic = dic.setdefault(char, {})
        dic[self._end] = self._end

    def has_word(self, word):
        dic = self.dic
        for char in word:
            if char not in dic:
                self.add_word(word)
                return False
            dic = dic[char]

        return True

trie = Trie()
trie.add_word('hello')
print(trie.get_trie())
trie.add_word('helloo')
print(trie.get_trie())
print(trie.has_word('hellr'))
print(trie.has_word('hellr'))
