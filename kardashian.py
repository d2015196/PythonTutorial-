invited = []
invited.append("Kendall Jenner")
invited.append("Mariana Vazquez Romo")
invited.append("Khloe Kardashian")
invited.append("Kourtney Kardashian")

accepted = []

#iterate over items in invited. 

#remember that the in command automatically activates an iterator. 
for i in invited:

#give control back to the iterator if the invited person has name Kardashian. 

	if "Kardashian" in i: 
		continue 

	else: 

		accepted.append(i)

for i in accepted: 
	print (i)

