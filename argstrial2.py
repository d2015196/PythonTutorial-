def IntroductionPrompt(arg1, arg2, arg3, arg4, arg5):
	print("My name is " + arg1+ " and I really like to cook " + str(arg2) + " " + arg3 )
	print("My mom's name is " + arg4 + " and you should contact her if you need " + arg5)



	#call function 

IntroductionPrompt('Diana', 7, 'Asparagus', 'Alicia', 'Lolipops')

#now I will do the same thing with variable length argument 

args = ("Diana", 7, "Asparagus", "Alicia", "Lolipops")

IntroductionPrompt(*args)



