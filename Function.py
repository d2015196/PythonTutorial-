x = 5
name = "Jeremy"

def Future(name, futuretime, currentage): 
	newage = currentage + futuretime
	print("In " + str(futuretime) + " years, " + name 
		+ " will be " + str(newage) + " years old")


print(name +" is " + str(x) + " years old")

Future(name, 9, x)