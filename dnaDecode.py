# conversion from DNA
retrive = {"AG":0,"GC":0,"CT":0,"TA":0,
		   "AC":1,"GT":1,"CA":1,"TG":1,
		   "AT":2,"GA":2,"CG":2,"TC":2}


class decodedna:
	def __init__(self):
	#erstmal datei einlesen
		self.readfile()

	def readfile(self):
		global retrive
		frame = bytearray()
		with open("data/dna_output.fasta", "r") as in_file:
			n = in_file.read(1)	
			last = n
			i = 0
			c = 0 # every trimer has 6 values
			
			byteint = 0 #the actual encodet byte		

			while n:
				#print(n)
				#erster buchstabe und zeilenumbruch wird ignoriert
				if( i > 0 and n != "\n"):
					dimer = last + n
					value = retrive[dimer]
					#print(c)
					last = n
					#print(value)
					
					if(c < 6):
						#print(value)
						byteint = byteint + value*(3**c)
						c = c + 1
					else:
						#print(value)
						byteint = value*(3**0)					
						c       = 1
					#ausgabe des int					
					if(c == 5):
						#print(bytes(byteint))
						frame.append(byteint)
				i = i + 1
				n = in_file.read(1)

			self.createfile(frame)
	def createfile(self,frame):
		with open("data/output.txt", "wb") as out_file:
			out_file.write(frame)

decodedna()
