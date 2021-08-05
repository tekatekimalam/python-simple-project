import requests
from bs4 import BeautifulSoup as bs

username = input('Masukkan nama: ')
url = f'https://github.com/'+username

r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image_link = soup.find('img', {'alt': 'Avatar'})['src'] 
print(profile_image_link)