html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
</body>
</html>"""

html = html.replace('lang="en"', 'lang="es"')
html = html.replace('<title>My Page</title>', '<title>Full Page Challenge</title>')

new_css = "app.min.css"
new_js = "main.bundle.js"

pos_css = html.find("styles.css")
end_css = pos_css + len("styles.css")
html = html[:pos_css] + new_css + html[end_css:]

pos_js = html.find("app.js")
end_js = pos_js + len("app.js")
html = html[:pos_js] + new_js + html[end_js:]

if html.count("styles.css") == 0 and html.count("app.js") == 0:
    print("✅ Assets updated successfully!")

h1= "Welcome to My Page"
h2= "About This Project"
h3= "Technical Details"
body_headings = f"    <h1>{h1}</h1>\n    <h2>{h2}</h2>\n    <h3>{h3}</h3>"
parts = html.split("<body>", 1)
html = parts[0] + "<body>\n" + body_headings + parts[1]

p_text = "This project was built entirely using Python string methods."
img_src = "hero.jpg"
img_alt = "A hero image for the page"
p_tag = f"    <p>{p_text}</p>"
img_tag = f"    <img src='{img_src}' alt='{img_alt}'>"
pos = html.rfind("</h3>")
insert_pos = pos + len("</h3>")
html = html[:insert_pos] + "\n" + p_tag + "\n" + img_tag + html[insert_pos:]

title_start = html.find("<title>") + len("<title>")
title_end = html.find("</title>")
extracted_title = html[title_start:title_end]
# Full Page Challenge
p_tag_2 = f"    <p>This page title is: {extracted_title}</p>"
pos_body_end = html.find("</body>")
html = html[:pos_body_end] + p_tag_2 + "\n" + html[pos_body_end:]

print("\n--- Validation Report ---")

print(f"{'✅' if 'Full Page Challenge' in html else '❌'} <title> is correct")
print(f"{'✅' if html.count('<h1>') == 1 else '❌'} <h1> found")
print(f"{'✅' if html.count('<h2>') == 1 else '❌'} <h2> found")
print(f"{'✅' if html.count('<h3>') == 1 else '❌'} <h3> found")
print(f"{'✅' if html.count('<img') == 1 else '❌'} <img> appears exactly once")
print(f"{'✅' if html.count('<p>') == 2 else '❌'} <p> appears exactly twice")
print(f"{'✅' if html.startswith('<!DOCTYPE html>') else '❌'} Starts with <!DOCTYPE html>")
print(f"{'✅' if html.strip().endswith('</html>') else '❌'} Ends with </html>")

print("-" * 25 + "\n")

print(html)