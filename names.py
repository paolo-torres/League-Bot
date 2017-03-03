import requests
from reference import key

def getChampionName(ID):
	print "Loading: 70%"
	requestChampionID = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(ID) + "?api_key=" + key)
	if (requestChampionID.status_code == 200):
		ChampionIDJSON = requestChampionID.json()
		if (ChampionIDJSON["name"] == "Aurelion Sol"):
			ChampionIDJSON["name"] = "Aurelion"
		if (ChampionIDJSON["name"] == "Blitzcrank"):
			ChampionIDJSON["name"] = "Blitz"
		if (ChampionIDJSON["name"] == "Caitlyn"):
			ChampionIDJSON["name"] = "Cait"
		if (ChampionIDJSON["name"] == "Cassiopeia"):
			ChampionIDJSON["name"] = "Cass"
		if (ChampionIDJSON["name"] == "Cho'Gath"):
			ChampionIDJSON["name"] = "Cho"
		if (ChampionIDJSON["name"] == "Dr. Mundo"):
			ChampionIDJSON["name"] = "Mundo"
		if (ChampionIDJSON["name"] == "Evelynn"):
			ChampionIDJSON["name"] = "Eve"
		if (ChampionIDJSON["name"] == "Fiddlesticks"):
			ChampionIDJSON["name"] = "Fiddle"
		if (ChampionIDJSON["name"] == "Gangplank"):
			ChampionIDJSON["name"] = "GP"
		if (ChampionIDJSON["name"] == "Heimerdinger"):
			ChampionIDJSON["name"] = "Donger"
		if (ChampionIDJSON["name"] == "Jarvan IV"):
			ChampionIDJSON["name"] = "J4"
		if (ChampionIDJSON["name"] == "Katarina"):
			ChampionIDJSON["name"] = "Kat"
		if (ChampionIDJSON["name"] == "Kog'Maw"):
			ChampionIDJSON["name"] = "Kog"
		if (ChampionIDJSON["name"] == "LeBlanc"):
			ChampionIDJSON["name"] = "LB"
		if (ChampionIDJSON["name"] == "Master Yi"):
			ChampionIDJSON["name"] = "Yi"
		if (ChampionIDJSON["name"] == "Miss Fortune"):
			ChampionIDJSON["name"] = "MF"
		if (ChampionIDJSON["name"] == "Morgana"):
			ChampionIDJSON["name"] = "Morg"
		if (ChampionIDJSON["name"] == "Orianna"):
			ChampionIDJSON["name"] = "Ori"
		if (ChampionIDJSON["name"] == "Sejuani"):
			ChampionIDJSON["name"] = "Sej"
		if (ChampionIDJSON["name"] == "Shyvana"):
			ChampionIDJSON["name"] = "Shyv"
		if (ChampionIDJSON["name"] == "Tahm Kench"):
			ChampionIDJSON["name"] = "Tahm"
		if (ChampionIDJSON["name"] == "Tristana"):
			ChampionIDJSON["name"] = "Trist"
		if (ChampionIDJSON["name"] == "Tryndamere"):
			ChampionIDJSON["name"] = "Tryn"
		if (ChampionIDJSON["name"] == "Twisted Fate"):
			ChampionIDJSON["name"] = "TF"
		if (ChampionIDJSON["name"] == "Vladimir"):
			ChampionIDJSON["name"] = "Vlad"
		if (ChampionIDJSON["name"] == "Volibear"):
			ChampionIDJSON["name"] = "Voli"
		return ChampionIDJSON["name"]
	else:
		raise KeyError("Cound not connect when getting the name of the champion with the ID: " + str(highestChampionID))