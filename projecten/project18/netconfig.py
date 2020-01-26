class config:
    #settings for wireless connection and socket connection
    ssid_to_cn="KruisA"
    passwd="Hetcvo.be"
    static_ip=""
    connect_to="192.168.0.108"
    connect_to_port=8100
    port=1022
    
    #vars for wlan, socket server and client
    wlan = None
    sSocket = None
    cSocket = None
    conn=None
    NUMBYTES=const(32)
    
    