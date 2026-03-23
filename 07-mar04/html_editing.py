# Last time modified: 03/04/26
# Authour: lazy-h-null
# Class 07 - Assignment 1

def generate_website():
    html_base = ""

    with open("base.html", "r") as website:
        html_base = website.read()
        
    page_title = "MY Awesome Python Website"

    html_modified = html_base.replace("<title>Document", f"<title>{page_title}") 

    daisy_ui ="""

    <!-- Daisy UI -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <!-- Daisy ui themes -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />

    """

    html_modified = html_modified.replace("</head>", daisy_ui +"\n</head>" )

    theme = "retro"
    html_modified = html_modified.replace('<html lang="en">', f'<html lang="en" data-theme="{theme}">')

    nav_bar = """
    <div class="navbar bg-base-100 shadow-sm">
      <a class="btn btn-ghost text-xl">S.H.I.E.L.D. Database: Hero Registry</a>
    </div>
    """
    my_table = """
    <div class="overflow-x-auto rounded-box border border-base-content/5 bg-base-100">
    <table class="table">
    <!-- head -->
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>Favorite Color</th>
      </tr>
    </thead>
    <tbody>
      <!-- row 1 -->
      <tr>
        <th>1</th>
        <td>Iron Man</td>
        <td>CEO</td>
        <td class = "text-red-500 font-bold">Red</td>
      </tr>
      <!-- row 2 -->
      <tr>
        <th>2</th>
        <td>Hulk</td>
        <td>Scientist</td>
        <td class = "text-success font-bold">Green</td>
      </tr>
      <!-- row 3 -->
      <tr>
        <th>3</th>
        <td>Captain Marvel</td>
        <td>Cosmic Guardian</td>
        <td class = "text-amber-500 font-bold">Gold</td>
      </tr>
       <!-- row 4 -->
      <tr class="bg-base-200/50 animate-pulse">
        <th>4</th>
        <td colspan="3" class="italic text-xl py-6 text-base-content/60 text-center tracking-widest">Waiting for the Next Legend......</td>
      </tr>
    </tbody>
    </table>
    </div>
    """

    my_stack = """
    <div class="container mx-auto px-4 mb-10 text-center mt-5">
        <h2 class="text-2xl font-bold mb-4">Personnel file</h2>
        <div class="avatar-group -space-x-6 text-center justify-center">
          <div class="avatar">
           <div class="w-12">
             <img src="https://img.daisyui.com/images/profile/demo/batperson@192.webp" />
           </div>
          </div>
          <div class="avatar">
            <div class="w-12">
              <img src="https://img.daisyui.com/images/profile/demo/spiderperson@192.webp" />
            </div>
          </div>
          <div class="avatar">
            <div class="w-12">
              <img src="https://img.daisyui.com/images/profile/demo/averagebulk@192.webp" />
            </div>
          </div>
          <div class="avatar">
            <div class="w-12">
              <img src="https://img.daisyui.com/images/profile/demo/wonderperson@192.webp" />
            </div>
          </div>
        </div>
    </div>
    """
    html_modified = html_modified.replace('<body>', '<body>\n'+nav_bar)
    html_modified = html_modified.replace('</body>', my_stack + my_table + "\n</body>")

    with open("index.html", "w") as file:
        file.write(html_modified)

generate_website()