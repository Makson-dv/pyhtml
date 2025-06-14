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
