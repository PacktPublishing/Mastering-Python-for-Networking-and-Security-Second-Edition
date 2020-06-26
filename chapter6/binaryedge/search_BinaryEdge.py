from pybinaryedge import BinaryEdge

key='e4dd5074-7aec-45b9-9b81-3bd4d1f382ac'

binaryEdge = BinaryEdge(key)

search_domain = 'www.python.org'

results = binaryEdge.host_search(search_domain)

for ip in results['events']:
    print("%s" %(ip['target']['ip']))
