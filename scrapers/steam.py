import urllib2
import json
from xml.dom.minidom import parseString

def get_steamid(username):    
    xml = urllib2.urlopen('http://steamcommunity.com/id/' + username + '/?xml=1')
    data = xml.read()
    xml.close()
    dom = parseString(data)
    try:
        steamid = dom.getElementsByTagName('steamID64')[0].toxml()
        steamid = steamid.replace('<steamID64>','').replace('</steamID64>','')
    except IndexError, ex:
        steamid = None
    return steamid


def get_game_appids(username):
    games_appid_list = []
    api_key = '8FFA57C3004635970E3366E04EE2F8A0'
    steamid = get_steamid(username)
    if steamid == None:
        return None
    
    owned_games_url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=' + api_key + '&steamid=' + steamid + '&format=json'
    owned_games = urllib2.urlopen(owned_games_url)
    games = json.load(owned_games)
    for game in games['response']['games']:
        games_appid_list.append(str(game['appid']))
        
    return games_appid_list


def get_game_name(username, appid):
    api_key = '8FFA57C3004635970E3366E04EE2F8A0'
    steamid = get_steamid(username)
    # not happy with having to call get_steamid here. need to refactor this all a bit i think
    game_stats_url = 'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=' + appid + '&key=' + api_key + '&steamid=' + steamid
    # couldn't find a better/more reliable api call to get game name than this one
    try:
        game_stats = urllib2.urlopen(game_stats_url)
        stats = json.load(game_stats)
        name = stats['playerstats']['gameName']
        if name != '' and not 'ValveTestApp' in name:
            return name
        else:
            return None
    except ValueError, ex:
        return None
    except urllib2.URLError, ex:
        return None
    
    
def get_all_game_names(username):
    game_names = []
    appids = []
    api_key = '8FFA57C3004635970E3366E04EE2F8A0'
    steamid = get_steamid(username)
    if steamid == None:
        return game_names
    owned_games_url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=' + api_key + '&steamid=' + steamid + '&format=json'
    owned_games = urllib2.urlopen(owned_games_url)
    games = json.load(owned_games)
    for game in games['response']['games']:
        appids.append(str(game['appid']))
    for appid in appids:
        game_stats_url = 'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=' + appid + '&key=' + api_key + '&steamid=' + steamid
        try:
            game_stats = urllib2.urlopen(game_stats_url)
            stats = json.load(game_stats)
            name = stats['playerstats']['gameName']
            if name != '' and not 'ValveTestApp' in name:
                game_names.append(name)
            else:
                continue
        except ValueError, ex:
            continue
        except urllib2.URLError, ex:
            continue
    return game_names
