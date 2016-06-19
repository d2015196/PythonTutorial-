import pickle 

book = {}
book["favorite"] = "Jungle Book"
book["worst"] = "Hello by Rebecca "
book["proper"] = "SmashMoth "

#supposedly stores the data in bytes 

m = pickle.dumps(book)
book3 = pickle.loads(m)

print(book3 == book)