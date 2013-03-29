import os

class decodedna:
	def __init__(self,filename):
	#erstmal datei einlesen
		print("We decode")
		self.readfile(filename)
		print("We are done")

	def readfile(self,filename):
		# conversion from DNA
		retrive = {"AG":0,"GC":0,"CT":0,"TA":0,
				   "AC":1,"GT":1,"CA":1,"TG":1,
				   "AT":2,"GA":2,"CG":2,"TC":2}

		frame = bytearray()
		inputdir = "inputencoded/%s" % (filename)
		with open(inputdir, "r") as in_file:
			n = in_file.read()	
			last = n[0:1] #first base
			i = 0
			c = 0 # every trimer has 6 values
			
			byteint = 0 #the actual encodet byte		
			
			for base in n:
				#print(base)
				#erster buchstabe und zeilenumbruch wird ignoriert
				if( i > 0 and base != "\n"):
					dimer = last + base
					value = retrive[dimer]
					#print(c)
					last = base
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
					if(c == 6):
						#print("done")
						#print(byteint)
						#print(bytes(byteint))
						frame.append(byteint)
				i = i + 1

			self.createfile(frame,filename)
	def createfile(self,frame,filename):
		outputdir = "output/%s" % (filename)
		with open(outputdir, "wb") as out_file:
			out_file.write(frame)


for files in os.listdir("inputencoded"):
	decodedna(files)
