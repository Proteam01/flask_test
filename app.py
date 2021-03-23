from flask import Flask, jsonify, request
from book import BookDAO, Book
from flask_json import FlaskJSON

app = Flask(__name__)
FlaskJSON(app)
# app.config["DEBUG"] = True


@app.route('/books', methods=['GET'])
def home():
    book_dao = BookDAO()
    books = book_dao.get_all_books()
    books_json = map(lambda book: book.__dict__, books)
    return jsonify(books_json)


@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book_dao = BookDAO()
    book = book_dao.get_book_by_id(id)
    return jsonify(book.__dict__)


@app.route('/books', methods=['POST'])
def save_book():
    content = request.get_json()
    book = Book()
    book_dao = BookDAO()
    book.name = content['name']
    book.type = content['type']
    book_dao.save_book(book)
    return 'saved'


@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book_dao = BookDAO()
    book_dao.delete(id)
    return 'deleted'


app.run('localhost', port=3000, debug=True)
