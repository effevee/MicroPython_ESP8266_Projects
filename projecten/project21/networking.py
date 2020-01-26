import netconfig as net
import network
import socket

class wifi:
    @staticmethod
    def connectWIFI():
        net.config.wlan = network.WLAN(network.STA_IF)
        net.config.wlan.active(True)
        if not net.config.wlan.isconnected():
            print('connecting to network...')
            net.config.wlan.connect(net.config.ssid_to_cn, net.config.passwd)
            while not net.config.wlan.isconnected():
                pass
        #if in net.config static_ip is defined change ip adress obtained by DHCP with the static adress
        if net.config.static_ip != "":
            ifData=list(net.config.wlan.ifconfig())
            ifData[0]=net.config.static_ip
            net.config.wlan.ifconfig(tuple(ifData))
        print('network config:', net.config.wlan.ifconfig())
        return net.config.wlan
    
    @staticmethod
    def disconnectWIFI():
        if net.config.wlan == None:
            return 0
        if not net.config.wlan.isconnected():
            return 0
        net.config.wlan.disconnect()
        return 1

class socketServer:
    
    @staticmethod
    def start():
        try:
            host = net.config.wlan.ifconfig()[0]
            net.config.sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            net.config.sSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            addr = socket.getaddrinfo(host,net.config.port)
            print(addr)
            net.config.sSocket.bind(addr[0][-1])
            net.config.sSocket.listen(1)
            return True
        except Exception as e:
            net.config.sSocket.close()
            print(e)
            return False

    @staticmethod
    def waitCn():
        try:
            net.config.conn,addr=net.config.sSocket.accept()
            qs = net.config.conn.recv(net.config.NUMBYTES).decode("ascii")
            if qs == 'GO' or qs == 'go':
                return 1
            elif qs == 'HALT' or qs == 'halt':
                net.config.conn.close()
                net.config.sSocket.close()
                return 0
            else:
                net.config.conn.close()
                net.config.conn=None
                return -1
        except Exception as e:
            print(e)
            net.config.conn.close()
            return -1
    
    @staticmethod
    def sendData(data):
        net.config.conn.send(data)
    
    @staticmethod
    def readData():
        res=net.config.conn.recv(net.config.NUMBYTES)
        return res.decode("ascii")
    @staticmethod
    def stopClient():
        try:
            net.config.conn.close()
            return True
        except:
            return True
    
    @staticmethod
    def stop():
        try:
            net.config.sSocket.close()
            return True
        except:
            return True

class socketHTTPRequest:
    
    @staticmethod
    def sendGETRequest(req):
        try:
            addr = socket.getaddrinfo(net.config.connect_to,net.config.connect_to_port)[0][-1]
            cSocket=socket.socket()
            cSocket.connect(addr)
            strToSend='GET ' + req + ' HTTP/1.1\r\n\r\n'
            cSocket.send(strToSend.encode("ascii"))
            res=cSocket.recv(1024)
            res=res.decode("ascii")
            if res.find("OK")<0 or res.find("200")<0:
                cSocket.close()
                return 0
            cSocket.close()
            return 1
        except Exception as e:
            print(e)
            return -1
            
