import re
filenames = ["WhatsApp Chat with Person B"]
 
for names in filenames:
	file_handle = open(names + ".txt")
	print(names + ".txt has been opened")
	f = open(names + "out.txt", 'w')
	for line in file_handle:
		temp = re.sub(r'.*-', '-', line)
		line = temp[2:]
		f.write(line)
		#print(line)
file_handle.close()