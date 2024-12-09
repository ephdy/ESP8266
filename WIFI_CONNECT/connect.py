import network
from socket import *

def station_init(ssid="C7",key="98765432"):
    wlan = network.WLAN(network.WLAN.IF_STA) # create station interface
    wlan.active(True)       # activate the interface
    #wlan.scan()             # scan for access points
    #wlan.isconnected()      # check if the station is connected to an AP
    #wlan.connect(ssid,key) # connect to an AP
    #wlan.config('mac')      # get the interface's MAC address
    #wlan.ipconfig('addr4')  # get the interface's IPv4 addresses
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, key)
        while not wlan.isconnected():
            pass
    

def ap_init():
    ap = network.WLAN(network.WLAN.IF_AP) # create access-point interface
    ap.active(True)         # activate the interface
    ap.config(ssid='ESP-AP') # set the SSID of the access point
    
    
def udp_init():
    udp=socket(AF_INET, SOCK_DGRAM)
    udp.sendto("AMD".encode('uft-8'),('192.168.1.110',8080))
    recv_data=udp.recvfrom(1024)
    print(recv_data[0].decode('gbk'))
    print(recv_data[1])
    udp.close()