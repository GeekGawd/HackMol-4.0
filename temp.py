from bs4 import BeautifulSoup as BSoup
import requests


url = "https://musclewiki.com/Kettlebells/Male/Glutes"

r = requests.get(url)
htmlcontent = r.content

soup = BSoup(htmlcontent, 'html.parser')

parse_steps = soup.select("ol.steps-list")

parse_exercises = [exercise.text.strip() for exercise in soup.find_all("h3")]

data = soup.find_all("p")

pizza = list()

links = list()

for i in data:
    for link in i.find_all('a'):
        links.append(link.get('href'))

del links[0]
del links[-4: -1]
del links[-1]
print(links)

for i in data:
    if i.findChildren('strong'):
        pizza.append(i.text)

print(pizza)

for i in parse_steps:
    steps = [j.text for j in i if j != '\n']