from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data Dummy
books = [
    {"id": 1, "title": "tugas cloud computing", "author": "Pitoli", "year": 2020},
    {"id": 2, "title": "tugas docker", "author": "Ronal", "year": 2021}
]

# Halaman Utama (Read)
@app.route("/")
def index():
    return render_template("index.html", books=books)

# Tambah Buku (Create)
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "id": len(books) + 1,
            "title": request.form["title"],
            "author": request.form["author"],
            "year": int(request.form["year"])
        }
        books.append(new_book)
        return redirect(url_for("index"))
    return render_template("add.html")

# Edit Buku (Update)
@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return "Book not found", 404
    if request.method == "POST":
        book["title"] = request.form["title"]
        book["author"] = request.form["author"]
        book["year"] = int(request.form["year"])
        return redirect(url_for("index"))
    return render_template("edit.html", book=book)

# Hapus Buku (Delete)
@app.route("/delete/<int:book_id>")
def delete(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

