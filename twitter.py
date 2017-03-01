import requests
import tweepy
import os
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweetRTLike(summonerName, championName, winRate, KDA, sum1, sum2, item1, item2, item3, item4, item5, item6, championKey):
	print "Loading: 100%"
	print "Done"
	leagueInformation = "Name: %s\nChamp: %s\nWin Rate: %s%%\nKDA: %s\nSums: %s, %s\nItems: %s, %s, %s, %s, %s, %s" % (summonerName, championName, winRate, KDA, sum1, sum2, item1, item2, item3, item4, item5, item6)
	print leagueInformation
	posts = api.user_timeline(screen_name = "@lolesports", count = 10)
	for post in posts:
		try:
			api.retweet(post.id)
			api.create_favorite(post.id)
		except tweepy.error.TweepError:
			continue
		print "Retweeted and Liked LoL Esports"
		break;
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