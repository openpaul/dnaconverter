# some variables
hugetryte = ""
DNA       = "A"

#conversion to DNA
# lastlettervalue:letter
next = {"A0":"G",
		"A1":"C",
		"A2":"T",
		"G0":"C",
		"G1":"T",
		"G2":"A",
		"C0":"T",
		"C1":"A",
		"C2":"G",
		"T0":"A",
		"T1":"G",
		"T2":"C"}

# conversion from DNA
retrive = {"AG":0,"GC":0,"CT":0,"TA":0,
		   "AC":1,"GT":1,"CA":1,"TG":1,
		   "AT":2,"GA":2,"CG":2,"TC":2}

class encodedna:
	def __init__(self):
	#erstmal datei einlesen
		self.readfile()

	# this opens any file and converts it into DNA
	def readfile(self):
		global hugetryte
		global DNA
		#open file trough path
		with open("test.txt", "rb") as in_file:
			byte = in_file.read(1)	
			while byte:
				#here we got the bytes
				for item in bytes(byte):
					#each int now needs to be calculatet as ternary number
					# so we divide trough3 and as our new format will have the base of 6 we will have to make 6 iterations until there is no rest
					dnaint = item
					rest   = dnaint
					i      = 6 #number of iterations
					ternary = list()
					while i > 0:
						number = dnaint//3
						rest   = dnaint%3
						dnaint = number
						i      = i - 1 # next iteration
						ternary.append(rest)
						#print(rest)
					#print(item)
					self.createtryte(ternary)
				byte = in_file.read(1)	
		self.converttryte2DNA(hugetryte)
		self.createfasta(DNA)
	
	# this function creates little trytes and then appends them to the huge on
	def createtryte(self, ternary):
		tryte = str()
		for n in ternary:
			tryte += str(n)
		self.createmegatryte(tryte)

	# this function creates one huge tryte
	def createmegatryte(self,tryte):
		global hugetryte
		hugetryte += tryte

	def converttryte2DNA(self,ternary):
		global DNA
		global next		
		last = "A"
		length = len(ternary)
		a = 0
		while length > 0:
			
			dimer = last + ternary[a:a+1]
			last = next[dimer]
			DNA += last
			#print dimer;
			length = length -1
			a      = a + 1
	def createfasta(self,DNA):
		with open("dna.fasta", "w") as out_file:
			out_file.write(DNA)
		
encodedna()
