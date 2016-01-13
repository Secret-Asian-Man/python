
# name=input("Input your name: ")

# def outputName(aName):
	# {
		# print ("Your name is ",name)
	# }
	
	
# outputName(name)




money=input("Give me your money, and I will double it: ") #money is a string atm
money=int(money) #converted the string into an integer

def addTen(number):
	number=number*2
	return number
	
number=addTen(money)

	
print ("Here is your $",number)

