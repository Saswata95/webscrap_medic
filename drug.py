from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = 'http://janaushadhi.gov.in/list_of_medicines.html'

uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()

page_soup = soup(page_html, "html.parser")

filename = "generic_medic.csv"
f = open(filename, "w")

table_heads = page_soup.find_all("th")
header = table_heads[0].text

for i in range(1, 6):
    head_temp = table_heads[i].text
    header = header + ", " + head_temp
    if i == 5:
        header = header + "\n"
    else:
        continue
f.write(header)

table_contents = page_soup.find_all("tr")
len(table_contents)
del table_contents[0]
del table_contents[756]
del table_contents[755]
for table_content in table_contents:
    table_cells = table_content.findAll("td")
    body = table_cells[0].text
    
    for i in range(1, 6):
        body_temp = table_cells[i].text.replace(",", "|").replace("\n", " ")
        body = body + ", " + body_temp
        if i == 5:
            body = body + "\n"
        else:
            continue
    f.write(body)
print('Scrapping completed! Check generic_medic.csv for the data.')
f.close()