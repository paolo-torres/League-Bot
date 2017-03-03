import requests
import time
from reference import key
from match import get10MatchIDs
from info import getSummonerInformation
from wins import getMostWinsChampion
from kda import getGamesWinsLossesKDA
from keys import getChampionKey
from names import getChampionName
from items import getItemNames
from spells import getSummonerSpellName
from twitter import tweetRTLike

def meetsRequirements(summonerName):
	print "Loading: 10%"
	requestSummonerID = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=" + key)
	if (requestSummonerID.status_code == 200):
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
		if (not potentialChampions):
			return False
		requestStats = requests.get('https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/' + str(summonerID) + '/ranked?api_key=' + key)
		if (requestStats.status_code == 200):
			statsJSON = requestStats.json()
			highestChampionID = getMostWinsChampion(statsJSON, potentialChampions)
			data = getGamesWinsLossesKDA(statsJSON, highestChampionID)
			games = data[0]
			wins = data[1]
			if (wins == 0):
				return False
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