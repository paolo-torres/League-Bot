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