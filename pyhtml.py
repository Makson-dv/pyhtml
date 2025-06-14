
cont = []
meta_tags = []
css_links = []
css_styles = []
js_scripts = []
js_inline = []


def p(content): cont.append(f"<p>{content}</p>")
def h1(content): cont.append(f"<h1>{content}</h1>")
def h2(content): cont.append(f"<h2>{content}</h2>")
def h3(content): cont.append(f"<h3>{content}</h3>")
def h4(content): cont.append(f"<h4>{content}</h4>")
def h5(content): cont.append(f"<h5>{content}</h5>")
def h6(content): cont.append(f"<h6>{content}</h6>")

def br(): cont.append("<br>")
def hr(): cont.append("<hr>")
def span(content): cont.append(f"<span>{content}</span>")
def div(content, class_name=""): cls = f' class="{class_name}"' if class_name else ""; cont.append(f"<div{cls}>{content}</div>")
def a(href, content, target="_blank"): cont.append(f'<a href="{href}" target="{target}">{content}</a>')
def af(href,imag,alt,width): 
    cont.append(f'<a href="{href}" target="_blank"><img src="{imag}" alt="{alt}"width="{width}"></a>')
def img(src, alt="", width="", height=""):
    size = f' width="{width}"' if width else ""
    size += f' height="{height}"' if height else ""
    cont.append(f'<img src="{src}" alt="{alt}"{size}>')

def ul(items): cont.append(f"<ul>{''.join(f'<li>{item}</li>' for item in items)}</ul>")
def ol(items): cont.append(f"<ol>{''.join(f'<li>{item}</li>' for item in items)}</ol>")

def table(headers, rows):
    thead = "".join(f"<th>{h}</th>" for h in headers)
    tbody = "".join("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in rows)
    cont.append(f"<table border='1'><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>")

def header(content): cont.append(f"<header>{content}</header>")
def footer(content): cont.append(f"<footer>{content}</footer>")
def nav(content): cont.append(f"<nav>{content}</nav>")
def main(content): cont.append(f"<main>{content}</main>")
def section(content): cont.append(f"<section>{content}</section>")
def article(content): cont.append(f"<article>{content}</article>")
def aside(content): cont.append(f"<aside>{content}</aside>")


def form(action="", method="post", content=""): cont.append(f'<form action="{action}" method="{method}">{content}</form>')
def input_text(name, value="", placeholder=""): cont.append(f'<input type="text" name="{name}" value="{value}" placeholder="{placeholder}">')
def input_password(name, placeholder=""): cont.append(f'<input type="password" name="{name}" placeholder="{placeholder}">')
def input_submit(value="إرسال"): cont.append(f'<input type="submit" value="{value}">')


def meta_charset(charset="utf-8"):
    meta_tags.append(f'<meta charset="{charset}">')

def meta_viewport(content="width=device-width, initial-scale=1.0"):
    meta_tags.append(f'<meta name="viewport" content="{content}">')

def meta_compatibility():
    meta_tags.append('<meta http-equiv="X-UA-Compatible" content="IE=edge">')

def meta_description(content):
    meta_tags.append(f'<meta name="description" content="{content}">')

def meta_keywords(keywords):
    if isinstance(keywords, list): keywords = ", ".join(keywords)
    meta_tags.append(f'<meta name="keywords" content="{keywords}">')

def meta_author(name): meta_tags.append(f'<meta name="author" content="{name}">')
def meta_refresh(seconds=30): meta_tags.append(f'<meta http-equiv="refresh" content="{seconds}">')
def meta_theme_color(color): meta_tags.append(f'<meta name="theme-color" content="{color}">')

def meta_custom(name, content):
    meta_tags.append(f'<meta name="{name}" content="{content}">')

def link_css(href):
    css_links.append(f'<link rel="stylesheet" href="{href}">')

def style(css_code):
    css_styles.append(f"<style>{css_code}</style>")


def script_src(src):
    js_scripts.append(f'<script src="{src}"></script>')

def script_inline(code):
    js_inline.append(f"<script>{code}</script>")

def script_file(file_path):
    with open(file_path, encoding="utf-8") as f:
        code = f.read()
        js_inline.append(f"<script>{code}</script>")


def html(lang="en", title="no title",dir="ltr"):
    body = "\n".join(cont)
    meta = "\n".join(meta_tags)
    css = "\n".join(css_links + css_styles)
    js = "\n".join(js_scripts + js_inline)
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{dir}">
<head>
    {meta}
    <title>{title}</title>
    {css}
</head>
<body>
{body}
{js}
</body>
</html>"""


def save(filename, html_content):
    if not filename.endswith(".html"):
        filename += ".html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Done: {filename}")




def input_radio(name, value, label_text=""):
    cont.append(f'<label><input type="radio" name="{name}" value="{value}"> {label_text}</label>')

def input_checkbox(name, value, label_text=""):
    cont.append(f'<label><input type="checkbox" name="{name}" value="{value}"> {label_text}</label>')

def input_hidden(name, value):
    cont.append(f'<input type="hidden" name="{name}" value="{value}">')

def input_file(name):
    cont.append(f'<input type="file" name="{name}">')

def textarea(name, placeholder="", rows=4, cols=40):
    cont.append(f'<textarea name="{name}" placeholder="{placeholder}" rows="{rows}" cols="{cols}"></textarea>')

def select(name, options):
    opts = "".join(f'<option value="{val}">{val}</option>' for val in options)
    cont.append(f'<select name="{name}">{opts}</select>')

def label(for_id, text):
    cont.append(f'<label for="{for_id}">{text}</label>')

def button(content, onclick=""):
    action = f' onclick="{onclick}"' if onclick else ""
    cont.append(f'<button{action}>{content}</button>')

def iframe(src, width="", height=""):
    size = f' width="{width}"' if width else ""
    size += f' height="{height}"' if height else ""
    cont.append(f'<iframe src="{src}"{size}></iframe>')

def video(src, controls=True, width="", height=""):
    controls_attr = " controls" if controls else ""
    size = f' width="{width}"' if width else ""
    size += f' height="{height}"' if height else ""
    cont.append(f'<video src="{src}"{controls_attr}{size}></video>')

def audio(src, controls=True):
    controls_attr = " controls" if controls else ""
    cont.append(f'<audio src="{src}"{controls_attr}></audio>')

def figure(img_src, caption, width="", height=""):
    size = f' width="{width}"' if width else ""
    size += f' height="{height}"' if height else ""
    cont.append(f'''
<figure>
    <img src="{img_src}" alt="{caption}"{size}>
    <figcaption>{caption}</figcaption>
</figure>''')

def code_block(code, language=""):
    lang_class = f' class="language-{language}"' if language else ""
    cont.append(f"<pre><code{lang_class}>{code}</code></pre>")
