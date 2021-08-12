from pprint import pprint
import requests
names_intelligence = {}
names = ['Hulk', 'Captain America', 'Thanos']
url = "https://superheroapi.com/api/2619421814940190/"
for name in names:
    response = requests.get(url+'search/' + name)
    intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
    names_intelligence[name] = intelligence
# pprint(response.headers)
print(names_intelligence)
intelligence_max = sorted(names_intelligence.items(), key=lambda x: x[1], reverse=True)[0]
print(intelligence_max)
print('Наибольший интелект \033[34m{0[1]}\033[0m, у супергероя \033[34m{0[0]}\033[0m (из списка сравнения)'.format(intelligence_max))