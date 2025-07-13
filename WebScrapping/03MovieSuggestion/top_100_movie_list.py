from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/').text

wb_pg = BeautifulSoup(response, 'html.parser')

movie_title = wb_pg.find_all(name='h3' , class_ = 'title')
movie_title_txt = [each.getText() for each in movie_title]
movie_title_txt.reverse()

with open("41_DAY/movieList.txt", 'w', encoding="utf-8") as doc:
    for each in movie_title_txt :
        doc.write(f"{each}\n")

    
        