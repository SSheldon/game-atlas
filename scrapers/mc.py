from BeautifulSoup import BeautifulSoup
import urllib
import re

def get_score(game):
	url = urllib.urlopen("http://www.metacritic.com/game/xbox-360/" + game)

	soup = BeautifulSoup(url)

	for span in soup.findAll('span', {'class':'score_value', 'property':'v:average'}):
		#We will need to trim this somehow, but it returns the right score
		return span

