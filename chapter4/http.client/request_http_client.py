import http.client

connection = http.client.HTTPConnection("www.google.com")
connection.request("GET", "/")
response = connection.getresponse()
print(type(response))
print(response.status, response.reason)
data = response.read()
print(data)
