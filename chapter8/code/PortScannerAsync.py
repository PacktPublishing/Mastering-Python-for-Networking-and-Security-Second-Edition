import nmap

portScannerAsync = nmap.PortScannerAsync()

def callback_result(host, scan_result):
    print(host, scan_result)

portScannerAsync.scan(hosts='scanme.nmap.org', arguments='-sP', callback=callback_result)
while portScannerAsync.still_scanning():
    print("Scanning >>>")
    portScannerAsync.wait(5)
