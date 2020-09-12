
#!/usr/bin/python

# Python code to search files in current folder
import os 

# This is to get the directory that the program 
# is currently running in. 
term_to_search = "Branch"
letter = str(term_to_search[0].lower)
dir_path = os.path.dirname(os.path.realpath(__file__)) 

for root, dirs, files in os.walk(dir_path): 
	for file in files: 

		# the one of your choice. 
		if file.startswith(letter): 
			print (letter) 
