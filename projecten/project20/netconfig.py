class config:
    # settings for wireless connection and socket connection
    ssid_to_cn = "DS9"
    # ssid_to_cn = "lokhetcvo"
    passwd = "********"
    # passwd = "Hetcvo.be"
    static_ip = ""
    connect_to = "192.168.1.54"
    # connect_to = "172.24.0.79"
    connect_to_port = 7600
    # port = 1022

    # vars for wlan, socket server and client
    wlan = None
    sSocket = None
    cSocket = None
    conn = None
    NUMBYTES = const(32)
