import requests

url = "https://dam.flippenterprise.net/flyerkit/publication/7813184/products?display_type=all&locale=en&access_token=881f0b9feea3693a704952a69b2a037a"

def get_data(url):
    response = requests.get(url)
    return response.json()

data_freshco = get_data(url)
total_products = len(data_freshco)
print(f"Number of products: {total_products}")

html_links= """
    <link href="https://cdn.jsdelivr.net/npm/daisyui@latest/dist/full.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.tailwindcss.com"></script>
"""

html_title = "<h1 class='text-3xl font-bold text-center mb-4 text-primary'>Freshco Discount List</h1>"

html_table_start = """
    <div class="overflow-x-auto">
        <table class="table table-zebra w-full shadow-md">
            <thead>
                <tr class="bg-base-200">
                    <th>ID</th>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Image</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
"""

html_bottom = """
            </tbody>
        </table>
    </div>
"""

test_html = html_title + html_table_start + html_bottom

with open("template.html", "r") as f:
    template = f.read()

test_template = template.replace("<title>Document</title>", "<title>Freshco Flyer</title>")
test_template = test_template.replace("{{change_head}}", html_links)
test_template = test_template.replace("{{change_body}}", test_html)

with open("index.html", "w") as f:
    f.write(test_template)

print("HTML file created successfully.")


item = data_freshco[0]

id = item.get('id')
name = item.get('name')
price = item.get('price_text')
image = item.get('image_url')

html_sample_row = f"""
                <tr>
                    <td>{id}</td>
                    <td>{name}</td>
                    <td>{price}</td>
                    <td><img src="{image}" alt="product" class="w-[50px] h-[50px] rounded shadow border object-contain"></td>
                    <td><button class="btn btn-success btn-xs text-white px-3">Edit</button>
                        <button class="btn btn-error btn-xs text-white px-3">Delete</button></td>
                </tr>
"""

final_test_html = html_title + html_table_start + html_sample_row + html_bottom

with open("index.html", "w") as f:
    f.write(final_test_html)

print("HTML file with sample row created successfully.")

all_html_rows = ""

for item in data_freshco:
    id = item.get('id')
    name = item.get('name')
    price = item.get('price_text')
    image = item.get('image_url')
    row = f"""
                <tr>
                    <td>{id}</td>
                    <td>{name}</td>
                    <td>{price}</td>
                    <td><img src="{image}" alt="product" class="w-[50px] h-[50px] rounded shadow border object-contain"></td>
                    <td>
                        <button class="btn btn-success btn-xs text-white px-3">Edit</button>
                        <button class="btn btn-error btn-xs text-white px-3">Delete</button></td>
                </tr>
    """ 

    all_html_rows += row

full_html = html_title + html_table_start + all_html_rows + html_bottom

with open("index.html", "w") as f:
    f.write(full_html)

print("HTML file with all products created successfully.")


total_products = len(data_freshco)

html_count_info = f"""
    <div class="flex justify-end mb-6 w-full">
        <div class="stats shadow scale-50 origin-right border-base-200">
            <div class="stat p-1 px-3 flex flex-row items-baseline">
                <span class="stat-title">Total</span>
                <span class="stat-value text-orange-500 text-2xl">{total_products}</span>
                <span class="stat-desc">Updated just now</span>
            </div>
        </div>
    </div>
"""

final_html_with_count = html_title + html_table_start + all_html_rows + html_count_info + html_bottom

with open("index.html", "w") as f:
    f.write(final_html_with_count)

print("HTML file with product count created successfully.")

final_sample_html = template.replace("<title>Document</title>", "<title>Freshco Flyer</title>")
final_sample_html = final_sample_html.replace("{{change_head}}", html_links)
final_sample_html = final_sample_html.replace("{{change_body}}", final_html_with_count)

with open("index.html", "w") as f:
    f.write(final_sample_html)

print("Finish.")