class protocol(object):

	def __init__(self, name, number,description):
		self.name = name
		self.number = number
		self.description = description

	def getProtocolInfo(self):
		return self.name+ " "+str(self.number)+ " "+self.description
		
protocol_http= protocol("HTTP", 80, "Hypertext transfer protocol")

print(protocol_http.name)
print(protocol_http.number)
print(protocol_http.description)
print(protocol_http.getProtocolInfo())
