import os
for root, directories, files in os.walk(".",topdown=False):
    # Iterate over the files in the current "root"
	for file_entry in files:
        # create the relative path to the file
		print('[+] ',os.path.join(root,file_entry))
	
	for name in directories:
		print('[++] ',name)

