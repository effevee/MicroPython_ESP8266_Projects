import threading
import json

class work:

	data={"button_2":"","output_3":"","output_0":""}
	lock = threading.Lock()
	#schrijf hier eigen klas variabelen, zoals
	#Lists voor selects en radiogroups
	teller = 0

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
	def do_btn_teller(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
			cls.teller += 1
			boodschap = "Er is reeds " + str(cls.teller) + " maal contact gemaakt."
			cls.set_txt_teller(boodschap)

		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_btn_teller(cls):
		return cls.data["button_2"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_btn_teller(cls,val):
		cls.data["button_2"]=val

	@classmethod
	def do_txt_teller(cls):
		try:
			cls.lock.acquire()
			#schrijf hier code, bijv. getters en/of setters
		finally:
			cls.lock.release()

		return json.dumps(cls.data,ensure_ascii=False)

	@classmethod
	def get_txt_teller(cls):
		return cls.data["output_3"]

	@classmethod
	#maak dat een setter altijd tussen cls.lock.acquire()
	#en cls.lock.release() staat!!!!
	def set_txt_teller(cls,val):
		cls.data["output_3"]=val

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

