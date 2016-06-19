#this program contains the names of the accapted people. 

#so we have the invited list... 

invited = []
invited.append("Kendall Jenner")
invited.append("Mariana Vazquez Romo")
invited.append("Khloe Kardashian")
invited.append("Kourtney Kardashian")
invited.append("Miley Cyrus")
invited.append("Rob Kardashian")

accepted = []

#and then.. this is what we call List Comprehensions, make a list using another one as a base. 

accepted = [i for i in invited if "Kardashian" not in i]

for i in accepted: 
	print (i) 

