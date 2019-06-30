import re
filenames = ["WhatsApp Chat with Person B"]

for names in filenames:
	file_handle = open(names + "sep.txt")
	print(names + ".txt has been opened")
	f = open(names + "OK.txt", 'w')
	for line in file_handle:
		if(line.startswith("|")):
			f.write(line)
		else:
			temp = re.sub(r'.*:', ':', line)
			line = temp[2:]
			f.write(line)

file_handle.close()