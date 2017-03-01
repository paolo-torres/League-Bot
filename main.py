import requests
import time
from random import shuffle
from reference import key
from requirements import meetsRequirements

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

if __name__ == "__main__":
	main()