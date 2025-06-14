# pyhtml

**pyhtml** is a lightweight Python-based HTML builder library. It allows you to programmatically generate HTML pages using intuitive Python functions instead of writing raw HTML code.

## ✅ Features

- Supports all basic HTML elements (`<p>`, `<h1>`, `<img>`, `<a>`, etc.)
- Includes structural elements like `<header>`, `<main>`, `<footer>`
- Meta tag generation (`charset`, `viewport`, SEO tags, etc.)
- Inline and linked CSS and JS support
- Form element builders: `input`, `textarea`, `checkbox`, `radio`, `select`, etc.
- Media support: images, videos, audio, iframes
- Code block rendering
- Supports direction (`dir`) and language (`lang`) for RTL/LTR pages

## 📦 Requirements

- Python 3.x

## 🚀 Usage Example

```python
from pyhtml import *

meta_charset()
meta_viewport()
meta_description("This is an example page about Algeria.")
meta_keywords(["Algeria", "Africa", "Tourism"])
meta_author("Your Name")

link_css("styles.css")
style("body { font-family: Arial; background-color: #f9f9f9; padding: 20px; }")

h1("Welcome to Algeria")
img("https://upload.wikimedia.org/wikipedia/commons/7/77/Flag_of_Algeria.svg", "Algerian Flag", width="200")
p("Algeria is the largest country in Africa, known for its Mediterranean coastline and Saharan desert.")
ul(["Capital: Algiers", "Official language: Arabic", "Currency: Algerian dinar"])

html_output = html(lang="en", title="Algeria Example Page", dir="ltr")
save("algeria.html", html_output)

Made by Lakson-dv
