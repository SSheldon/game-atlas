from bs4 import BeautifulSoup
import urllib
import re

def get_score(soup):
    ret_val = soup.find('span', {'class':'score_value', 'property':'v:average'})
    if ret_val is None:
        return None
    else:
        return ret_val.string
def get_developer(soup):
    for span in soup.findAll('span', {'class': 'label'}):
        if span.string == 'Developer:':
            return span.findNext('span').string.strip()

def get_esrb(soup):
    for span in soup.findAll('span', {'class': 'label'}):
        if span.string == 'Rating:':
            return span.findNext('span').string

def get_genre(soup):
    for span in soup.findAll('span', {'class': 'label'}):
        if span.string == 'Genre(s):':
            return span.findNext('span').string

def get_publisher(soup):
    for span in soup.findAll('span', {'class': 'label'}):
        if span.string == 'Publisher:':
            return span.findNext('a').string.strip()

def get_release(soup):
    for span in soup.findAll('span', {'class': 'label'}):
        if span.string == 'Release Date:':
            return span.findNext('span').string

def get_name(soup):
    div = soup.find('div', {'class': 'product_title'})
    return div.findNext('a').string.strip()

def get_platform(soup):
    val = soup.find('span', {'class': 'platform'})
    return val.findNext('a').string.strip()

def get_other_platforms(soup):
    platforms = []
    for span in soup.findAll('span', {'class': 'label'}):
	    if span.string == 'Also On:':
		    span_next = span.findNext('span')
		    for a in span_next.findAll('a'):
			    platforms.append(a.string.strip())
    return platforms

def fix_string(s):
    s = s.lower()
    s = re.sub('[.!,;:]', '', s)
    s = s.replace(' ', '-')
    return s


def get_info(game, platform):
    game = fix_string(game)
    platform = fix_string(platform)
    
    url = urllib.urlopen("http://www.metacritic.com/game/" + platform +"/" + game)
    soups = [BeautifulSoup(url)]

    platforms = get_other_platforms(soups[0])
    for platform in platforms:
	url = urllib.urlopen("http://www.metacritic.com/game/" + fix_string(platform) + "/" + game)
	soups.append(BeautifulSoup(url))

    info_list = []
    for soup in soups:
        info_dict = {}
        info_dict['title'] = get_name(soup)
        info_dict['platform'] = get_platform(soup)
        info_dict['score'] = get_score(soup)
        info_dict['esrb'] = get_esrb(soup)
        info_dict['developer'] = get_developer(soup)
        info_dict['genre'] =  get_genre(soup)
        info_dict['publisher'] = get_publisher(soup)
        info_dict['release'] =  get_release(soup)
        if (info_dict['release'] != 'TBA'):
            info_list.append(info_dict)

    return info_list
