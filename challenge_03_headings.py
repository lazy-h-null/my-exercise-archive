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

h1 = "Welcome to My Page"
h2 = "About This Project"
h3 = "Technical Details"

body_content = f"    <h1>{h1}</h1>\n    <h2>{h2}</h2>\n    <h3>{h3}</h3>"

parts = html.split("<body>", 1)
#Advanced Extension -> add 1

html = parts[0] + "<body>\n" + body_content + "\n" + parts[1]
#"\n": reviving the divided <body> and simultaneously pressing Enter so that the next letters appear nicely on the next line
#python number -> 0(real 1), 1(real 2), 2(real 3), 3(real 4), 4(real 5)

print(html)