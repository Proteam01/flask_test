import sqlite3


class Book:

    def __init__(self):
        self.id = None
        self.name = None
        self.type = None


class BookDAO:

    def get_all_books(self):
        conn = sqlite3.connect('flask.db')
        cursor = conn.execute('select * from books')
        books = []
        rows = cursor.fetchall()
        for row in rows:
            book = Book()
            book.id = row[0]
            book.name = row[1]
            book.type = row[2]
            books.append(book)
        conn.close()
        return books

    def get_book_by_id(self, book_id):
        conn = sqlite3.connect('flask.db')
        cursor = conn.execute('select * from books where id = ?', [book_id])
        rows = cursor.fetchall()
        book = Book()
        for row in rows:
            book.id = row[0]
            book.name = row[1]
            book.type = row[2]
        conn.close()
        return book

    def save_book(self, book):
        conn = sqlite3.connect('flask.db')
        sql = "insert into books (name,type) values(?,?)"
        conn.execute(sql, (book.name, book.type))
        conn.commit()
        conn.close()

    def delete(self, book_id):
        conn = sqlite3.connect('flask.db')
        sql = "delete from books where id = ?"
        conn.execute(sql, [book_id])
        conn.commit()
        conn.close()

