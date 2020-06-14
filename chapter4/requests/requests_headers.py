#!/usr/bin/python

import requests, json


domain = input("Enter the domain http://")

response = requests.get("http://"+domain)

print(response.json)

print("Status code: "+str(response.status_code))

print("Headers response: ")
for header, value in response.headers.items():
  print(header, '-->', value)
  
print("Headers request : ")
for header, value in response.request.headers.items():
  print(header, '-->', value)
