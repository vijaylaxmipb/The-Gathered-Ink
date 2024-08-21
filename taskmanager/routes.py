import os
from taskmanager import app
from taskmanager.models import Category, Task


@app.route('/')
def home():
    return "Welcome to Gathered Ink!"

@app.route('/about')
def about():
    return "This is the about page."

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )