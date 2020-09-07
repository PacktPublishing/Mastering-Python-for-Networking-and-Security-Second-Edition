#!/usr/bin/python3

import sys
from Registry import Registry
reg = Registry.Registry(sys.argv[1])

print("Analyzing SOFTWARE in Windows registry...")

try:
    key = reg.open("Microsoft\\Windows\\CurrentVersion\\Run")
    print("Last modified: %s [UTC]" % key.timestamp())
    for value in key.values():
            print("Name: " + value.name() + ", Value path: " + value.value())
except Registry.RegistryKeyNotFoundException as exception:
    print("Exception",exception)
