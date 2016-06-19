#this is program written here: https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print ("%s == %s" %(key,value))


#call the function 

greet_me(name="Diana")

# doesnt work. 




