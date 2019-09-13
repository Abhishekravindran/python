def listfun():
	carlist = ["audi","benz","jaguar","rangerover"]
	print('i want',len(carlist), 'to buy these cars')
	
	print("i also have to buy a bike")
	carlist.append("ducati")
	print('my wish list of vehicles are',carlist)
	print("lets sort the lisr according to alphabetical order")
	carlist.sort()
	print("sorted car list is",carlist)

	print("the first car i will buy is", carlist[0])
	oldcar=carlist[0]
	del carlist[0]
	print("wish fullfilled",oldcar)
	print("the left over cars and bike to buy are",carlist)
listfun()
