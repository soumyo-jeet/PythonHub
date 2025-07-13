import requests
from bs4 import BeautifulSoup

date = input("Which year whish to travel? YYYY-MM-DD: ")

url1 = f"https://www.billboard.com/charts/hot-100/{date}"


header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

billboard_response = requests.get(url=url1, headers=header)

soup = BeautifulSoup(billboard_response.text, 'html.parser')

top_songs = soup.select('ul li h3')

top_songs_h = []

try:
    for i in range (100):
        top_song_h = top_songs[i].getText().strip()
        top_songs_h.append(top_song_h)
except IndexError:
    print("Invalid Input!!!")
    top_songs_h = []

