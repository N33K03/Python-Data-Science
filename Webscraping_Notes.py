import requests
from bs4 import BeautifulSoup

html="‹!DOCTYPE html›<html><head›‹title›PageTitle</title>‹/head>‹body><h3><b id='boldest'>LebronJames</b>‹/h3><p› Salary: $ 92,000,000 </p><h3> StephenCurry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p>Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, ' html5lib')

tag_object_title = soup.title
tag_object_h3 = soup.h3

child_tag_h3 = tag_object_h3.b   # accesses the child of the tag
parent_tag_h3 = child_tag_h3     # accesses the parent tag
sibling1_tag_h3 = tag_object_h3.next_sibling # finds sibling of tag object
attribute_name_child_tage_h3 = child_tag_h3.attrs  # accesses attribute name

# the find_all() method looks through a tag's descendants and retrieves all the descendants.



