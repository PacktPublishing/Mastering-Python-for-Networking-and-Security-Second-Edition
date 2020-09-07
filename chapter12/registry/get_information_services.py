#!/usr/bin/python3

from Registry import Registry
import sys

def getCurrentControlSet(registry):
    try:
        key = registry.open("Select")
        for value in key.values():
            if value.name() == "Current":
                return value.value()
    except Registry.RegistryKeyNotFoundException as exception:
        print("Couldn't find SYSTEM\Select key ",exception)

def getServiceInfo(dictionary):
    serviceType = { 1 : "Kernel device driver", 2 : "File system driver", 4 : "Arguments for an adapter",
    8 : "File system driver interpreter", 16 : "Own process", 32 : "Share process",272 : "Independent interactive program",
    288 : "Shared interactive program" }
    print(" Service name: %s" % dictionary["SERVICE_NAME"])
    if "DisplayName" in dictionary:
        print (" Display name: %s" % "".join(dictionary["DisplayName"]).encode('utf8'))

    if "ImagePath" in dictionary:
        print(" ImagePath: %s" % dictionary["ImagePath"])

    if "Type" in dictionary:
        print(" Type: %s" % serviceType[dictionary["Type"]])

    if "Group" in dictionary:
        print(" Group: %s" % dictionary["Group"])

    print("--------------------------")


def serviceParams(subkey):
    service = {}
    service["SERVICE_NAME"] = subkey.name()
    service["ModifiedTime"] = subkey.timestamp()

    for value in subkey.values():
        service[value.name()] = value.value()

    getServiceInfo(service)

def servicesKey(registry, controlset):
    serviceskey = "ControlSet00%d\\Services" % controlset
    try:
        key = registry.open(serviceskey)
    except Registry.RegistryKeyNotFoundException as exception:
        print("Couldn't find Services key ",exception)

    for subkey in key.subkeys():
        serviceParams(subkey)


if __name__ == "__main__" :
    registry = Registry.Registry(sys.argv[1])
    controlset = getCurrentControlSet(registry)
    servicesKey(registry, controlset)
