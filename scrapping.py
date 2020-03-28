import requests
from bs4 import BeautifulSoup
from Card import Card

list_of_cards = []  
base_page = 'https://www.simplyhired.com'

page_counter = 1

link = '/search?q=marketing&l=New+Orleans%2C+LA&pn=&job=D6iraakU-GxMN-ufAR2E3a_4gB0LkhWWOmshmTSiCiAqZ8GutM9ZJw'

while(link != None):
    print('page: {}'.format(page_counter))
    page_counter += 1

    print('{}{}'.format(base_page,link))

    data = requests.get('{}{}'.format(base_page,link))
    soup = BeautifulSoup(data.text, 'html.parser')

    for article in soup.findAll('article'):
        title = article.find('div', { 'class': 'jobposting-title-container'}).text
        location = article.find('span', { 'class': 'JobPosting-labelWithIcon jobposting-company'}).text
        ammount = article.find('span', { 'class': 'jobposting-salary'})

        if ammount is None:
            ammount = "unknown"
        else:
            ammount = ammount.text

        description = article.find('p', { 'class': 'jobposting-snippet'}).text
        curr_card = Card(title, location, ammount, description)
        list_of_cards.append(curr_card)
    
    link = soup.find('a', { 'class': 'next-pagination'})
    if link is None:
        break
    link = link['href']

f = open("jobs.txt","w")

for card in list_of_cards:
    f.write(card.__str__())
    f.write('\n')

f.close()