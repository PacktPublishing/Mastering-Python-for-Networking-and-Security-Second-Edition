import pysftp
import getpass

HOSTNAME = 'localhost'
PORT = 22

def sftp_getfiles(username, password, hostname=HOSTNAME,port=PORT):
    with pysftp.Connection(host=hostname, username=username, password=password) as sftp:
        print("Connection successfully established with server... ")
        sftp.cwd('/')
        list_directory = sftp.listdir_attr()
        for directory in list_directory:
            print(directory.filename, directory)

if __name__ == '__main__':
	hostname = input("Enter the target hostname: ")
	port = input("Enter the target port: ")
	username = input("Enter your username: ")
	password = getpass.getpass(prompt="Enter your password: ")
	sftp_getfiles(username, password, hostname, port)
