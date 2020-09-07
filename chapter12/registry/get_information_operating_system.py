#!/usr/bin/python3

import sys
from Registry import Registry
reg = Registry.Registry(sys.argv[1])

print("Analyzing SOFTWARE in Windows registry...")

try:
    key = reg.open("Microsoft\\Windows NT\\CurrentVersion")
    print("\tProduct name: " + key.value("ProductName").value())
    print("\tCurrentVersion: " + key.value("CurrentVersion").value())
    print("\tServicePack: " + key.value("CSDVersion").value())
    print("\tProductID: " + key.value("ProductId").value() + "\n")
except Registry.RegistryKeyNotFoundException as exception:
    print("Exception",exception)
