alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rotors = input("input the Rotors you got from the encrypter: ")
string = input("enter the output from the encrypter: ")

def rollover(inp):
	inp -= inp * 2

	if(inp / 26 > 1):
		inp = inp - 26 * round(inp / 26 - 0.5)
	return (inp - inp * 2)

def decrypter(string, rotor):
	endstring = ""
	
	for x in range(len(string)):
		if(string[x] == " "):
			endstring += (" ")
		else:
			alphIndex = 0
			for y in range(int(len(rotor) / 26)):
				subtractorIndex = rollover(x) * 3 + y

				alphIndex -= (rotor[subtractorIndex])
				alphIndex = rollover(alphIndex)

			print(alphIndex)
			endstring += alphabet[alphabet.index(string[x]) + alphIndex + 1]
	return endstring

print(decrypter(string, rotors))