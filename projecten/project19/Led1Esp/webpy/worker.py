import threading
import json
from networkingPI import PiSocketClient

class work:

	data={"button_3":"","toggle_2":"0","output_0":""}
	lock = threading.Lock()
	#schrijf hier eigen klas variabelen, zoals
	#Lists voor selects en radiogroups
	IPSERVER = "192.168.1.30"
	PORT = 1022


	@classmethod
	def start(cls):
		#schrijf hieronder je initialisatie code:
		#init gpio pinnen (RPi.GPIO), init sercomm ...
		print("start worker")

	@classmethod
	def stop(cls):
		#schrijf hieronder je opkuis code:
		#opkuisen gpio pinnen (RPi.GPIO), sluiten sercomm ...
		print("stop worker")

	@classmethod
	def do_btnStopESP(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
			PiSocketClient.start(cls.IPSERVER, cls.PORT)
			PiSocketClient.sendData("halt")
			PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btnStopESP(cls):
		return cls.data["button_3"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btnStopESP(cls,val):
		cls.data["button_3"]=val

	@classmethod
	def do_tgLedESP(cls,val):
		try:
			cls.lock.acquire()
			cls.set_tgLedESP(val)
			#schrijf hier code, bijv. aan de hand van val een LED doen branden
			if PiSocketClient.start(cls.IPSERVER, cls.PORT):
				PiSocketClient.sendData("go")
				res = PiSocketClient.readData()
				PiSocketClient.sendData(val)
				res = PiSocketClient.readData()
				PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_tgLedESP(cls):
		return cls.data["toggle_2"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_tgLedESP(cls,val):
		cls.data["toggle_2"]=val

	@classmethod
	def do_output_0(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_output_0(cls):
		return cls.data["output_0"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_output_0(cls,val):
		cls.data["output_0"]=val

