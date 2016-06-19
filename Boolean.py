favoritefood = "Hotdogs"
favoritelanguage = "Python (Yuzzz!)"
favoritecountry = "Deutschland"
stuff = [] 
stuff.append(favoritecountry)
stuff.append(favoritelanguage)


if favoritecountry == "Deutschland" or favoritecountry == "Mexico": 
	print ("You are correct ")

if favoritelanguage in stuff: 
	print("Cool bro")

if favoritecountry == "Deutschland": 
	print("Cool story, die Deutsche sind immer toll ")

elif favoritefood == "Hotdogs": 
	print("Sie sind nicht so gut fur sie, aber ja hotdogs sind lecker")

else: 
	print("Du bist nicht interessant, tut mir leid")


print(not False == False)



