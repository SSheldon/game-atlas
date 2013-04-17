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

def get_achievement_percentage(stats):
    percentage = 0.0
    if 'achievements' in  stats['playerstats']:
        total_num = len(stats['playerstats']['achievements'])
        earned = 0
        for achievement in stats['playerstats']['achievements']:
            if achievement['achieved'] == 1:
                earned += 1.0
        percentage = (earned/total_num) * 100.0
    return percentage

def get_games(username):
    games_dict = {}
    api_key = '8FFA57C3004635970E3366E04EE2F8A0'
    steamid = get_steamid(username)
    if steamid == None:
        return None
    
    owned_games_url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=' + api_key + '&steamid=' + steamid + '&format=json'
    owned_games = urllib2.urlopen(owned_games_url)
    games = json.load(owned_games)
    for game in games['response']['games']:
        appid = str(game['appid'])
        game_stats_url = 'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=' + appid + '&key=' + api_key + '&steamid=' + steamid
        try:
            game_stats = urllib2.urlopen(game_stats_url)
            stats = json.load(game_stats)
            name = stats['playerstats']['gameName']
            if name != '' and not 'ValveTestApp' in name:
                percentage = get_achievement_percentage(stats)
                if not name in games_dict:
                    games_dict[name] = percentage
                else:
                    if percentage > games_dict[name]:
                        games_dict[name] = percentage
        except ValueError, ex:
            continue
        except urllib2.URLError, ex:
            continue
        
    return games_dict
        
    #for key in games_dict:
        #print key + ': ' + str(games_dict[key])





#if __name__ == '__main__':
    #get_games('Underground_Ace')
    #get_games('dark_knight_642')
    #get_games('Infinite010')
    
    
    