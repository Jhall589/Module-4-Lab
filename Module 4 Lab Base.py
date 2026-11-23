from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "book_name": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "publisher": "George Allen & Unwin"
    }
]

# READ - Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# READ - Get a single book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# CREATE - Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# UPDATE - Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()

    for book in books:
        if book["id"] == id:
            book["book_name"] = data["book_name"]
            book["author"] = data["author"]
            book["publisher"] = data["publisher"]
            return jsonify(book)

    return jsonify({"message": "Book not found"}), 404

# DELETE - Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})

    return jsonify({"message": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

    {
    "id": 1,
    "book_name": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "publisher": "George Allen & Unwin"
}

    