import os
import shutil

d = []
for x in os.listdir("./"):
	if x[:2] == "s00":
		d.append(x)
print(d)                                                  # stored all relevant directory names in one list. 

for x in d:
	for dirpath, dirnames, files in os.walk(x):
		print(f'Found directory: {dirpath}') 
		try:                                                  # Try/Except block because I didnt want to see random errors while testing... im too lazy to remove it.
			for file_name in files:
				if file_name[16] == "0":                          # If 16th character of filename is 0, then
					#print("To Close")
					shutil.move(dirpath+"/"+file_name, "close/")    # it will be moved from dirpath/filename to closed/
				elif file_name[16] == "1":                        # If 16th character of filename is 0, then
					#print("To Open")
					shutil.move(dirpath+"/"+file_name, "open/")     # It will be moved from dirpath/filename to closed/
				else:
					continue
		except:
			continue
