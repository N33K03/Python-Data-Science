import requests
from bs4 import BeautifulSoup


html="‹table›‹tr›‹td›Pizza Place‹/td><td›Orders‹/td><td>Slices </td></tr<tr><td>Domino'sPizza</td><td>10</td><td>100</td>く/tr><tr><td>LittleCaesars</td›<td›12</td><td>144</td>‹/table›"
table = BeautifulSoup(html, 'html5lib')

table_row = table.find_all(name='tr')  # the find_all() method looks through a tag's descendants and retrieves all the descendants.

first_row = table_row[0]  # gives first tabel cell

for i, row in enumerate(table_row):   # loop to iterate through each table cell
    print('row', i)
    cells = row.find_all('td')

    for j, cell in enumerate(cells):
        print('column', j, 'cells', cell)




