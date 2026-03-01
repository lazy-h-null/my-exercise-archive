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
    <h1>Welcome to My Page</h1>
    <h2>About This Project</h2>
    <h3>Technical Details</h3>
</body>
</html>"""

paragraph_text = "This project was built entirely using Python string methods."
img_src = "hero.jpg"
img_alt = "A hero image for the page"

p_tag = f"    <p>{paragraph_text}</p>"
img_tag = f"    <img src='{img_src}' alt='{img_alt}'>"

pos = html.rfind("</h3>")

insert_pos = pos + len("</h3>")

html = html[:insert_pos] + "\n" + p_tag + "\n" + img_tag + html[insert_pos:]

print(html)