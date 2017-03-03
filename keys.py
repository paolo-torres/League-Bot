import requests
from reference import key

def getChampionKey(ID):
	print "Loading: 60%"
	requestChampionID = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(ID) + "?api_key=" + key)
	if (requestChampionID.status_code == 200):
		ChampionIDJSON = requestChampionID.json()
		return ChampionIDJSON["key"]
	else:
		raise KeyError("Cound not connect when getting the key of the champion with the ID: " + str(highestChampionID))