from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
NOTES_DIR = "notes"
VIEWS_FILE = "views.txt"

os.makedirs(NOTES_DIR, exist_ok=True)

# Load views count
if not os.path.exists(VIEWS_FILE):
    with open(VIEWS_FILE, "w") as f:
        f.write("")

views = {}
with open(VIEWS_FILE, "r") as f:
    for line in f:
        name, count = line.strip().split(":")
        views[name] = int(count)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/note/<note_name>", methods=["GET", "POST"])
def note(note_name):
    path = os.path.join(NOTES_DIR, note_name + ".txt")
    
    if request.method == "POST":
        with open(path, "w") as f:
            f.write(request.form["content"])
        return "Saved"
    
    if os.path.exists(path):
        with open(path, "r") as f:
            content = f.read()
    else:
        content = ""

    # Count views
    views[note_name] = views.get(note_name, 0) + 1
    with open(VIEWS_FILE, "w") as f:
        for k, v in views.items():
            f.write(f"{k}:{v}\n")

    return render_template("note.html", note_name=note_name, content=content, views=views[note_name])

@app.route("/admin-login")
def admin_login():
    return render_template("admin_login.html")

if __name__ == "__main__":
    app.run(debug=True)
