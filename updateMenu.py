import requests
from bs4 import BeautifulSoup
import time
URL = "https://newsmerp.iiserkol.ac.in/canteen/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html5lib')
specials = soup.find_all('div', attrs = {'class': 'blink_me'})
menuContainer = soup.find('div', attrs = {'class': 'tablecontainer'})
menu = [line.strip() for line in str(menuContainer.text).splitlines() if line.strip() != '']
specials = [special.text.strip() for special in specials]
out = [[], [], [], []]
i = 0
for e in menu:
    if e == "BreakFast:":
        i = 0
    elif e == "Lunch:":
        i = 1
    elif e == "EveningSnacks:":
        i = 2
    elif e == "Dinner:":
        i = 3
    else:
        out[i].append(e)

# create the html
t = time.localtime()
timestamp = f"Last Updated at {t.tm_hour:02}:{t.tm_min:02} on {t.tm_mday:02}-{t.tm_mon:02}-{t.tm_year}"
output = "---\nimport BaseLayout from '../layouts/Base.astro';\nimport '../styles/menu.css';\n\nconst pageTitle = 'Menu'\n---\n\n<BaseLayout title= { pageTitle }>\n"
output += f"<div class='header'>Today's Menu <span class='timestamp'>({timestamp})</span></div>\n"
output += "<div class='menu-cont'>\n"
output += "<div class='time'>\n"
output += "\t<span class='type'> Breakfast: </span>\n"
output += "\t\t<div class='items'>\n"
for item in out[0]:
    if item in specials:
        output += f"\t\t\t<span class='item special'>{item}</span>\n"
    else:
        output += f"\t\t\t<span class='item'>{item}</span>\n"
output += "\t\t</div>\n"
output += "</div>\n"
output += "<div class='time'>\n"
output += "\t<span class='type'> Lunch: </span>\n"
output += "\t\t<div class='items'>\n"
for item in out[1]:
    if item in specials:
        output += f"\t\t\t<span class='item special'>{item}</span>\n"
    else:
        output += f"\t\t\t<span class='item'>{item}</span>\n"
output += "\t\t</div>\n"
output += "</div>\n"
output += "<div class='time'>\n"
output += "\t<span class='type'> Snacks: </span>\n"
output += "\t\t<div class='items'>\n"
for item in out[2]:
    if item in specials:
        output += f"\t\t\t<span class='item special'>{item}</span>\n"
    else:
        output += f"\t\t\t<span class='item'>{item}</span>\n"
output += "\t\t</div>\n"
output += "</div>\n"
output += "<div class='time'>\n"
output += "\t<span class='type'> Dinner: </span>\n"
output += "\t\t<div class='items'>\n"
for item in out[3]:
    if item in specials:
        output += f"\t\t\t<span class='item special'>{item}</span>\n"
    else:
        output += f"\t\t\t<span class='item'>{item}</span>\n"
output += "\t\t</div>\n"
output += "</div>\n"
output+= "</div>\n"
output += "</BaseLayout>"
fh = open("src/pages/menu.astro", "w")
fh.write(output)
fh.close()