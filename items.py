import requests
from reference import key

def getItemNames(itemBuild):
	print "Loading: 80%"
	itemNames = []
	for i in range(len(itemBuild)):
		item = itemBuild[i]
		requestItem = requests.get("https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/" + str(item) + "?api_key=" + key)
		if (requestItem.status_code == 200):
			itemNames.append(requestItem.json()["name"])
			if (itemNames[i] == "Abyssal Scepter"):
				itemNames[i] = "Abyssal"
			elif (itemNames[i] == "Aegis of the Legion"):
				itemNames[i] = "Aegis"
			elif (itemNames[i] == "Aether Wisp"):
				itemNames[i] = "Aether"
			elif (itemNames[i] == "Amplifying Tome"):
				itemNames[i] = "Tome"
			elif (itemNames[i] == "Archangel's Staff"):
				itemNames[i] = "Archangel's"
			elif (itemNames[i] == "Ardent Censer"):
				itemNames[i] = "Ardent"
			elif (itemNames[i] == "Athene's Unholy Grail"):
				itemNames[i] = "Athene's"
			elif (itemNames[i] == "B. F. Sword"):
				itemNames[i] = "BF"
			elif (itemNames[i] == "Banner of Command"):
				itemNames[i] = "Banner"
			elif (itemNames[i] == "Banshee's Veil"):
				itemNames[i] = "Banshee's"
			elif (itemNames[i] == "Berserker's Greaves"):
				itemNames[i] = "Greaves"
			elif (itemNames[i] == "Bilgewater Cutlass"):
				itemNames[i] = "Cutlass"
			elif (itemNames[i] == "Blade of the Ruined King"):
				itemNames[i] = "BORK"
			elif (itemNames[i] == "Blasting Wand"):
				itemNames[i] = "B Wand"
			elif (itemNames[i] == "Boots of Speed"):
				itemNames[i] = "Boots"
			elif (itemNames[i] == "Boots of Mobility"):
				itemNames[i] = "Mobis"
			elif (itemNames[i] == "Boots of Swiftness"):
				itemNames[i] = "Swiftys"
			elif (itemNames[i] == "Catalyst of Aeons"):
				itemNames[i] = "Catalyst"
			elif (itemNames[i] == "Caulfield's Warhammer"):
				itemNames[i] = "Warhammer"
			elif (itemNames[i] == "Chalice of Harmony"):
				itemNames[i] = "Chalice"
			elif (itemNames[i] == "Chain Vest"):
				itemNames[i] = "C Vest"
			elif (itemNames[i] == "Cloth Armor"):
				itemNames[i] = "Cloth"
			elif (itemNames[i] == "Control Ward"):
				itemNames[i] = "Ward"
			elif (itemNames[i] == "Corrupting Potion"):
				itemNames[i] = "Corrupt Pot"
			elif (itemNames[i] == "Crystalline Bracer"):
				itemNames[i] = "C Bracer"
			elif (itemNames[i] == "Dead Man's Plate"):
				itemNames[i] = "Dead Man's"
			elif (itemNames[i] == "Doran's Blade"):
				itemNames[i] = "D Blade"
			elif (itemNames[i] == "Doran's Ring"):
				itemNames[i] = "D Ring"
			elif (itemNames[i] == "Doran's Shield"):
				itemNames[i] = "D Shield"
			elif (itemNames[i] == "Duskblade of Draktharr"):
				itemNames[i] = "Duskblade"
			elif (itemNames[i] == "Edge of Night"):
				itemNames[i] = "EoN"
			elif (itemNames[i] == "Executioner's Calling"):
				itemNames[i] = "Executioner's"
			elif (itemNames[i] == "Enchantment: Bloodrazor"):
				itemNames[i] = "Bloodrazor"
			elif (itemNames[i] == "Enchantment: Cinderhulk"):
				itemNames[i] = "Cinderhulk"
			elif (itemNames[i] == "Enchantment: Runic Echoes"):
				itemNames[i] = "Runic"
			elif (itemNames[i] == "Enchantment: Warrior"):
				itemNames[i] = "Warrior"
			elif (itemNames[i] == "Essence Reaver"):
				itemNames[i] = "Essence"
			elif (itemNames[i] == "Eye of the Equinox"):
				itemNames[i] = "Equinox"
			elif (itemNames[i] == "Eye of the Oasis"):
				itemNames[i] = "Oasis"
			elif (itemNames[i] == "Eye of the Watchers"):
				itemNames[i] = "Watchers"
			elif (itemNames[i] == "Face of the Mountain"):
				itemNames[i] = "FotM"
			elif (itemNames[i] == "Fiendish Codex"):
				itemNames[i] = "Codex"
			elif (itemNames[i] == "Frost Queen's Claim"):
				itemNames[i] = "Frost Queen's"
			elif (itemNames[i] == "Frozen Mallet"):
				itemNames[i] = "Mallet"
			elif (itemNames[i] == "Giant's Belt"):
				itemNames[i] = "G Belt"
			elif (itemNames[i] == "Glacial Shroud"):
				itemNames[i] = "Shroud"
			elif (itemNames[i] == "Guardian Angel"):
				itemNames[i] = "GA"
			elif (itemNames[i] == "Guinsoo's Rageblade"):
				itemNames[i] = "Guinsoo's"
			elif (itemNames[i] == "Haunting Guise"):
				itemNames[i] = "Guise"
			elif (itemNames[i] == "Health Potion"):
				itemNames[i] = "Health Pot"
			elif (itemNames[i] == "Hextech GLP-800"):
				itemNames[i] = "GLP-800"
			elif (itemNames[i] == "Hextech Gunblade"):
				itemNames[i] = "Gunblade"
			elif (itemNames[i] == "Hextech Protobelt-01"):
				itemNames[i] = "Protobelt"
			elif (itemNames[i] == "Hunter's Potion"):
				itemNames[i] = "Hunter's Pot"
			elif (itemNames[i] == "Iceborn Gauntlet"):
				itemNames[i] = "Iceborn"
			elif (itemNames[i] == "Infinity Edge"):
				itemNames[i] = "IE"
			elif (itemNames[i] == "Ionian Boots of Lucidity"):
				itemNames[i] = "Ionians"
			elif (itemNames[i] == "Jaurim's Fist"):
				itemNames[i] = "Jaurim's"
			elif (itemNames[i] == "Kircheis Shard"):
				itemNames[i] = "Kircheis"
			elif (itemNames[i] == "Last Whisper"):
				itemNames[i] = "LW"
			elif (itemNames[i] == "Liandry's Torment"):
				itemNames[i] = "Liandry's"
			elif (itemNames[i] == "Locket of the Iron Solari"):
				itemNames[i] = "Locket"
			elif (itemNames[i] == "Long Sword"):
				itemNames[i] = "L Sword"
			elif (itemNames[i] == "Lord Dominik's Regards"):
				itemNames[i] = "LDR"
			elif (itemNames[i] == "Luden's Echo"):
				itemNames[i] = "Luden's"
			elif (itemNames[i] == "Maw of Malmortius"):
				itemNames[i] = "Maw"
			elif (itemNames[i] == "Mejai's Soulstealer"):
				itemNames[i] = "Mejai's"
			elif (itemNames[i] == "Mercurial Scimitar"):
				itemNames[i] = "Merc Scim"
			elif (itemNames[i] == "Mercury's Treads"):
				itemNames[i] = "Merc Treads"
			elif (itemNames[i] == "Mikael's Crucible"):
				itemNames[i] = "Mikael's"
			elif (itemNames[i] == "Morellonomicon"):
				itemNames[i] = "Morello"
			elif (itemNames[i] == "Mortal Reminder"):
				itemNames[i] = "M Reminder"
			elif (itemNames[i] == "Nashor's Tooth"):
				itemNames[i] = "Nashor's"
			elif (itemNames[i] == "Needlessly Large Rod"):
				itemNames[i] = "Large Rod"
			elif (itemNames[i] == "Negatron Cloak"):
				itemNames[i] = "Negatron"
			elif (itemNames[i] == "Ninja Tabi"):
				itemNames[i] = "Tabis"
			elif (itemNames[i] == "Null-Magic Mantle"):
				itemNames[i] = "N-M Mantle"
			elif (itemNames[i] == "Perfect Hex Core"):
				itemNames[i] = "Hex Core"
			elif (itemNames[i] == "Phantom Dancer"):
				itemNames[i] = "PD"
			elif (itemNames[i] == "Quicksilver Sash"):
				itemNames[i] = "QSS"
			elif (itemNames[i] == "Rabadon's Deathcap"):
				itemNames[i] = "Rabadon's"
			elif (itemNames[i] == "Randuin's Omen"):
				itemNames[i] = "Randuin's"
			elif (itemNames[i] == "Rapid Firecannon"):
				itemNames[i] = "RFC"
			elif (itemNames[i] == "Ravenous Hydra"):
				itemNames[i] = "Ravenous"
			elif (itemNames[i] == "Refillable Potion"):
				itemNames[i] = "Refill Pot"
			elif (itemNames[i] == "Relic Shield"):
				itemNames[i] = "Relic"
			elif (itemNames[i] == "Righteous Glory"):
				itemNames[i] = "R Glory"
			elif (itemNames[i] == "Rod of Ages"):
				itemNames[i] = "RoA"
			elif (itemNames[i] == "Ruby Crystal"):
				itemNames[i] = "R Crystal"
			elif (itemNames[i] == "Ruby Sightstone"):
				itemNames[i] = "Ruby S Stone"
			elif (itemNames[i] == "Runaan's Hurricane"):
				itemNames[i] = "Runaan's"
			elif (itemNames[i] == "Rylai's Crystal Scepter"):
				itemNames[i] = "Rylai's"
			elif (itemNames[i] == "Sapphire Crystal"):
				itemNames[i] = "S Crystal"
			elif (itemNames[i] == "Seeker's Armguard"):
				itemNames[i] = "Seeker's"
			elif (itemNames[i] == "Seraph's Embrace"):
				itemNames[i] = "Seraph's"
			elif (itemNames[i] == "Serrated Dirk"):
				itemNames[i] = "S Dirk"
			elif (itemNames[i] == "Sightstone"):
				itemNames[i] = "S Stone"
			elif (itemNames[i] == "Sorcerer's Shoes"):
				itemNames[i] = "Sorcs"
			elif (itemNames[i] == "Spectre's Cowl"):
				itemNames[i] = "Spectre's"
			elif (itemNames[i] == "Spellthief's Edge"):
				itemNames[i] = "Spellthief's"
			elif (itemNames[i] == "Spirit Visage"):
				itemNames[i] = "Visage"
			elif (itemNames[i] == "Statikk Shiv"):
				itemNames[i] = "Shiv"
			elif (itemNames[i] == "Sterak's Gage"):
				itemNames[i] = "Sterak's"
			elif (itemNames[i] == "Sunfire Cape"):
				itemNames[i] = "Sunfire"
			elif (itemNames[i] == "Talisman of Ascension"):
				itemNames[i] = "Talisman"
			elif (itemNames[i] == "Targon's Brace"):
				itemNames[i] = "Targon's"
			elif (itemNames[i] == "Tear of the Goddess"):
				itemNames[i] = "Tear"
			elif (itemNames[i] == "The Black Cleaver"):
				itemNames[i] = "Cleaver"
			elif (itemNames[i] == "The Bloodthirster"):
				itemNames[i] = "BT"
			elif (itemNames[i] == "The Dark Seal"):
				itemNames[i] = "Dark Seal"
			elif (itemNames[i] == "The Hex Core mk-1"):
				itemNames[i] = "Hex Core"
			elif (itemNames[i] == "The Hex Core mk-2"):
				itemNames[i] = "Hex Core"
			elif (itemNames[i] == "Titanic Hydra"):
				itemNames[i] = "Titanic"
			elif (itemNames[i] == "Total Biscuit of Rejuvenation"):
				itemNames[i] = "Biscuits"
			elif (itemNames[i] == "Trinity Force"):
				itemNames[i] = "Tri Force"
			elif (itemNames[i] == "Vampiric Scepter"):
				itemNames[i] = "Vamp Scepter"
			elif (itemNames[i] == "Void Staff"):
				itemNames[i] = "Void"
			elif (itemNames[i] == "Warden's Mail"):
				itemNames[i] = "Warden's"
			elif (itemNames[i] == "Warmog's Armor"):
				itemNames[i] = "Warmog's"
			elif (itemNames[i] == "Youmuu's Ghostblade"):
				itemNames[i] = "Youmuu's"
			elif (itemNames[i] == "Zeke's Harbinger"):
				itemNames[i] = "Zeke's"
			elif (itemNames[i] == "Zhonya's Hourglass"):
				itemNames[i] = "Zhonya's"
			elif (itemNames[i] == "Zz'Rot Portal"):
				itemNames[i] = "Zz'Rot"
		else:
			print "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item/" + str(item) + "?api_key=" + key
			raise KeyError("Could not connect when getting the item ID: " + str(item))
	return itemNames
