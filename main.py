import tkinter as tk
from tkinter import simpledialog, messagebox
from mylibrary.library import Library  

def main():
    lib = Library()

    def add_book():
        title = simpledialog.askstring("Add Book", "Enter book title:")
        author = simpledialog.askstring("Add Book", "Enter book author:")
        if title and author:
            lib.add_book(title, author)
            messagebox.showinfo("Success", "✅ Book added.")
        else:
            messagebox.showwarning("Input Error", "Both fields are required.")

    def remove_book():
        title = simpledialog.askstring("Remove Book", "Enter book title to remove:")
        if title:
            lib.remove_book(title)
            messagebox.showinfo("Removed", "🗑️ Book removed.")

    def search_book():
        title = simpledialog.askstring("Search Book", "Enter book title to search:")
        result = lib.search_book(title)
        if result:
            books = "\n".join(f"- {b['title']} by {b['author']}" for b in result)
            messagebox.showinfo("Found", f"🔍 Book(s) found:\n{books}")
        else:
            messagebox.showinfo("Not Found", "❌ Book not found.")

    def show_books():
        if not lib.books:
            messagebox.showinfo("Library", "No books in the library.")
        else:
            books = "\n".join(f"- {b['title']} by {b['author']}" for b in lib.books)
            messagebox.showinfo("Library Books", books)

    def exit_app():
        root.destroy()

    # GUI setup
    root = tk.Tk()
    root.title("📚 Library System")
    root.geometry("400x400")

    tk.Label(root, text="Library Menu", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="1. Add Book", width=25, command=add_book).pack(pady=10)
    tk.Button(root, text="2. Remove Book", width=25, command=remove_book).pack(pady=10)
    tk.Button(root, text="3. Search Book", width=25, command=search_book).pack(pady=10)
    tk.Button(root, text="4. Show All Books", width=25, command=show_books).pack(pady=10)
    tk.Button(root, text="5. Exit", width=25, command=exit_app).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
