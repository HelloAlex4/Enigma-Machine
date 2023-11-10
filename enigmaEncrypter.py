import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def generateRotor():
	rotor = []

	for x in range(26 * 3 + 3):
		rotor.append(random.randint(0,25))

	return(rotor)

def rollover(inp):
	if(inp / 26 > 1):
		inp = inp - 26 * round(inp / 26 - 0.5)
	return (inp)

def encrypt(string):
	endstring = ""
	
	for x in range(len(string)):
		if(string[x] == " "):
			endstring += (" ")
		else:
			alphIndex = 0
			for y in range(int(len(rotor) / 26)):
				adder = rollover(x) * 3 + y

				alphIndex += (rotor[adder])
				alphIndex = rollover(alphIndex)

			alphIndex += alphabet.index(string[x])
			alphIndex = rollover(alphIndex)
			endstring += alphabet[alphIndex - 1]
	return endstring

	


rotor = (generateRotor())

string = input("enter text: ")
print(encrypt(sting))
print(rotor)
