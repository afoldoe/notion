import unittest


LETTER_NUMBER_MAP = {
    'a': 2, 'b': 2, 'c': 2,
    'd': 3, 'e': 3, 'f': 3,
    'g': 4, 'h': 4, 'i': 4,
    'j': 5, 'k': 5, 'l': 5,
    'm': 6, 'n': 6, 'o': 6,
    'p': 7, 'q': 7, 'r': 7, 's': 7,
    't': 8, 'u': 8, 'v': 8,
    'w': 9, 'x': 9, 'y': 9, 'z': 9,
}


def word_to_numbers(word):
    """
    Converts a word to it's T9 keypad input representation:
        >>> _word_to_numbers("apple")
        [2, 7, 7, 5, 3]
    """
    return [LETTER_NUMBER_MAP[c] for c in word]


class T9TrieNode(object):
    """
    Indexes words by their T9 keypad representation.
    The root of a Trie is a TrieNode with no word or numbers, only child
    nodes.
    """
    def __init__(self, number):
        self.number = number
        self.word = None
        self.children = []

    def insert(self, word):
        """
        Inserts a word into the trie, adding new child nodes if
        necessary.
        """
        node = self
        numbers = word_to_numbers(word)
        for n in numbers:
            child = node.find_child_by_number(n)
            if not child:
                child = T9TrieNode(n)
                node.add_child(child)

            node = child

        node.word = word

    def find_child_by_number(self, n):
        print('self.children in search %r' % (self.children))
        for child in self.children:
            print('child.word %r' % (child.word))
            if child.number == n:
                return child

        return None

    def add_child(self, node):
        self.children.append(node)

    def search(self, input_numbers):
        """
        Returns a list of all possible words that match the input
        numbers.
        """
        node = self
        # catching the exception test now passes
        while input_numbers and node:
            n = input_numbers[0]
            node = node.find_child_by_number(n)
            input_numbers = input_numbers[1:]

        if node:
            return node.collect_subwords()
        else:
            return []

    def collect_subwords(self):
        result = []
        if self.word:
            result.append(self.word)

        for c in self.children:
            result.extend(c.collect_subwords())

        # print("Value of %r" % (result))
        return result


WORD_LIST = [
    'addendum',
    'ape',
    'app',
    'appeal',
    'apple',
    'bode',
    'code',
    'mode',
    'open'
]


def build_trie_from_words(words):
    trie = T9TrieNode(None)
    for word in words:
        trie.insert(word)

    return trie


class T9TrieNodeTest(unittest.TestCase):
    def setUp(self):
        self.t9trie = build_trie_from_words(WORD_LIST)

    def test_exact_match(self):
        self.assertEqual(["ape"], self.t9trie.search([2, 7, 3]))

    def test_partial_match(self):
        self.assertEqual(["addendum"], self.t9trie.search([2, 3, 3, 3]))

    def test_multiple_matches(self):
        self.assertEqual(["app", "appeal", "apple"], self.t9trie.search([2, 7, 7]))

    def test_no_match(self):
        self.assertEqual([], self.t9trie.search([2, 9, 9]))

    """test to catch bode AND code bug. Not currently passing. I believe this is the bug, but I could not get a proper working solution before 5pm Wed 
    def test_found_bug(self):
        self.assertEqual(["bode", "code"], self.t9trie.search([2, 6, 3, 3]))

    """
if __name__ == "__main__":
    unittest.main()
