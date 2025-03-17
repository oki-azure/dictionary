import json

class Node:
    """A Node in the Binary Search Tree."""
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree for dictionary operations."""
    def __init__(self):
        self.root = None

    def insert(self, word, meaning):
        """Insert a new word into the BST."""
        self.root = self._insert_recursive(self.root, word.lower(), meaning)

    def _insert_recursive(self, node, word, meaning):
        if node is None:
            return Node(word, meaning)
        if word < node.word:
            node.left = self._insert_recursive(node.left, word, meaning)
        elif word > node.word:
            node.right = self._insert_recursive(node.right, word, meaning)
        return node

    def search(self, word):
        """Search for a word in the BST."""
        return self._search_recursive(self.root, word.lower())

    def _search_recursive(self, node, word):
        if node is None:
            return None
        if node.word == word:
            return node.meaning
        if word < node.word:
            return self._search_recursive(node.left, word)
        return self._search_recursive(node.right, word)

    def update_word(self, word, new_meaning):
        """Update the meaning of an existing word."""
        node = self._find_node(self.root, word.lower())
        if node:
            node.meaning = new_meaning
            return True
        return False

    def _find_node(self, node, word):
        """Find a node containing the word."""
        if node is None or node.word == word:
            return node
        if word < node.word:
            return self._find_node(node.left, word)
        return self._find_node(node.right, word)

    def get_all_words(self):
        words = []
        self._inorder_traversal(self.root, words)
        return words


    def _inorder_traversal(self, node, words):
        if node:
            self._inorder_traversal(node.left, words)
            words.append((node.word, node.meaning))  
            self._inorder_traversal(node.right, words)

    def delete(self, word):
        """Delete a word from the BST."""
        self.root, deleted = self._delete_recursive(self.root, word.lower())
        return deleted

    def _delete_recursive(self, node, word):
        if node is None:
            return node, False
        if word < node.word:
            node.left, deleted = self._delete_recursive(node.left, word)
        elif word > node.word:
            node.right, deleted = self._delete_recursive(node.right, word)
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            min_larger_node = self._find_min(node.right)
            node.word, node.meaning = min_larger_node.word, min_larger_node.meaning
            node.right, _ = self._delete_recursive(node.right, min_larger_node.word)
            return node, True
        return node, deleted

    def _find_min(self, node):
        """Find the smallest node in a subtree."""
        while node.left:
            node = node.left
        return node

    def save_to_file(self, filename):
        """Save dictionary words to a JSON file in dictionary format."""
        words = {word: meaning for word, meaning in self.get_all_words()}
        with open(filename, "w") as file:
            json.dump(words, file, indent=4)


    def load_from_file(self, filename):
        """Load dictionary words from a JSON file."""
        try:
            with open(filename, "r") as file:
                content = file.read().strip()
                if not content:  
                    words = {}
                else:
                    words = json.loads(content)
                for word, meaning in words.items():
                    self.insert(word, meaning)
        except (FileNotFoundError, json.JSONDecodeError):
            with open(filename, "w") as file:
                json.dump({}, file)

    def get_suggestions(self, prefix):
        suggestions = []
        self._collect_suggestions(self.root, prefix, suggestions)
        return suggestions

    def _collect_suggestions(self, node, prefix, suggestions):
        if node is None:
            return
        # If the node's word starts with the prefix, add it to suggestions
        if node.word.startswith(prefix):
            suggestions.append(node.word)
        # Recursively check left and right subtrees
        self._collect_suggestions(node.left, prefix, suggestions)
        self._collect_suggestions(node.right, prefix, suggestions)