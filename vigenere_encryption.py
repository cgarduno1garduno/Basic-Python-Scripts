# encVigenere - Vigenere encryption function
def encVigenere(key, plaintext):
	from math import ceil 					  			# import ceiling function
	repeat   = ceil(len(plaintext)/len(key))  			# compute ratio for size of plaintext to size of key
	tempKey  = (repeat*key)[:len(plaintext)]  			# create key of the same size as input text
	convKey  = textConvert(tempKey)           			# convert key to integer/index values
	convText = textConvert(plaintext)		  			# convert plaintext to integer/index values	
	tempText = [i+j for i,j in zip(convKey,convText)]   # add key and text elements
	ciphertext = textConvert([t%41 for t in tempText])  # compute mods and convert to characters
	return ciphertext

# decVignere - Vigenere decryption function
def decVigenere(key, ciphertext):
	from math import ceil 					  			# import ceiling function
	repeat   = ceil(len(ciphertext)/len(key))  			# compute ratio for size of plaintext to size of key
	tempKey  = (repeat*key)[:len(ciphertext)]  			# create key of the same size as input text
	convKey  = textConvert(tempKey)           			# convert key to integer/index values
	convCiph = textConvert(ciphertext)		  			# convert ciphertext to integer/index values	
	tempCiph = [i-j for i,j in zip(convCiph,convKey)] 	# subtract key from cipher
	plaintext = textConvert([t%41 for t in tempCiph])   # compute mods and convert to characters
	return plaintext



# textConvert - converts input bidirectionally (string <--> indeces)
def textConvert(message):
	alphabet = "abcdefghijklmnopqrstuvwxyz0123456789 .,?!" 
	if isinstance(message, str): # executes when converting message to indices
		returnMessage = []
		for i in message: returnMessage.append(alphabet.index(i))
		return returnMessage
	else: 						 # executes when converting indices to message
		returnMessage = ""
		for i in message: returnMessage += alphabet[i] 
		return returnMessage