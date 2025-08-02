class Library:
    def __init__(self):
        self.books  = []
        

    def add_book (self, title, author):
        self.books.append({"title": title, "author": author})

    def remove_book (self, title):
        update_books = []

        for book in self.books :
            if book["title"] != title:
                update_books.append(book)

        self.books = update_books
         

    def search_book(self, title):
        found_books = []
        for book in self.books:
            if book["title"] == title:
                found_books.append(book)
        return found_books


    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Book in the library:") 
            for book in self.books:
                print(f" - {book['title']} by {book['author']}")   

