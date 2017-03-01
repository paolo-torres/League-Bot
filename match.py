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