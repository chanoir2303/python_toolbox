from blizzardapi import BlizzardApi
import json

api_client = BlizzardApi("client_id", "client_secret")


def get_ladder():
    y = api_client.wow.game_data.get_pvp_leaderboard('eu', 'en_EU', 27, '3v3')

    x = open('test_ladder.json', 'a+')
    x.write(json.dumps({'ladder': y}))
    x.close()


def find_user(user):
    with open('test_ladder.json') as f:
        data = json.load(f)

    for i in data['ladder']['entries']:
        if user in data['ladder']['entries'][0]['character']['name']:
            print('ok')


def display_ladder():
    with open('test_ladder.json') as f:
        data = json.load(f)

    for i in data['ladder']['entries'][0:10]:
        print(i['character']['name'])
        print(i['character']['realm']['slug'])
        print(i['faction']['type'])
        print('rank:', i['rank'])
        print('rating:', i['rating'])
        print('played:', i['season_match_statistics']['played'])
        print('won:', i['season_match_statistics']['won'])
        print('lost:', i['season_match_statistics']['lost'])
        print('______________________________')

