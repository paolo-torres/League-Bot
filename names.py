import requests
from reference import key

def getChampionName(ID):
	print "Loading: 70%"
	requestChampionID = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(ID) + "?api_key=" + key)
	if (requestChampionID.status_code == 200):
		ChampionIDJSON = requestChampionID.json()
		if (ChampionIDJSON["name"] == "Alistar"):
			ChampionIDJSON["name"] = "Ali"
		if (ChampionIDJSON["name"] == "Amumu"):
			ChampionIDJSON["name"] = "Mumu"
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
		if (ChampionIDJSON["name"] == "Corki"):
			ChampionIDJSON["name"] = "Cork"
		if (ChampionIDJSON["name"] == "Dr. Mundo"):
			ChampionIDJSON["name"] = "Mundo"
		if (ChampionIDJSON["name"] == "Evelynn"):
			ChampionIDJSON["name"] = "Eve"
		if (ChampionIDJSON["name"] == "Ezreal"):
			ChampionIDJSON["name"] = "Ez"
		if (ChampionIDJSON["name"] == "Fiddlesticks"):
			ChampionIDJSON["name"] = "Fiddle"
		if (ChampionIDJSON["name"] == "Gangplank"):
			ChampionIDJSON["name"] = "GP"
		if (ChampionIDJSON["name"] == "Gragas"):
			ChampionIDJSON["name"] = "Grag"
		if (ChampionIDJSON["name"] == "Hecarim"):
			ChampionIDJSON["name"] = "Hec"
		if (ChampionIDJSON["name"] == "Heimerdinger"):
			ChampionIDJSON["name"] = "Donger"
		if (ChampionIDJSON["name"] == "Jarvan IV"):
			ChampionIDJSON["name"] = "J4"
		if (ChampionIDJSON["name"] == "Kalista"):
			ChampionIDJSON["name"] = "Kali"
		if (ChampionIDJSON["name"] == "Karthus"):
			ChampionIDJSON["name"] = "Karth"
		if (ChampionIDJSON["name"] == "Kassadin"):
			ChampionIDJSON["name"] = "Kass"
		if (ChampionIDJSON["name"] == "Katarina"):
			ChampionIDJSON["name"] = "Kat"
		if (ChampionIDJSON["name"] == "Kha'Zix"):
			ChampionIDJSON["name"] = "Kha"
		if (ChampionIDJSON["name"] == "Kog'Maw"):
			ChampionIDJSON["name"] = "Kog"
		if (ChampionIDJSON["name"] == "LeBlanc"):
			ChampionIDJSON["name"] = "LB"
		if (ChampionIDJSON["name"] == "Lee Sin"):
			ChampionIDJSON["name"] = "Lee"
		if (ChampionIDJSON["name"] == "Leona"):
			ChampionIDJSON["name"] = "Leo"
		if (ChampionIDJSON["name"] == "Lissandra"):
			ChampionIDJSON["name"] = "Liss"
		if (ChampionIDJSON["name"] == "Malphite"):
			ChampionIDJSON["name"] = "Malph"
		if (ChampionIDJSON["name"] == "Malzahar"):
			ChampionIDJSON["name"] = "Malz"
		if (ChampionIDJSON["name"] == "Maokai"):
			ChampionIDJSON["name"] = "Mao"
		if (ChampionIDJSON["name"] == "Master Yi"):
			ChampionIDJSON["name"] = "Yi"
		if (ChampionIDJSON["name"] == "Miss Fortune"):
			ChampionIDJSON["name"] = "MF"
		if (ChampionIDJSON["name"] == "Mordekaiser"):
			ChampionIDJSON["name"] = "Morde"
		if (ChampionIDJSON["name"] == "Morgana"):
			ChampionIDJSON["name"] = "Morg"
		if (ChampionIDJSON["name"] == "Nautilus"):
			ChampionIDJSON["name"] = "Naut"
		if (ChampionIDJSON["name"] == "Nidalee"):
			ChampionIDJSON["name"] = "Nid"
		if (ChampionIDJSON["name"] == "Nocturne"):
			ChampionIDJSON["name"] = "Noc"
		if (ChampionIDJSON["name"] == "Orianna"):
			ChampionIDJSON["name"] = "Ori"
		if (ChampionIDJSON["name"] == "Pantheon"):
			ChampionIDJSON["name"] = "Panth"
		if (ChampionIDJSON["name"] == "Rek'Sai"):
			ChampionIDJSON["name"] = "Rek"
		if (ChampionIDJSON["name"] == "Renekton"):
			ChampionIDJSON["name"] = "Renek"
		if (ChampionIDJSON["name"] == "Rengar"):
			ChampionIDJSON["name"] = "Reng"
		if (ChampionIDJSON["name"] == "Riven"):
			ChampionIDJSON["name"] = "Riv"
		if (ChampionIDJSON["name"] == "Sejuani"):
			ChampionIDJSON["name"] = "Sej"
		if (ChampionIDJSON["name"] == "Shyvana"):
			ChampionIDJSON["name"] = "Shyv"
		if (ChampionIDJSON["name"] == "Sivir"):
			ChampionIDJSON["name"] = "Siv"
		if (ChampionIDJSON["name"] == "Skarner"):
			ChampionIDJSON["name"] = "Skarn"
		if (ChampionIDJSON["name"] == "Soraka"):
			ChampionIDJSON["name"] = "Raka"
		if (ChampionIDJSON["name"] == "Tahm Kench"):
			ChampionIDJSON["name"] = "Tahm"
		if (ChampionIDJSON["name"] == "Tristana"):
			ChampionIDJSON["name"] = "Trist"
		if (ChampionIDJSON["name"] == "Tryndamere"):
			ChampionIDJSON["name"] = "Tryn"
		if (ChampionIDJSON["name"] == "Twisted Fate"):
			ChampionIDJSON["name"] = "TF"
		if (ChampionIDJSON["name"] == "Veigar"):
			ChampionIDJSON["name"] = "Veig"
		if (ChampionIDJSON["name"] == "Viktor"):
			ChampionIDJSON["name"] = "Vik"
		if (ChampionIDJSON["name"] == "Vladimir"):
			ChampionIDJSON["name"] = "Vlad"
		if (ChampionIDJSON["name"] == "Volibear"):
			ChampionIDJSON["name"] = "Voli"
		if (ChampionIDJSON["name"] == "Wukong"):
			ChampionIDJSON["name"] = "Wu"
		if (ChampionIDJSON["name"] == "Xin Zhao"):
			ChampionIDJSON["name"] = "Xin"
		if (ChampionIDJSON["name"] == "Yasuo"):
			ChampionIDJSON["name"] = "Yas"
		if (ChampionIDJSON["name"] == "Zilean"):
			ChampionIDJSON["name"] = "Zil"
		return ChampionIDJSON["name"]
	else:
		raise KeyError("Cound not connect when getting the name of the champion with the ID: " + str(highestChampionID))
