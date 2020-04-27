import csv
from bs4 import BeautifulSoup

file = open('messages.txt', 'a')

with open("frostbite.html", "r", encoding="utf8", errors='ignore') as f:
    
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    file.write(soup.text.strip())

file.close()


