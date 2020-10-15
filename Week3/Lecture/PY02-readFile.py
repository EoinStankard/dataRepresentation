from bs4 import BeautifulSoup

with open("../Week2/Lab/CarViewer.html") as fp:
    soup = BeautifulSoup(fp,'html.parser')

print (soup.prettify())