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
		if (item1 == 0 or item2 == 0 or item3 == 0 or item4 == 0 or item5 == 0 or item6 == 0):
			continue
		if participants["championId"] in potentialChampions:
			continue
		potentialChampions.append(participants["championId"])
		itemBuilds.append([item1, item2, item3, item4, item5, item6])
		summonerSpells.append([participants["spell1Id"], participants["spell2Id"]])
	return potentialChampions, itemBuilds, summonerSpells