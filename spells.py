import requests
from reference import key

def getSummonerSpellName(summonerSpell1, summonerSpell2):
	print "Loading: 90%"
	requestSummonerSpell1 = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/summoner-spell/" + str(summonerSpell1) + "?api_key=" + key)
	requestSummonerSpell2 = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/summoner-spell/" + str(summonerSpell2) + "?api_key=" + key)
	if (requestSummonerSpell1.status_code == 200 and requestSummonerSpell2.status_code == 200):
		summonerSpell1JSON = requestSummonerSpell1.json()
		summonerSpell2JSON = requestSummonerSpell2.json()
		if (summonerSpell1JSON["name"] == "Exhaust"):
			summonerSpell1JSON["name"] = "Exh"
		elif (summonerSpell1JSON["name"] == "Ignite"):
			summonerSpell1JSON["name"] = "Ign"
		elif (summonerSpell1JSON["name"] == "Teleport"):
			summonerSpell1JSON["name"] = "TP"
		if (summonerSpell2JSON["name"] == "Exhaust"):
			summonerSpell2JSON["name"] = "Exh"
		elif (summonerSpell2JSON["name"] == "Ignite"):
			summonerSpell2JSON["name"] = "Ign"
		elif (summonerSpell2JSON["name"] == "Teleport"):
			summonerSpell2JSON["name"] = "TP"
		return summonerSpell1JSON["name"], summonerSpell2JSON["name"]
	else:
		raise KeyError("Could not connect when getting the summoner spell ID " + str(summonerSpell1) + " or " + str(summonerSpell2))