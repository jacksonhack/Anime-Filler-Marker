#!/usr/bin/env python

# From AnimVille project. See README.md for more details.

# Import necessary libraries
import requests
import bs4
import json
import shutil

# Rest of the code

# links = ['akame-ga-kill', 'another', 'ansatsu-kyoushitsu-assassination-classroom', 'attack-titan', 'beelzebub', 'berserk-2016', 
#     'black-clover', 'black-lagoon', 'bleach', 'blue-exorcist', 'boruto-naruto-next-generations', 'classroom-elite',
#     'code-geass', 'deadman-wonderland', 'death-note', 'demon-slayer-kimetsu-no-yaiba', 'devilman-crybaby', 
#     'dr-stone', 'dragon-ball', 'dragon-ball-gt', 'dragon-ball-heroes', 'dragon-ball-super', 'dragon-ball-z', 'elfen-lied', 
#     'erased', 'fairy-tail','fatestay-night', 'fatestay-night-unlimited-blade-works', 'fate-zero', 'fire-force', 
#     'shokugeki-no-soma', 'fruits-basket-2019', 'fullmetal-alchemist-brotherhood', 'gintama', 'goblin-slayer', 'gurren-lagann',
#     'haikyuu', 'high-school-dxd', 'highschoool-dead', 'hunter-x-hunter', 'jojos-bizarre-adventure-tv', 'jujutsu-kaisen', 
#     'kabaneri-iron-fortress', 'kill-la-kill', 'kingdom', 'kuroko’s-basketball', 'mob-psycho-100', 'my-hero-academia', 'naruto', 
#     'naruto-shippuden', 'one-piece', 'one-punch-man', 'parasyte-maxim', 'pokemon', 'prison-school', 
#     're-zero-starting-life-another-world', 'samurai-champloo', 'serial-experiments-lain', 'slam-dunk-0', 'steinsgate', 
#     'sword-art-online', 'sword-art-online-alicization', 'terror-resonance', 'devil-part-timer', 'god-high-school', 
#     'promised-neverland', 'nanatsu-no-taizai', 'tokyo-ghoul', 'tokyo-ghoul-re-0', 'vinland-saga']

def getJsons(link):

    result = requests.get('https://www.animefillerlist.com/shows/'+link)
    print(result)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    numbers = soup.select('td.Number')
    titles = soup.select('td.Title>a')
    types = soup.select('td.Type>span')
    dates = soup.select('td.Date')

    for i in range(len(numbers)): 
        numbers[i] = numbers[i].getText()
        titles[i] = titles[i].getText()
        types[i] = types[i].getText()
        dates[i] = dates[i].getText()

    anime = []
    for i in range(len(numbers)):
        if types[i] == 'Filler':
            y = 'red'
        else:
            y = 'green'
        x = {'id': numbers[i], 'title': titles[i], 'type': types[i], 'date': dates[i], 'class': y}
        anime.append(x)

    animeJSON = json.dumps(anime)

    f = open(link+'.json', 'w+')
    f.write(animeJSON)
    f.close()

    #shutil.move(link+'.json', '\\JSON')

getJsons('naruto')