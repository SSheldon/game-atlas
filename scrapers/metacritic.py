from bs4 import BeautifulSoup
import urllib
import re

def get_score(game, soup):
    return soup.find('span', {'class':'score_value', 'property':'v:average'})
        #We will need to trim this somehow, but it returns the right score

def get_genre(game, soup):
    for span in soup.findAll('span', {'class': 'label'}):
        if span.string == 'Genre(s):':
            return span.findNext('span')

def get_release(game, soup):
    for span in soup.findAll('span', {'class': 'label'}):
        if span.string == 'Release Date:':
            return span.findNext('span')

def getGameInfo(game):
    url = urllib.urlopen("http://www.metacritic.com/game/xbox-360/" + game)

    soup = BeautifulSoup(url)

    print get_score(game, soup)
    print get_genre(game, soup)
    print get_release(game, soup)
def main():
    getGameInfo('halo-4')
if __name__ == '__main__': 
     main() 
