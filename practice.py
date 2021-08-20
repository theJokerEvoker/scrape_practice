from bs4 import BeautifulSoup
import requests

# Start the session
session = requests.Session()

# Create the payload
payload = {'_username':'[]',
          '_password':'[]'
         }

# Post the payload to the site to log in
s = session.post("https://anilist.co/login", data = payload)

# Navigate to the next page and scrape the data
s = session.get('https://anilist.co/home')

soup = BeautifulSoup(s.content, 'html.parser')
results = soup.find(id = "app")
card_elements = results.find_all("div", class_ = "media-card")

for card_element in card_elements:
    title_element = card_element.find("a", class_ = "title")
    # card_image_element = card_element.find("a", class_ = "image")
    print(title_element.text.strip())
    # print(card_image_element)
    print()
