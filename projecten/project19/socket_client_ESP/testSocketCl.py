from networkingPI import PiSocketClient
import time

IPSERVER = "192.168.1.30"
PORT = 1022

LEDseq = [1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,1,1,1,1,0]

for s in LEDseq:
	if PiSocketClient.start(IPSERVER, PORT):
		PiSocketClient.sendData("go")
		res = PiSocketClient.readData()
		print(res)
		PiSocketClient.sendData(str(s))
		res = PiSocketClient.readData()
		print(res)
	PiSocketClient.stop()
	time.sleep(2)

PiSocketClient.start(IPSERVER, PORT)
PiSocketClient.sendData("halt")
PiSocketClient.stop()
