import requests
import time
import tweepy
import os
from random import shuffle
from credentials import *
from decimal import *

myFile = file("C:\School\University\League Bot\config.txt", "r")
configFile = myFile.readlines()
key = configFile[0].split("=")[1].rstrip("\n")
filepath = configFile[1].split("=")[1].rstrip("\n")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def main():
	print "Running Program"
	print "Loading: 0%"
	requestPlayers = requests.get("https://na.api.pvp.net/api/lol/na/v2.5/league/challenger?type=RANKED_SOLO_5x5&api_key=" + key)
	if(requestPlayers.status_code == 200):
		playersJSON = requestPlayers.json()
		potentialPlayers = []
		for i in range(len(playersJSON["entries"])):
			potentialPlayers.append(playersJSON["entries"][i]["playerOrTeamName"])
		shuffle(potentialPlayers)
		for i in potentialPlayers:
			if(meetsRequirements(i)):
				break
			time.sleep(20)
	else:
		print "Could not connect when getting challenger players"

def meetsRequirements(summonerName):
	print "Loading: 10%"
	requestSummonerID = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=" + key)
	if(requestSummonerID.status_code == 200):
		summonerIDJSON = requestSummonerID.json()
		summonerNameStripped = summonerName
		summonerNameStripped = summonerNameStripped.lower()
		summonerNameStripped = summonerNameStripped.encode('utf-8')
		summonerNameStripped = summonerNameStripped.replace(" ", "")
		try:
			summonerID = summonerIDJSON[summonerNameStripped]["id"]
		except KeyError:
			return False
		requestMatchHistory = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner/" + str(summonerID) + "?api_key=" + key)
		matchIDs = get10MatchIDs(requestMatchHistory.json())
		matchInformationJSON = []
		for IDs in matchIDs:
			time.sleep(3)
			requestMatch = requests.get('https://na.api.pvp.net/api/lol/na/v2.2/match/' + str(IDs) + '?api_key=' + key)
			try:
				matchInformationJSON.append(requestMatch)
			except Exception as e:
				print requestMatch.text
		potentialChampions, itemBuild, summonerSpells = getSummonerInformation(matchInformationJSON)
		if(not potentialChampions):
			return False
		requestStats = requests.get('https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/' + str(summonerID) + '/ranked?api_key=' + key)
		if(requestStats.status_code == 200):
			statsJSON = requestStats.json()
			highestChampionID = getMostWinsChampion(statsJSON, potentialChampions)
			data = getGamesWinsLossesKDA(statsJSON, highestChampionID)
			games = data[0]
			wins = data[1]
			losses = data[2]
			kills = data[3]
			deaths = data[4]
			assists = data[5]
			winRate = int((float(wins) / (wins + losses)) * 100)
			KDA = (kills + assists) / deaths
			championID = highestChampionID
			location = potentialChampions.index(championID)
			itemBuild = itemBuild[location]
			summonerSpell1 = summonerSpells[location][0]
			summonerSpell2 = summonerSpells[location][1]
			championKey = getChampionKey(championID)
			championName = getChampionName(championID)
			itemBuildName = getItemNames(itemBuild)
			spellName1, spellName2 = getSummonerSpellName(summonerSpell1, summonerSpell2)
			tweetRTLike(summonerName, championName, winRate, KDA, spellName1, spellName2, itemBuildName[0], itemBuildName[1], itemBuildName[2], itemBuildName[3], itemBuildName[4], itemBuildName[5], championKey)
			return True
		else:
			print "Cound not connect when getting ranked stats for " + summonerName
	else:
		print requestSummonerID.text
		print "Could not connect when getting the ID for " + summonerName
	return False

def get10MatchIDs(j):
	print "Loading: 20%"
	matches = []
	count = 0
	for i in range(len(j)):
		try:
			curr = j["matches"][i]
		except KeyError:
			continue
		if(curr["queue"] == "TEAM_BUILDER_RANKED_SOLO"):
			matches.append(curr["matchId"])
			count += 1
		if(count == 30):
			break
	return matches

def getSummonerInformation(jList):
	print "Loading: 30%"
	potentialChampions = []
	itemBuilds = []
	summonerSpells = []
	for j in jList:
		j = j.json()
		try:
			participants = j["participants"][0]
		except KeyError:
			continue
		stats = participants["stats"]
		item1 = stats.get("item0", 0)
		item2 = stats.get("item1", 0)
		item3 = stats.get("item2", 0)
		item4 = stats.get("item3", 0)
		item5 = stats.get("item4", 0)
		item6 = stats.get("item5", 0)
		if(item1 == 0 or item2 == 0 or item3 == 0 or item4 == 0 or item5 == 0 or item6 == 0):
			continue
		if participants["championId"] in potentialChampions:
			continue
		potentialChampions.append(participants["championId"])
		itemBuilds.append([item1, item2, item3, item4, item5, item6])
		summonerSpells.append([participants["spell1Id"], participants["spell2Id"]])
	return potentialChampions, itemBuilds, summonerSpells

def getMostWinsChampion(j, potentialChampions):
	print "Loading: 40%"
	championData = {}
	for i in range(len(j["champions"])):
		championID = j["champions"][i]["id"]
		if championID in potentialChampions:
			championData[championID] = j["champions"][i]["stats"]
	highestChampionID = -1
	highestWins = -1
	for i in potentialChampions:
		if i in championData:
			if(championData[i]["totalSessionsWon"] > highestWins):
				highestWins = championData[i]["totalSessionsWon"]
				highestChampionID = i
		else:
			continue
	if(highestChampionID != -1):
		return highestChampionID
	else:
		return potentialChampions[0]

def getGamesWinsLossesKDA(j, champion):
	print "Loading: 50%"
	for i in range(len(j["champions"])):
		if(j["champions"][i]["id"] == champion):
			champData = j["champions"][i]["stats"]
			getcontext().prec = 2
			kills = Decimal(champData["totalChampionKills"]) / Decimal(champData["totalSessionsPlayed"])
			deaths = Decimal(champData["totalDeathsPerSession"]) / Decimal(champData["totalSessionsPlayed"])
			assists = Decimal(champData["totalAssists"]) / Decimal(champData["totalSessionsPlayed"])
			return [champData["totalSessionsPlayed"], champData["totalSessionsWon"], champData["totalSessionsLost"], kills, deaths, assists]
	champData = j["champions"][i]["stats"]
	getcontext().prec = 2
	kills = Decimal(champData["totalChampionKills"]) / Decimal(champData["totalSessionsPlayed"])
	deaths = Decimal(champData["totalDeathsPerSession"]) / Decimal(champData["totalSessionsPlayed"])
	assists = Decimal(champData["totalAssists"]) / Decimal(champData["totalSessionsPlayed"])
	return [champData["totalSessionsPlayed"], champData["totalSessionsWon"], champData["totalSessionsLost"], kills, deaths, assists]

def getChampionKey(ID):
	print "Loading: 60%"
	requestChampionID = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(ID) + "?api_key=" + key)
	if(requestChampionID.status_code == 200):
		ChampionIDJSON = requestChampionID.json()
		return ChampionIDJSON["key"]
	else:
		raise KeyError("Cound not connect when getting the key of the champion with the ID: " + str(highestChampionID))

def getChampionName(ID):
	print "Loading: 70%"
	requestChampionID = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(ID) + "?api_key=" + key)
	if(requestChampionID.status_code == 200):
		ChampionIDJSON = requestChampionID.json()
		return ChampionIDJSON["name"]
	else:
		raise KeyError("Cound not connect when getting the name of the champion with the ID: " + str(highestChampionID))

def getItemNames(itemBuild):
	print "Loading: 80%"
	itemNames = []
	for i in range(len(itemBuild)):
		item = itemBuild[i]
		requestItem = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/" + str(item) + "?api_key=" + key)
		if(requestItem.status_code == 200):
			itemNames.append(requestItem.json()["name"])
			if(itemNames[i] == "Abyssal Scepter"):
				itemNames[i] = "Abyssal"
			elif(itemNames[i] == "Aegis of the Legion"):
				itemNames[i] = "Aegis"
			elif(itemNames[i] == "Aether Wisp"):
				itemNames[i] = "Aether"
			elif(itemNames[i] == "Amplifying Tome"):
				itemNames[i] = "Tome"
			elif(itemNames[i] == "Ardent Censer"):
				itemNames[i] = "Ardent"
			elif(itemNames[i] == "Athene's Unholy Grail"):
				itemNames[i] = "Athene's"
			elif(itemNames[i] == "B. F. Sword"):
				itemNames[i] = "BF"
			elif(itemNames[i] == "Banner of Command"):
				itemNames[i] = "Banner"
			elif(itemNames[i] == "Banshee's Veil"):
				itemNames[i] = "Banshee's"
			elif(itemNames[i] == "Berserker's Greaves"):
				itemNames[i] = "Greaves"
			elif(itemNames[i] == "Bilgewater Cutlass"):
				itemNames[i] = "Cutlass"
			elif(itemNames[i] == "Blade of the Ruined King"):
				itemNames[i] = "BORK"
			elif(itemNames[i] == "Blasting Wand"):
				itemNames[i] = "B Wand"
			elif(itemNames[i] == "Boots of Speed"):
				itemNames[i] = "Boots"
			elif(itemNames[i] == "Boots of Mobility"):
				itemNames[i] = "Mobis"
			elif(itemNames[i] == "Boots of Swiftness"):
				itemNames[i] = "Swiftys"
			elif(itemNames[i] == "Catalyst of Aeons"):
				itemNames[i] = "Catalyst"
			elif(itemNames[i] == "Caulfield's Warhammer"):
				itemNames[i] = "Warhammer"
			elif(itemNames[i] == "Chalice of Harmony"):
				itemNames[i] = "Chalice"
			elif(itemNames[i] == "Chain Vest"):
				itemNames[i] = "C Vest"
			elif(itemNames[i] == "Cloth Armor"):
				itemNames[i] = "Cloth"
			elif(itemNames[i] == "Control Ward"):
				itemNames[i] = "Ward"
			elif(itemNames[i] == "Corrupting Potion"):
				itemNames[i] = "Corrupt Pot"
			elif(itemNames[i] == "Crystalline Bracer"):
				itemNames[i] = "C Bracer"
			elif(itemNames[i] == "Dead Man's Plate"):
				itemNames[i] = "Dead Man's"
			elif(itemNames[i] == "Doran's Blade"):
				itemNames[i] = "D Blade"
			elif(itemNames[i] == "Doran's Ring"):
				itemNames[i] = "D Ring"
			elif(itemNames[i] == "Doran's Shield"):
				itemNames[i] = "D Shield"
			elif(itemNames[i] == "Duskblade of Draktharr"):
				itemNames[i] = "Duskblade"
			elif(itemNames[i] == "Edge of Night"):
				itemNames[i] = "EoN"
			elif(itemNames[i] == "Executioner's Calling"):
				itemNames[i] = "Executioner's"
			elif(itemNames[i] == "Enchantment: Bloodrazor"):
				itemNames[i] = "Bloodrazor"
			elif(itemNames[i] == "Enchantment: Cinderhulk"):
				itemNames[i] = "Cinderhulk"
			elif(itemNames[i] == "Enchantment: Runic Echoes"):
				itemNames[i] = "Runic"
			elif(itemNames[i] == "Enchantment: Warrior"):
				itemNames[i] = "Warrior"
			elif(itemNames[i] == "Essence Reaver"):
				itemNames[i] = "Essence"
			elif(itemNames[i] == "Eye of the Equinox"):
				itemNames[i] = "Equinox"
			elif(itemNames[i] == "Eye of the Oasis"):
				itemNames[i] = "Oasis"
			elif(itemNames[i] == "Eye of the Watchers"):
				itemNames[i] = "Watchers"
			elif(itemNames[i] == "Face of the Mountain"):
				itemNames[i] = "FotM"
			elif(itemNames[i] == "Fiendish Codex"):
				itemNames[i] = "Codex"
			elif(itemNames[i] == "Frost Queen's Claim"):
				itemNames[i] = "Frost Queen's"
			elif(itemNames[i] == "Frozen Mallet"):
				itemNames[i] = "Mallet"
			elif(itemNames[i] == "Guardian Angel"):
				itemNames[i] = "GA"
			elif(itemNames[i] == "Giant's Belt"):
				itemNames[i] = "G Belt"
			elif(itemNames[i] == "Guinsoo's Rageblade"):
				itemNames[i] = "Guinsoo's"
			elif(itemNames[i] == "Haunting Guise"):
				itemNames[i] = "Guise"
			elif(itemNames[i] == "Health Potion"):
				itemNames[i] = "Health Pot"
			elif(itemNames[i] == "Hextech GLP-800"):
				itemNames[i] = "GLP-800"
			elif(itemNames[i] == "Hextech Gunblade"):
				itemNames[i] = "Gunblade"
			elif(itemNames[i] == "Hextech Protobelt-01"):
				itemNames[i] = "Protobelt"
			elif(itemNames[i] == "Hunter's Potion"):
				itemNames[i] = "Hunter's Pot"
			elif(itemNames[i] == "Iceborn Gauntlet"):
				itemNames[i] = "Iceborn"
			elif(itemNames[i] == "Infinity Edge"):
				itemNames[i] = "IE"
			elif(itemNames[i] == "Ionian Boots of Lucidity"):
				itemNames[i] = "Ionians"
			elif(itemNames[i] == "Jaurim's Fist"):
				itemNames[i] = "Jaurim's"
			elif(itemNames[i] == "Kircheis Shard"):
				itemNames[i] = "Kircheis"
			elif(itemNames[i] == "Last Whisper"):
				itemNames[i] = "LW"
			elif(itemNames[i] == "Liandry's Torment"):
				itemNames[i] = "Liandry's"
			elif(itemNames[i] == "Locket of the Iron Solari"):
				itemNames[i] = "Locket"
			elif(itemNames[i] == "Long Sword"):
				itemNames[i] = "L Sword"
			elif(itemNames[i] == "Lord Dominik's Regards"):
				itemNames[i] = "LDR"
			elif(itemNames[i] == "Luden's Echo"):
				itemNames[i] = "Luden's"
			elif(itemNames[i] == "Maw of Malmortius"):
				itemNames[i] = "Maw"
			elif(itemNames[i] == "Mejai's Soulstealer"):
				itemNames[i] = "Mejai's"
			elif(itemNames[i] == "Mercurial Scimitar"):
				itemNames[i] = "Merc Scim"
			elif(itemNames[i] == "Mercury's Treads"):
				itemNames[i] = "Merc Treads"
			elif(itemNames[i] == "Mikael's Crucible"):
				itemNames[i] = "Mikael's"
			elif(itemNames[i] == "Morellonomicon"):
				itemNames[i] = "Morello"
			elif(itemNames[i] == "Mortal Reminder"):
				itemNames[i] = "M Reminder"
			elif(itemNames[i] == "Nashor's Tooth"):
				itemNames[i] = "Nashor's"
			elif(itemNames[i] == "Needlessly Large Rod"):
				itemNames[i] = "Large Rod"
			elif(itemNames[i] == "Negatron Cloak"):
				itemNames[i] = "Negatron"
			elif(itemNames[i] == "Ninja Tabi"):
				itemNames[i] = "Tabis"
			elif(itemNames[i] == "Null-Magic Mantle"):
				itemNames[i] = "N-M Mantle"
			elif(itemNames[i] == "Phantom Dancer"):
				itemNames[i] = "PD"
			elif(itemNames[i] == "Quicksilver Sash"):
				itemNames[i] = "QSS"
			elif(itemNames[i] == "Rabadon's Deathcap"):
				itemNames[i] = "Rabadon's"
			elif(itemNames[i] == "Randuin's Omen"):
				itemNames[i] = "Randuin's"
			elif(itemNames[i] == "Rapid Firecannon"):
				itemNames[i] = "RFC"
			elif(itemNames[i] == "Ravenous Hydra"):
				itemNames[i] = "Ravenous"
			elif(itemNames[i] == "Refillable Potion"):
				itemNames[i] = "Refill Pot"
			elif(itemNames[i] == "Relic Shield"):
				itemNames[i] = "Relic"
			elif(itemNames[i] == "Rod of Ages"):
				itemNames[i] = "RoA"
			elif(itemNames[i] == "Ruby Sightstone"):
				itemNames[i] = "Ruby S Stone"
			elif(itemNames[i] == "Runaan's Hurricane"):
				itemNames[i] = "Runaan's"
			elif(itemNames[i] == "Rylai's Crystal Scepter"):
				itemNames[i] = "Rylai's"
			elif(itemNames[i] == "Seeker's Armguard"):
				itemNames[i] = "Seeker's"
			elif(itemNames[i] == "Seraph's Embrace"):
				itemNames[i] = "Seraph's"
			elif(itemNames[i] == "Serrated Dirk"):
				itemNames[i] = "S Dirk"
			elif(itemNames[i] == "Sightstone"):
				itemNames[i] = "S Stone"
			elif(itemNames[i] == "Sorcerer's Shoes"):
				itemNames[i] = "Sorcs"
			elif(itemNames[i] == "Spectre's Cowl"):
				itemNames[i] = "Spectre's"
			elif(itemNames[i] == "Spellthief's Edge"):
				itemNames[i] = "Spellthief's"
			elif(itemNames[i] == "Spirit Visage"):
				itemNames[i] = "Visage"
			elif(itemNames[i] == "Statikk Shiv"):
				itemNames[i] = "Shiv"
			elif(itemNames[i] == "Sterak's Gage"):
				itemNames[i] = "Sterak's"
			elif(itemNames[i] == "Sunfire Cape"):
				itemNames[i] = "Sunfire"
			elif(itemNames[i] == "Talisman of Ascension"):
				itemNames[i] = "Talisman"
			elif(itemNames[i] == "Targon's Brace"):
				itemNames[i] = "Targon's"
			elif(itemNames[i] == "Tear of the Goddess"):
				itemNames[i] = "Tear"
			elif(itemNames[i] == "The Black Cleaver"):
				itemNames[i] = "Cleaver"
			elif(itemNames[i] == "The Bloodthirster"):
				itemNames[i] = "BT"
			elif(itemNames[i] == "The Dark Seal"):
				itemNames[i] = "Dark Seal"
			elif(itemNames[i] == "The Hex Core mk-1"):
				itemNames[i] = "Hex Core mk-1"
			elif(itemNames[i] == "The Hex Core mk-2"):
				itemNames[i] = "Hex Core mk-2"
			elif(itemNames[i] == "Titanic Hydra"):
				itemNames[i] = "Titanic"
			elif(itemNames[i] == "Total Biscuit of Rejuvenation"):
				itemNames[i] = "Biscuits"
			elif(itemNames[i] == "Trinity Force"):
				itemNames[i] = "Tri Force"
			elif(itemNames[i] == "Vampiric Scepter"):
				itemNames[i] = "Vamp Scepter"
			elif(itemNames[i] == "Void Staff"):
				itemNames[i] = "Void"
			elif(itemNames[i] == "Warden's Mail"):
				itemNames[i] = "Warden's"
			elif(itemNames[i] == "Warmog's Armor"):
				itemNames[i] = "Warmog's"
			elif(itemNames[i] == "Youmuu's Ghostblade"):
				itemNames[i] = "Youmuu's"
			elif(itemNames[i] == "Zeke's Harbinger"):
				itemNames[i] = "Zeke's"
			elif(itemNames[i] == "Zhonya's Hourglass"):
				itemNames[i] = "Zhonya's"
			elif(itemNames[i] == "Zz'Rot Portal"):
				itemNames[i] = "Zz'Rot"
		else:
			print "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/" + str(item) + "?api_key=" + key
			raise KeyError("Could not connect when getting the item ID: " + str(item))
	return itemNames

def getSummonerSpellName(summonerSpell1, summonerSpell2):
	print "Loading: 90%"
	requestSummonerSpell1 = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/summoner-spell/" + str(summonerSpell1) + "?api_key=" + key)
	requestSummonerSpell2 = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/summoner-spell/" + str(summonerSpell2) + "?api_key=" + key)
	if(requestSummonerSpell1.status_code == 200 and requestSummonerSpell2.status_code == 200):
		summonerSpell1JSON = requestSummonerSpell1.json()
		summonerSpell2JSON = requestSummonerSpell2.json()
		if(summonerSpell1JSON["name"] == "Exhaust"):
			summonerSpell1JSON["name"] = "Exh"
		elif(summonerSpell1JSON["name"] == "Ignite"):
			summonerSpell1JSON["name"] = "Ign"
		elif(summonerSpell1JSON["name"] == "Teleport"):
			summonerSpell1JSON["name"] = "TP"
		if(summonerSpell2JSON["name"] == "Exhaust"):
			summonerSpell2JSON["name"] = "Exh"
		elif(summonerSpell2JSON["name"] == "Ignite"):
			summonerSpell2JSON["name"] = "Ign"
		elif(summonerSpell2JSON["name"] == "Teleport"):
			summonerSpell2JSON["name"] = "TP"
		return summonerSpell1JSON["name"], summonerSpell2JSON["name"]
	else:
		raise KeyError("Could not connect when getting the summoner spell ID " + str(summonerSpell1) + " or " + str(summonerSpell2))

def tweetRTLike(summonerName, championName, winRate, KDA, sum1, sum2, item1, item2, item3, item4, item5, item6, championKey):
	print "Loading: 100%"
	print "Done"
	leagueInformation = "Name: %s\nChamp: %s\nWin Rate: %s%%\nKDA: %s\nSums: %s, %s\nItems: %s, %s, %s, %s, %s, %s" % (summonerName, championName, winRate, KDA, sum1, sum2, item1, item2, item3, item4, item5, item6)
	print leagueInformation
	posts = api.user_timeline(screen_name = "@lolesports", count = 1)
	for post in posts:
		api.retweet(post.id)
		api.create_favorite(post.id)
		print "Retweeted LoL Esports"
	outputFile = open("output.txt", "w")
	outputFile.write(leagueInformation)
	outputFile = open("output.txt", "r")
	tweetInformation = outputFile.read()
	imageFileName = "championImage.jpg"
	requestChampionImage = requests.get("http://ddragon.leagueoflegends.com/cdn/img/champion/splash/" + championKey + "_0.jpg", stream = True)
	if(requestChampionImage.status_code == 200):
		with open(imageFileName, "wb") as image:
			for chunk in requestChampionImage:
				image.write(chunk)
		api.update_with_media(imageFileName, status = tweetInformation)
		print "Tweeted"
		os.remove(imageFileName)
	else:
		print "Could not download image"
	outputFile.close()

if __name__ == "__main__":
	main()
