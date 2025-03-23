# Dictionary Binary Search Tree (BST) Code

This code represents a dictionary application, with all the words organized in a **Binary Search Tree (BST)**. A BST is a tree-like structure where:
- Each "node" (point) stores a word and its meaning.
- Words smaller alphabetically go to the left branch.
- Words larger alphabetically go to the right branch.
- This makes searching and managing words faster.

Here’s a step-by-step explanation of the different parts of the code:

---

## Node Class
### Purpose:
This represents one piece of the tree—a word and its meaning.

### Code:
```
python
class Node:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None
```
---

## BST (Binary Search Tree) Class
### Purpose:
Manages all operations related to the dictionary, like adding, searching, updating, or deleting words.

Functions:
Here’s what each function does:

#### 1. Insert a Word
```
python
def insert(self, word, meaning):
    self.root = self._insert_recursive(self.root, word.lower(), meaning)
```
This function adds a word to the tree.

```
_insert_recursive 
```
ensures the word goes in the correct position (left for smaller, right for larger)

#### 2. Search for a Word

```
python
def search(self, word):
    return self._search_recursive(self.root, word.lower())
```
Checks if a word exists in the tree.

```
_search_recursive
```
Traverses the tree:

If the word matches, it returns the meaning.

If the word is smaller, it looks left; if larger, it looks right.

#### 3. Update a Word

```
python
def update_word(self, word, new_meaning):
    node = self._find_node(self.root, word.lower())
    if node:
        node.meaning = new_meaning
        return True
    return False
```
Finds a word and changes its meaning.

```
_find_node: Locates the node containing the word.
```

#### 4. Get All Words

```
python
def get_all_words(self):
    words = []
    self._inorder_traversal(self.root, words)
    return words
```
Gathers all words in alphabetical order.

```
_inorder_traversal: Visits the smaller words first (left), then the current word, then larger words (right).
```

#### 5. Delete a Word

```
python
def delete(self, word):
    self.root, deleted = self._delete_recursive(self.root, word.lower())
    return deleted
```
Removes a word from the tree.

##### How it works:

- If no children, it simply removes the node.

- If one child, it connects the child to the parent.

- If two children, it replaces the word with the smallest word from the right branch.

#### 6. Save the Dictionary to a File

```
python
def save_to_file(self, filename):
    words = {word: meaning for word, meaning in self.get_all_words()}
    with open(filename, "w") as file:
        json.dump(words, file, indent=4)
```
Converts the entire dictionary into a JSON file so the data can be stored and reused.

#### 7. Load the Dictionary from a File

```
python
def load_from_file(self, filename):
    try:
        with open(filename, "r") as file:
            words = json.loads(file.read().strip() or "{}")
            for word, meaning in words.items():
                self.insert(word, meaning)
```
Reads the JSON file and rebuilds the tree by inserting the stored words back.

#### 8. Suggestions

```
python
def get_suggestions(self, prefix):
    suggestions = []
    self._collect_suggestions(self.root, prefix, suggestions)
    return suggestions
```
Provides autocomplete suggestions based on a prefix.

##### How it works:

- Looks for words starting with the prefix using _collect_suggestions.

##### How Everything Works Together:

- Insert: Add a new word.

- Search: Find a word's meaning.

- Update: Change an existing word's meaning.

- Delete: Remove a word.

- Save/Load: Keep your dictionary safe in a file and reload it anytime.

- Suggestions: Quickly find words that match what you’re typing.

---

## Created By: DSA Group 3 
### Members:
- Setor Yao
- David Kwame
- Klenam Delvin Koku
- Tiindang Martin
- Reine
- Jesse
- Kelvin Agbozo
- Gabriel Nii Attoh
---