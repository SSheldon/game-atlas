import urllib2
from xml.dom.minidom import parseString

def get_games(gamertag):
    games = []
    xml = urllib2.urlopen("https://xboxapi.com/xml/games/" + gamertag)
    data = xml.read()
    xml.close()
    dom = parseString(data)
    x = dom.documentElement.childNodes
    for i in range(0,x.length - 3):
        game = dom.getElementsByTagName('Name')[i].toxml()
        game = game.replace('<Name>','').replace('</Name>','')
        games.append(game)
    return games