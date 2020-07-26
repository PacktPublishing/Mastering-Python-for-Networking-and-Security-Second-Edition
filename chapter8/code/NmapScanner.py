#!/usr/bin/env python3

import optparse
import nmap

class NmapScanner:
     
    def __init__(self): 
        self.portScanner = nmap.PortScanner()
    
    def nmapScan(self, host, port): 
        self.portScanner.scan(host, port) 
        self.state = self.portScanner[host]['tcp'][int(port)]['state']
        print(" [+] Executing command: ", self.portScanner.command_line()) 
        print(" [+] "+ host + " tcp/" + port + " " + self.state)

def main():
    parser = optparse.OptionParser("usage%prog " + "--host <target host> --ports <target port>") 
    parser.add_option('--host', dest = 'host', type = 'string', help = 'Please, specify the target host.')
    parser.add_option('--ports', dest = 'ports', type = 'string', help = 'Please, specify the target port(s) separated by comma.')
    (options, args) = parser.parse_args()
    if (options.host == None) | (options.ports == None): 
        print('[-] You must specify a target host and a target port(s).')
        exit(0)
    host = options.host
    ports = options.ports.split(',')

    for port in ports: 
        NmapScanner().nmapScan(host, port)

if __name__ == "__main__": 
    main()
