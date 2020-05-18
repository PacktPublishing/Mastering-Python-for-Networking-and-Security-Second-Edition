import os
pwd = os.getcwd()
list_directory = os.listdir(pwd)
for directory in list_directory:
	print('[+] ',directory)
