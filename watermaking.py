import string

string.printable = string.printable.replace("\r", "éèùàïîê")

def cesar_cypher(message, key):
	if type(message) != str:
		raise Exception("Message must be a str")
	if type(key) != int:
		raise Exception("Key must be a int")

	crypted_message = []
	for carac in message :
		crypted_index = (string.printable.index(carac) + key) % len(string.printable)
		crypted_message.append(string.printable[crypted_index])

	return "".join(crypted_message)


print(cesar_cypher("hakim a mangé un muffin", 3))
print(cesar_cypher("kdnlpédépdqjàéxqépxiilq", -3))



