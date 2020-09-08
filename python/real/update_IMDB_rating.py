from bs4 import BeautifulSoup
 
import requests
import sys
 
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text)
tr = soup.findChildren("tr")
tr = iter(tr)
next(tr)
print tr
count  = 0 
#import pdb;pdb.set_trace()
for movie in tr:
    if count == 250:
        print movie
        break
    title = movie.find('td', {'class': 'titleColumn'} ).find('a').contents[0]
    year = movie.find('td', {'class': 'titleColumn'} ).find('span', {'class': 'secondaryInfo'}).contents[0]
    rating = movie.find('td', {'class': 'ratingColumn imdbRating'} ).find('strong').contents[0]
    row = title + ' - ' + year + ' ' + ' ' + rating
    print(row)
    count = count +1

