# Web Todo List - Starter Code
# Save this as: project-4-web-todo/app.py
# Run with: python app.py
# Visit: http://localhost:5000

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
