import requests
import os

lan = ['deDE','enUS','esES','esMX','frFR','itIT','jaJP','koKR','plPL','ptBR','ruRU','thTH','zhCN','zhTW']

for localization in lan:
    if not os.path.exists('./resources/'+localization):
        os.makedirs('./resources/'+localization)
    r = requests.get('https://api.hearthstonejson.com/v1/latest/'+localization+'/cards.collectible.json')
    with open('./resources/'+localization+'/cards.collectible.json','wb') as f:
        f.write(r.content)
