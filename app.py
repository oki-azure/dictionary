from flask import Flask, request, jsonify
from bst import BST

app = Flask(__name__)
dictionary = BST()

# Load existing words from file
dictionary.load_from_file("dictionary.json")

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/search/<word>', methods=['GET'])
def search_word(word):
    meaning = dictionary.search(word)
    return jsonify({"word": word, "meaning": meaning if meaning else "Not found"})

@app.route('/add', methods=['POST'])
def add_word():
    data = request.json
    dictionary.insert(data["word"], data["meaning"])
    dictionary.save_to_file("dictionary.json")
    return jsonify({"message": f'Word "{data["word"]}" added successfully'})

@app.route('/update', methods=['PUT'])
def update_word():
    data = request.json
    updated = dictionary.update_word(data["word"], data["new_meaning"])
    if updated:
        dictionary.save_to_file("dictionary.json")
        return jsonify({"message": f'Word "{data["word"]}" updated successfully'})
    return jsonify({"message": "Word not found"}), 404

@app.route('/delete/<word>', methods=['DELETE'])
def delete_word(word):
    deleted = dictionary.delete(word)
    dictionary.save_to_file("dictionary.json")
    return jsonify({"message": f'Word "{word}" deleted' if deleted else "Word not found"})

@app.route('/suggest/<prefix>', methods=['GET'])
def suggest_words(prefix):
    suggestions = dictionary.get_suggestions(prefix)
    return jsonify({"suggestions": suggestions})

@app.route('/words', methods=['GET'])
def get_all_words():
    words = dictionary.get_all_words()
    return jsonify(words)

if __name__ == '__main__':
    app.run(debug=False)

# Group Members:
"""  
Kelvin Agbozo - 20886484
Setor Yao Avemenku - 20913143
David Kwame Castel - 20819673
Klenam Delvin Hottor - 20884236
Tiindang Martin - 20888690
Reine Ngamaleu - 21462627
Jesse Osei-Adu - 20896586
Gabriel Nii Attoh (Lead Coder) - 20910834
"""