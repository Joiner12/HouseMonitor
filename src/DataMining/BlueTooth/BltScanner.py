#-*- coding:utf-8 -*-
import bluetooth
from bluetooth.ble import DiscoveryService


def OrdBluetooth():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))


# bluetooth low energy scan
def LeBluetooth():
    service = DiscoveryService()
    devices = service.discover(2)

    for address, name in devices.items():
        print("name: {}, address: {}".format(name, address))


if name == "__main__":
    OrdBluetooth()