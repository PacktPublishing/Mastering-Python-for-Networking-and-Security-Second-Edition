import socket
import argparse
import re

parser = argparse.ArgumentParser(description='Get banner server')

# Main arguments
parser.add_argument("--target", dest="target", help="target IP", required=True)
parser.add_argument("--port", dest="port", help="port", type=int, required=True)
parsed_args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((parsed_args.target, parsed_args.port))
sock.settimeout(2)

query = "GET / HTTP/1.1\nHost: "+parsed_args.target+"\n\n"
http_get = bytes(query,'utf-8')

data = ''

with open('vulnbanners.txt', 'r') as file:
    vulnbanners = file.readlines()

try:
    sock.sendall(http_get)
    data = sock.recvfrom(1024)
    data = data[0]
    print(data)

    headers = data.splitlines()

    for header in headers:
        try:
            if re.search('Server:', str(header)):
                print("*****"+header.decode("utf-8")+"*****")
            else:
                print(header.decode("utf-8"))
        except Exception as exception:
            pass
    
    for vulnbanner in vulnbanners:
        if vulnbanner.strip() in str(data.strip().decode("utf-8")):
            print('Found server vulnerable! ', vulnbanner)
            print('Target: '+str(parsed_args.target))
            print('Port: '+str(parsed_args.port))

except socket.error:
	print ("Socket error", socket.errno)
finally:
	sock.close()
		
