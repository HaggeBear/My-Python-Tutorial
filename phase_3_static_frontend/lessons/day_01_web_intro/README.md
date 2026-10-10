# Day 1: Introduction to the Web and HTML Basics

## 🎯 Learning Objectives

By the end of today, you will be able to:
- Understand how the web works (client-server model)
- Understand the role of HTML, CSS, and JavaScript in web development
- Learn the basic structure of an HTML document
- Create your first HTML page
- Understand HTML elements and tags
- Use common HTML tags for content

---

## 📚 Lesson: How the Web Works

### The Client-Server Model

The web operates on a **client-server model**:

1. **Client (Your Browser):** Requests information
2. **Server (Web Server):** Provides information

When you visit a website:
1. Your browser (client) sends a **request** to the server
2. The server processes the request
3. The server sends back a **response** (usually HTML, CSS, JavaScript, images, etc.)
4. Your browser renders the response as a web page

```
┌─────────────┐     Request     ┌─────────────┐
│   Client     │ ─────────────▶ │    Server    │
│  (Browser)   │                 │  (Website)   │
└─────────────┘ ◀───────────── └─────────────┘
       Response
```

### HTTP Protocol

**HTTP (HyperText Transfer Protocol)** is the protocol used for communication between clients and servers.

- **HTTP Methods:**
  - `GET`: Retrieve data from the server
  - `POST`: Send data to the server
  - `PUT`: Update data on the server
  - `DELETE`: Delete data on the server

- **HTTP Status Codes:**
  - `200 OK`: Request was successful
  - `404 Not Found`: Resource doesn't exist
  - `500 Internal Server Error`: Server error
  - `403 Forbidden`: No permission to access resource

### URLs (Uniform Resource Locators)

A URL is the address of a resource on the web:

```
https://www.example.com:443/path/to/resource?query=value#section
└────┬────└ └───────────┬───────────└ └──────┬──────└ └─────┬─────└
     │                │                     │               │
  Protocol        Domain Name          Path           Query    Fragment
```

- **Protocol:** `http://` or `https://` (HTTP or HTTPS)
- **Domain Name:** `www.example.com` (the server address)
- **Port:** `:80` or `:443` (default ports for HTTP and HTTPS)
- **Path:** `/path/to/resource` (location of the resource on the server)
- **Query:** `?query=value` (parameters for the request)
- **Fragment:** `#section` (scrolls to a specific part of the page)

---

## 📚 Lesson: The Three Pillars of Web Development

### 1. HTML (HyperText Markup Language)

**Purpose:** Structure and content of the web page

- Defines the **skeleton** of the page
- Specifies what content appears on the page
- Uses **tags** to mark up content
- Example: headings, paragraphs, lists, links, images

```html
<!-- HTML Example -->
<h1>My Web Page</h1>
<p>This is a paragraph of text.</p>
<a href="https://example.com">Visit Example</a>
```

### 2. CSS (Cascading Style Sheets)

**Purpose:** Visual appearance and layout

- Defines the **style** of the page
- Controls colors, fonts, spacing, layout
- Makes the page look good
- Separates presentation from content

```css
/* CSS Example */
h1 {
    color: blue;
    font-size: 24px;
}

p {
    color: gray;
    line-height: 1.5;
}
```

### 3. JavaScript

**Purpose:** Interactivity and behavior

- Adds **interactivity** to the page
- Handles user actions (clicks, form submissions, etc.)
- Manipulates content dynamically
- Communicates with servers without page reloads (AJAX)

```javascript
// JavaScript Example
function greet() {
    alert("Hello, World!");
}
```

### How They Work Together

```
┌─────────────────────────────────────────────────────┐
│                        Web Page                          │
├─────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   │
│   │    HTML     │   │    CSS      │   │ JavaScript  │   │
│   │  Structure   │   │  Styling    │   │  Behavior    │   │
│   │  & Content   │   │  & Layout   │   │  & Logic     │   │
│   └─────────────┘   └─────────────┘   └─────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────┘
```

---

## 📚 Lesson: HTML Basics

### What is HTML?

HTML is a **markup language** that defines the structure and content of a web page. It's not a programming language - it doesn't have logic or variables. It simply describes what the page contains.

### HTML Document Structure

Every HTML document should have this basic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <!-- Page content goes here -->
</body>
</html>
```

- `<!DOCTYPE html>`: Declares this as an HTML5 document
- `<html>`: Root element of the document
- `<head>`: Contains metadata about the document (not visible on the page)
- `<body>`: Contains the visible content of the page

### HTML Elements

An **HTML element** consists of:
- **Opening tag:** `<tagname>`
- **Content:** The actual content
- **Closing tag:** `</tagname>`

```html
<p>This is a paragraph.</p>
└─┬─┘
  │
  └── Opening tag

┌───────────────┐
│ This is a     │
│ paragraph.     │
└───────────────┘
  │
  └── Content

┌─┬─┐
│/ │ p│
└─┴─┘
  │
  └── Closing tag
```

### Self-Closing Tags

Some elements don't have content and are self-closing:

```html
<img src="image.jpg" alt="An image">
<br>  <!-- Line break -->
<hr>  <!-- Horizontal rule -->
<input type="text">
```

---

## 📚 Common HTML Tags

### Basic Text Tags

| Tag | Description | Example |
|-----|-------------|---------|
| `<h1>` to `<h6>` | Headings (h1 is most important) | `<h1>Main Heading</h1>` |
| `<p>` | Paragraph | `<p>A paragraph of text.</p>` |
| `<br>` | Line break | `<p>Line 1<br>Line 2</p>` |
| `<hr>` | Horizontal rule (line) | `<hr>` |
| `<strong>` | Bold text (semantic) | `<strong>Important</strong>` |
| `<b>` | Bold text (presentational) | `<b>Bold</b>` |
| `<em>` | Italic text (semantic) | `<em>Emphasized</em>` |
| `<i>` | Italic text (presentational) | `<i>Italic</i>` |
| `<u>` | Underlined text | `<u>Underlined</u>` |
| `<del>` | Deleted text | `<del>Deleted</del>` |
| `<sup>` | Superscript | `<sup>2</sup>` (x²) |
| `<sub>` | Subscript | `<sub>2</sub>` (H₂O) |

### Links and Images

| Tag | Description | Example |
|-----|-------------|---------|
| `<a>` | Anchor (link) | `<a href="https://example.com">Link</a>` |
| `<img>` | Image | `<img src="image.jpg" alt="Description">` |

### Lists

| Tag | Description | Example |
|-----|-------------|---------|
| `<ul>` | Unordered list | `<ul><li>Item 1</li><li>Item 2</li></ul>` |
| `<ol>` | Ordered list | `<ol><li>First</li><li>Second</li></ol>` |
| `<li>` | List item | `<li>An item</li>` |

### Tables

| Tag | Description | Example |
|-----|-------------|---------|
| `<table>` | Table | `<table>...</table>` |
| `<tr>` | Table row | `<tr>...</tr>` |
| `<th>` | Table header cell | `<th>Header</th>` |
| `<td>` | Table data cell | `<td>Data</td>` |

### Forms

| Tag | Description | Example |
|-----|-------------|---------|
| `<form>` | Form | `<form action="/submit" method="post">...</form>` |
| `<input>` | Input field | `<input type="text" name="username">` |
| `<textarea>` | Multi-line text | `<textarea name="comment"></textarea>` |
| `<button>` | Button | `<button type="submit">Submit</button>` |
| `<select>` | Dropdown | `<select><option>Option</option></select>` |
| `<option>` | Dropdown option | `<option value="1">Option 1</option>` |
| `<label>` | Label for form field | `<label for="username">Username:</label>` |

### Semantic Elements

| Tag | Description | Example |
|-----|-------------|---------|
| `<header>` | Header content | `<header>...</header>` |
| `<footer>` | Footer content | `<footer>...</footer>` |
| `<nav>` | Navigation | `<nav>...</nav>` |
| `<main>` | Main content | `<main>...</main>` |
| `<article>` | Article content | `<article>...</article>` |
| `<section>` | Section of content | `<section>...</section>` |
| `<aside>` | Sidebar content | `<aside>...</aside>` |
| `<div>` | Division (generic container) | `<div>...</div>` |
| `<span>` | Span (generic inline container) | `<span>...</span>` |

---

## 💡 HTML Attributes

HTML elements can have **attributes** that provide additional information:

```html
<a href="https://example.com" target="_blank" rel="noopener">Example</a>
      └────────┬────────┘  └────────┬────────┘  └────────┬────────┘
               │                 │                     │
             href             target               rel
```

### Common Attributes

| Attribute | Description | Example |
|-----------|-------------|---------|
| `id` | Unique identifier | `<div id="main">` |
| `class` | Class name (can be used on multiple elements) | `<div class="container">` |
| `style` | Inline CSS styles | `<p style="color: red;">` |
| `title` | Tooltip text | `<a title="Visit Example">Link</a>` |
| `alt` | Alternative text (for images) | `<img alt="Description">` |
| `src` | Source (for images, scripts, etc.) | `<img src="image.jpg">` |
| `href` | Hyperlink reference | `<a href="https://example.com">` |
| `target` | Link target | `<a target="_blank">` |
| `name` | Name (for form fields) | `<input name="username">` |
| `value` | Value (for form fields) | `<input value="Default">` |
| `type` | Type (for input fields) | `<input type="password">` |
| `placeholder` | Placeholder text | `<input placeholder="Enter name">` |
| `required` | Required field | `<input required>` |

---

## 🎯 Creating Your First HTML Page

Let's create a simple HTML page together:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Web Page</title>
</head>
<body>
    <h1>Welcome to My First Web Page!</h1>
    
    <p>This is a paragraph of text on my web page.</p>
    
    <h2>About Me</h2>
    <p>I'm learning to build web pages with HTML and CSS.</p>
    
    <h2>My Favorite Things</h2>
    <ul>
        <li>Coding</li>
        <li>Reading</li>
        <li>Hiking</li>
    </ul>
    
    <h2>Contact Me</h2>
    <p>Email: <a href="mailto:me@example.com">me@example.com</a></p>
    
    <hr>
    
    <footer>
        <p>&copy; 2024 My First Web Page</p>
    </footer>
</body>
</html>
```

### How to View Your HTML Page

1. Save the code above in a file named `index.html`
2. Open the file in a web browser (double-click or right-click → Open With)
3. You should see your first web page!

---

## 🎯 Exercises

Now it's your turn! Complete the following exercises to practice what you've learned.

### Exercise Files

1. **exercise_1.html** - Create a simple HTML page with basic structure
2. **exercise_2.html** - Add various HTML elements

Open each file and follow the instructions inside.

---

## 📝 Knowledge Check

Test your understanding by answering these questions:

1. What is the client-server model?
   - Your answer: ________________________________________

2. What are the three main technologies used in web development?
   - Your answer: ________________________________________

3. What is the purpose of HTML?
   - Your answer: ________________________________________

4. What is the basic structure of an HTML document?
   - Your answer: ________________________________________

5. What is an HTML element?
   - Your answer: ________________________________________

6. What is the difference between a heading and a paragraph in HTML?
   - Your answer: ________________________________________

7. What is an HTML attribute?
   - Your answer: ________________________________________

8. How do you create a link in HTML?
   - Your answer: ________________________________________

---

## 🌟 Challenge (Optional)

Create an HTML page about your favorite hobby that includes:
- A title for the page
- A main heading
- At least two subheadings
- At least three paragraphs
- An unordered list
- An ordered list
- At least one link to a relevant website
- At least one image (you can use a placeholder image URL)

**Hint:** Use semantic HTML elements where appropriate (header, main, footer, etc.)

---

## 📚 Additional Resources

### HTML Tutorials
- [MDN Web Docs - HTML Basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
- [W3Schools - HTML Tutorial](https://www.w3schools.com/html/html_intro.asp)
- [HTML & CSS by Jon Duckett (Book)](https://www.htmlandcssbook.com/)
- [freeCodeCamp - HTML](https://www.freecodecamp.org/learn/2022/responsive-web-design/learn-html-by-building-a-cat-photo-app/step/1)

### Web Development
- [How the Internet Works (MDN)](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Internet_works)
- [Client-Server Model Explained](https://www.cloudflare.com/learning/ddos/glossary/client-server-model/)
- [HTTP Basics](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics)

### Tools
- [VS Code HTML Preview](https://code.visualstudio.com/docs/languages/html)
- [Online HTML Editor](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_default)
- [HTML Validator](https://validator.w3.org/)

---

## 🎉 Next Steps

Once you've completed the exercises:
1. Review your answers to the knowledge check
2. Try the optional challenge
3. Move on to **Day 2: HTML Structure and Semantics**

**Great job on Day 1!** 🎉
