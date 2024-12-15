from bs4 import BeautifulSoup


html_doc = """
<html>
    <head><title>Sample Website</title></head>
    <body>
        <h1>Welcome to the Sample Website</h1>
        <p>This is a <b>bold</b> paragraph.</p>
        <a href="http://example.com">Visit Example</a>
    </body>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_doc, 'html.parser')

# Print the prettified HTML
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.h1)

# print(soup.a)
# print(soup.a['href'])

# print(soup.get_text())

link = soup.find('a')
print(link)
print(link['href'])
