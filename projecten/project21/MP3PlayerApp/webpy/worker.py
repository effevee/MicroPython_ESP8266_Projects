import threading
import json
from networkingPI import PiSocketClient

class work:

	data={"button_9":"","button_8":"","slider_11":"0","button_3":"","button_2":"","button_4":"","button_7":"","button_6":"","select_5":"","button_10":"","button_12":"","output_0":""}
	lock = threading.Lock()
	#schrijf hier eigen klas variabelen, zoals
	#Lists voor selects en radiogroups
	SERVER = "192.168.1.30"
	PORT = 1022
	PLAYLIST = []
	TRACK = 1

	@classmethod
	def start(cls):
		#schrijf hieronder je initialisatie code:
		#init gpio pinnen (RPi.GPIO), init sercomm ...
		print("start worker")
		# opvullen playlist ahv tekstfile
		with open("playlist.txt") as file:
    			for line in file:
        			line = line.strip()
        			cls.PLAYLIST.append(line)
		# opvullen select met songs van PLAYLIST
		cls.data["select_5"] = {"fill@select":cls.PLAYLIST,"value":cls.PLAYLIST[0]}
		# volume op helft
		cls.do_sld_volume("50")

	@classmethod
	def stop(cls):
		#schrijf hieronder je opkuis code:
		#opkuisen gpio pinnen (RPi.GPIO), sluiten sercomm ...
		print("stop worker")

	@classmethod
	def do_btn_voldown(cls):
		# volume verlagen
		volume = int(cls.get_sld_volume())
		volume -= 1
		if volume < 0:
			volume = 0
		cls.do_sld_volume(str(volume))

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btn_voldown(cls):
		return cls.data["button_10"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btn_voldown(cls,val):
		cls.data["button_10"]=val

	@classmethod
	def do_btn_volup(cls):
		# volume verhogen
		volume = int(cls.get_sld_volume())
		volume += 1
		if volume > 100:
			volume = 100
		cls.do_sld_volume(str(volume))

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btn_volup(cls):
		return cls.data["button_12"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btn_volup(cls,val):
		cls.data["button_12"]=val

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

	@classmethod
	def do_btn_pauze(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
			if PiSocketClient.start(cls.SERVER, cls.PORT):
				PiSocketClient.sendData("go")
				res = PiSocketClient.readData()
				PiSocketClient.sendData("pause")
				res = PiSocketClient.readData()
				PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btn_pauze(cls):
		return cls.data["button_3"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btn_pauze(cls,val):
		cls.data["button_3"]=val

	@classmethod
	def do_btn_play(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
			if PiSocketClient.start(cls.SERVER, cls.PORT):
				PiSocketClient.sendData("go")
				res = PiSocketClient.readData()
				PiSocketClient.sendData("play")
				res = PiSocketClient.readData()
				PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btn_play(cls):
		return cls.data["button_2"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btn_play(cls,val):
		cls.data["button_2"]=val

	@classmethod
	def do_btn_stop(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
			if PiSocketClient.start(cls.SERVER, cls.PORT):
				PiSocketClient.sendData("go")
				res = PiSocketClient.readData()
				PiSocketClient.sendData("stop")
				res = PiSocketClient.readData()
				PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btn_stop(cls):
		return cls.data["button_4"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btn_stop(cls,val):
		cls.data["button_4"]=val

	@classmethod
	def do_btn_next(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
			if PiSocketClient.start(cls.SERVER, cls.PORT):
				PiSocketClient.sendData("go")
				res = PiSocketClient.readData()
				# volgende track
				cls.TRACK += 1
				if cls.TRACK > len(cls.PLAYLIST):
					cls.TRACK = 1
				cls.set_sel_track(cls.PLAYLIST[cls.TRACK-1])
				PiSocketClient.sendData("play:"+str(cls.TRACK))
				# PiSocketClient.sendData("next")
				res = PiSocketClient.readData()
				PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btn_next(cls):
		return cls.data["button_8"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btn_next(cls,val):
		cls.data["button_8"]=val

	@classmethod
	def do_btn_prev(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
			if PiSocketClient.start(cls.SERVER, cls.PORT):
				PiSocketClient.sendData("go")
				res = PiSocketClient.readData()
				# vorige track
				cls.TRACK -= 1
				if cls.TRACK <= 0:
					cls.TRACK = len(cls.PLAYLIST)
				cls.set_sel_track(cls.PLAYLIST[cls.TRACK-1])
				PiSocketClient.sendData("play:"+str(cls.TRACK))
				# PiSocketClient.sendData("prev")
				res = PiSocketClient.readData()
				PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btn_prev(cls):
		return cls.data["button_7"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btn_prev(cls,val):
		cls.data["button_7"]=val

	@classmethod
	def do_btn_first(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
			if PiSocketClient.start(cls.SERVER, cls.PORT):
				PiSocketClient.sendData("go")
				res = PiSocketClient.readData()
				# eerste track
				cls.TRACK = 1
				cls.set_sel_track(cls.PLAYLIST[cls.TRACK-1])
				PiSocketClient.sendData("play:"+str(cls.TRACK))
				# PiSocketClient.sendData("play:1")
				res = PiSocketClient.readData()
				PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btn_first(cls):
		return cls.data["button_6"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btn_first(cls,val):
		cls.data["button_6"]=val

	@classmethod
	def do_btn_last(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
			if PiSocketClient.start(cls.SERVER, cls.PORT):
				PiSocketClient.sendData("go")
				res = PiSocketClient.readData()
				# laatste track
				cls.TRACK = len(cls.PLAYLIST)
				cls.set_sel_track(cls.PLAYLIST[cls.TRACK-1])
				PiSocketClient.sendData("play:"+str(cls.TRACK))
				res = PiSocketClient.readData()
				PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btn_last(cls):
		return cls.data["button_9"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btn_last(cls,val):
		cls.data["button_9"]=val

	@classmethod
	def do_sld_volume(cls,val):
		try:
			cls.lock.acquire()
			cls.set_sld_volume(val)
			#schrijf hier code, bijv. aan de hand van val een LED doen branden
			if PiSocketClient.start(cls.SERVER, cls.PORT):
				PiSocketClient.sendData("go")
				res = PiSocketClient.readData()
				PiSocketClient.sendData("vol:"+val)
				res = PiSocketClient.readData()
				PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_sld_volume(cls):
		return cls.data["slider_11"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_sld_volume(cls,val):
		cls.data["slider_11"]=val

	@classmethod
	def do_sel_track(cls,val):
		try:
			cls.lock.acquire()
			cls.set_sel_track(val)
			#schrijf hier code, bijv. aan de hand van val een LED doen branden
			if PiSocketClient.start(cls.SERVER, cls.PORT):
				PiSocketClient.sendData("go")
				res = PiSocketClient.readData()
                                print(val)
				track = val.split(":")
				cls.TRACK = int(track[0])
				PiSocketClient.sendData("play:"+str(cls.TRACK))
				res = PiSocketClient.readData()
				PiSocketClient.stop()
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_sel_track(cls):
		return cls.data["select_5"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_sel_track(cls,val):
	    cls.data["select_5"] = {"fill@select":cls.PLAYLIST,"value":val}

