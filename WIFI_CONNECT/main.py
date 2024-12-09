import WIFI

def main():
    WIFI.station_init()
    WIFI.udp_init()
    
if __name__ == '__main__':
    main()