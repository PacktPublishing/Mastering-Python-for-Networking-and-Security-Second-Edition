import sys
import os

if len(sys.argv) == 2:

	filename = sys.argv[1]
	print(filename)
	
	if os.path.isfile(filename):
		print('[+] ' + filename + ' does exist.')
		exit(0)
	if not os.path.isfile(filename):
		print('[+] ' + filename + ' does not exist.')
		exit(0)
	if not os.access(filename, os.R_OK):
		print('[+] ' + filename + ' access denied.')
		exit(0)


