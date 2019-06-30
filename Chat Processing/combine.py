filenames = ["WhatsApp Chat with Person B"]
cwcounter = 0
othercounter = 0
stringstore = ""

f = open("myside.txt", 'w')
fother = open("otherside.txt", 'w')
#column 0 and column 1, 0 Chunside 1 Ohter Side, row 0++
for names in filenames:
	cwfile = open(names + "CWOK.txt")
	otherfile = open(names + "OK.txt")

	print(names + ".txt QnA pair has been opened")
	for line in cwfile:
		if(line.startswith("|")):
			#s1.write(cwcounter, 0, stringstore)
			f.write(stringstore)
			cwcounter += 1
			stringstore = "\n"
		else:
			stringstore += " " + line.rstrip()
			#print(stringstore)
			
	for oline in otherfile:
		if(oline.startswith("|")):
			#s1.write(othercounter, 1, stringstore)
			fother.write(stringstore)
			othercounter += 1
			stringstore = "\n"
		else:
			stringstore += " " + oline.rstrip()
			#print(stringstore)
print("Me:" + str(cwcounter) + " Other" + str(othercounter))
