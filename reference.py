import tweepy
from credentials import *

myFile = file("C:\School\University\League Bot\config.txt", "r")
configFile = myFile.readlines()
key = configFile[0].split("=")[1].rstrip("\n")
filepath = configFile[1].split("=")[1].rstrip("\n")