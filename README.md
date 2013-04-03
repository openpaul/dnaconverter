DNAconverter
============
The DNAconverter enables you to convert any digital file into a sequenz of DNA-base and back.

Why that?
Cause we can and its a convinient method to store information. Mother earth does it ;-)
https://en.wikipedia.org/wiki/DNA_digital_data_storage

The system is quiet easy to understand and follows some guidelines:

1. Digital files can be seen as binary data (e.g. 110101010...)
2. Binary data can be retrived and convertet into ternary data
3. Ternarydata can be convertet into DNA using the base AGTC as code
4. The first letter of each sequenz is beeing ignored. In this software we use an "A"


The conversion 
--------------
The meaning of each base changes depending on the preceding base. In that manner there wont be any double base pairs, because with the todays technology we are not able to read DNA with double bases.


| Values    | 0 | 1 | 2 |
|-----------|:---:|:---:|:---:|
|*preciding:* A | C | G | T |
|*preciding:* C | G | T | A |
|*preciding:* G | T | A | C |
|*preciding:* T | A | C| G |



Example
-------

Imagine we want to read the file "example.txt"
We read it byte for byte and retrive for each byte the integer (*int*) that represents the byte.
For Example: the byte 10101100 equals 172.
(1*2⁷+0*2⁶+1*2⁵...)

Now we can represent this number to the base of 3 by using the tenary system:
172 = 1*3⁰+0*3¹+1*3²+0*3³+2*3⁴

So 10101100 in the binary system equals to 10102 in the ternary system.

10102 now can be written using the bases with the encoding shown in the table. The first letter of each dna-file is A by convention:

AGTACA equals to: AG=1, GT=0, TA=1 ...


Roadmap
-------
1. To make script convert back and foreward every possible file
	- Done (28.03.2013): fixed error with integers > 242
	- Performance is very bad!
		- the performance improved a lot. Its now possible to encode or decode any file in a reasonable time. Just the encoded file is 6 times bigger because of the method used. Could be zipped in the future
2. Include Filename and some kind of indentifier
	- the first 64 bytes of each encodet file is the filename filled up with " "(spaces) until the end (so the maxlength of each filename would be 64 symbols!). this seems a lot, 384 bases are used for the filename. But we life in the 21th century and we do  not want o worry if our filename is to long or has some rare symbols in it. For that reason we use utf-8 encodeing for the filename
3. Split the string so they actually could be transcripted
	- goal would be something in the range of 100-150 basessegements and overlapping of > 50%


Dependecies
-----------
Depends on python3
Tested on Ubuntu 12_04


tutorial
--------
1. Download the zipped branch and unzip it
2. Have python3 installed
3. open terminal in the diretory with the scripts includet
4. Copy any files into the input folder (no folders, just files!).
	- remove old files out of the other folders
	- try it out with small files first < 1Mb (I've already converted > 1GB)
5. run dnaEncode.py
6. open any file in the "inputencoded"-folder with any editor to see the DNA-sequenz (Caution, they are 6 times the size now!)
7. run dnaDecode.py to decode the files
8. see the decoded files in the output-dir 
