from bs4 import BeautifulSoup
import urllib
import re

def get_score(game, soup):
    return soup.find('span', {'class':'score_value', 'property':'v:average'}).string
        #We will need to trim this somehow, but it returns the right score

def get_genre(game, soup):
    for span in soup.findAll('span', {'class': 'label'}):
        if span.string == 'Genre(s):':
            return span.findNext('span').string

def get_release(game, soup):
    for span in soup.findAll('span', {'class': 'label'}):
        if span.string == 'Release Date:':
            return span.findNext('span').string

def getGameInfo(game, platform):
    url = urllib.urlopen("http://www.metacritic.com/game/" + platform +"/" + game)

    soup = BeautifulSoup(url)
    info_dict = {}

    info_dict['score'] = get_score(game, soup)
    info_dict['genre'] =  get_genre(game, soup)
    info_dict['release'] =  get_release(game, soup)

    return info_dict
def main():
    test = getGameInfo('bioshock-infinite', 'playstation-3')
    print test
if __name__ == '__main__': 
     main() 
