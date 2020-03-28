import requests
from bs4 import BeautifulSoup
from Card import Card

# list_of_cards is going to contain all the jobs which are stored as a Card class
list_of_cards = []  
page_counter = 1

# the base page is always going to be the same, only the later part is going to differ (link)
base_page = 'https://www.simplyhired.com'
# this is the link of the first page
link = '/search?q=marketing&l=New+Orleans%2C+LA&pn=&job=D6iraakU-GxMN-ufAR2E3a_4gB0LkhWWOmshmTSiCiAqZ8GutM9ZJw'

while(True):
    # Show current page
    print('page: {}'.format(page_counter))
    page_counter += 1

    # Show current Link
    print('{}{}'.format(base_page,link))

    # Get data from the link
    data = requests.get('{}{}'.format(base_page,link))
    soup = BeautifulSoup(data.text, 'html.parser')

    # Get all articles (cards) in the page
    for article in soup.findAll('article'):
        # Get info (title, location, ammount, and description) for each one of them
        title = article.find('div', { 'class': 'jobposting-title-container'}).text
        location = article.find('span', { 'class': 'JobPosting-labelWithIcon jobposting-company'}).text
        ammount = article.find('span', { 'class': 'jobposting-salary'})
        description = article.find('p', { 'class': 'jobposting-snippet'}).text
        # sometimes there is no salary
        if ammount is None:
            ammount = "unknown"
        else:
            ammount = ammount.text
        
        # add a new Card to the list of cards with the current values
        curr_card = Card(title, location, ammount, description)
        list_of_cards.append(curr_card)
    # get the new link with the '->' that's in the page
    link = soup.find('a', { 'class': 'next-pagination'})
    # if it doesn't have one, it means we have reached the end page so we break out of the while loop
    if link is None:
        break
    link = link['href']

# Now we record each statement on the file named jobs.txt
f = open("jobs.txt","w")
for card in list_of_cards:
    f.write(card.__str__())
    f.write('\n')
f.close()