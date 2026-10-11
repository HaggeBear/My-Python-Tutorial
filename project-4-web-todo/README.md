# Project 4: Web Todo List

## 🎯 Goal
Learn Flask by making a web-based todo list.

---

## 📌 Start Here

First install Flask:
```bash
pip install flask
```

Then create this:

```python
# app.py - Simple Flask web app
from flask import Flask, render_template_string

app = Flask(__name__)

Todos = ["Buy groceries", "Walk the dog"]

@app.route("/")
def home():
    html = """
    <h1>My Todo List</h1>
    <ul>
        {% for todo in todos %}
        <li>{{ todo }}</li>
        {% endfor %}
    </ul>
    """
    return render_template_string(html, todos=Todos)

if __name__ == "__main__":
    app.run(debug=True)
```

Save as `project-4-web-todo/app.py` and run with `python app.py`

Then visit: http://localhost:5000

---

## 🚀 Next Steps

1. **Add HTML templates**
   - Create `templates/index.html`

2. **Add CSS styling**
   - Create `static/style.css`

3. **Add new todos**
   - Create a form to add tasks

4. **Add delete functionality**
   - Let users delete todos

5. **Add database**
   - Save todos to a file or database

---

## 💡 Tips

- Start with the simple version
- Use Flask's `render_template` for HTML files
- Put CSS in `static/` folder
- Test in browser as you build
