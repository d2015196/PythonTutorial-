#use of keyword arguments

def AboutMe(name1, verb1, verb2, noun1, adjective1, noun2, verb3, adjective2): 
	print("Hello my name is " + name1 + " and I like to go " + verb1 + " and " + verb2 + " with " + noun1 + ". ")
	print("I also am very " + adjective1 + " when " + noun2 + " is " + verb3 + " me because " + " the whole ")
	print(" scenario is very " + adjective2)

#Okay here we go I am going to call my function

#load my keyworded arguments 

kwargs = {"name1": "Diana" , "adjective1": "confused", "adjective2": "savage" , "noun1": "a snowman" , "noun2": "a Kevin Wayne" , 
"verb1": "hiking" , "verb2": "snowing" , "verb3": "playing basketball" } 

#call my function using kwargs 

AboutMe(**kwargs)

#so you can see how the key word argument can allow you to reorganize the input stream provided by the user. 
#if you have all of your input arguments labelled then the order in which the user gives them does not matter too much. 
#you can literally just call upon them in your function. 

