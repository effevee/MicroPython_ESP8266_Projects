import time

# klasse voor stepper motor met 4 fazen + common (halve stap sequentie)
# stepper 28BYJ-48 met ULN2003A driver board 
class FullCycleOYPB(object):

    def __init__(self, pins):
        self.pinColors = {"org":pins[0], "yel":pins[1], "pik":pins[2], "blu":pins[3]}
        self.pinOrder = ["org", "yel", "pik", "blu"]
        self.seqs = []
		
    def Build(self):
        seq = {"org":1, "yel":0, "pik":0, "blu":0}
        self.seqs.append(seq)
        seq = {"org":1, "yel":1, "pik":0, "blu":0}
        self.seqs.append(seq)       
        seq = {"org":0, "yel":1, "pik":0, "blu":0}
        self.seqs.append(seq)
        seq = {"org":0, "yel":1, "pik":1, "blu":0}
        self.seqs.append(seq)
        seq = {"org":0, "yel":0, "pik":1, "blu":0}
        self.seqs.append(seq)
        seq = {"org":0, "yel":0, "pik":1, "blu":1}
        self.seqs.append(seq)
        seq = {"org":0, "yel":0, "pik":0, "blu":1}
        self.seqs.append(seq)
        seq = {"org":1, "yel":0, "pik":0, "blu":1}
        self.seqs.append(seq)

# klasse voor stepper motor met 4 fazen + common (gehele stap sequentie)
# stepper 28BYJ-48 met ULN2003A driver board
class SimpleCycleOYPB(object):

    def __init__(self, pins):
        self.pinColors = {"org":pins[0], "yel":pins[1], "pik":pins[2], "blu":pins[3]}
        self.pinOrder = ["org", "yel", "pik", "blu"]
        self.seqs = []
        
		
    def Build(self):
        seq = {"org":1, "yel":0, "pik":0, "blu":0}
        self.seqs.append(seq)
        seq = {"org":0, "yel":1, "pik":0, "blu":0}
        self.seqs.append(seq)
        seq = {"org":0, "yel":0, "pik":1, "blu":0}
        self.seqs.append(seq)
        seq = {"org":0, "yel":0, "pik":0, "blu":1}
        self.seqs.append(seq)

# klasse om waarde van de pins op te halen en draairichting te bepalen
class Stepper(object):

    def __init__(self, delay, cycle):
        self.__delay = delay				# tijd tussen seq
        self.__seqs = cycle.seqs			# seq tabel
        self.__pins = cycle.pinOrder		# volgorde kleuren
        self.__cw = True					# wijzerzin
        self.__seqPos = 0					# positie in seq
        self.__pinPos = 0					# positie pin (kleur)
        self.__seqLen = len(self.__seqs)	# aantal seq  
        
    def setCW(self, cw=True):				# default wijzerzin
		self.__cw = cw

    def setDelay(self, delay):
		self.__delay = delay

    def nextPin(self):
		pinColor = ""						# init pinColor
		try:
			# kleur van de pin
			pinColor = self.__pins[self.__pinPos]
		except:
			time.sleep(self.__delay)		# delay voor volgende seq
			self.__pinPos = 0				# positie eerste pin
			pinColor = self.__pins[0]		# waarde eerste pin
			if self.__cw == True:			# wijzerzin
				self.__seqPos += 1			# positie + 1
			else:							# tegenwijzerzin
				self.__seqPos -= 1			# positie - 1
			if self.__seqPos >= self.__seqLen:	# test overflow positie
				self.__seqPos = 0
			if self.__seqPos < 0:			# test underflow positie
				self.__seqPos = self.__seqLen - 1
		# waarde van de pin
		val = self.__seqs[self.__seqPos][pinColor]
		self.__pinPos += 1					# pin positie ophogen
		return [pinColor, val]