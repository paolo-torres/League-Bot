from decimal import *

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