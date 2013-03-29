DNAconverter
============
The DNAconverter enables you to convert any digital file into a sequenz of DNA-base

The system is quiet easy to understand and follows some guidelines:

1. Digital files can be seen as binary data (e.g. 110101010...)
2. Binary data can be retrived and convertet into ternary data
3. Ternarydata can be convertet into DNA using the base AGTC as code
4. The first letter of each sequenz is beeing ignored. And it should be an A, by convention.



The conversion 
--------------
The meaning of each base changes depending on the preceding base. in that manner there wont be any double base pairs, because with the todays technology we are not able to read DNA with double bases.

| Values    | 0 | 1 | 2 |
|-----------|:---:|:---:|:---:|
|*preciding:* A | G | C | T |
|*preciding:* G | C | T | A |
|*preciding:* C | T | A | G |
|*preciding:* T | A | G | C |



Example
-------

We want to read the file "test.txt"
We read it byte for byte and retrive for each byte the int that represents the byte.
For Example: the byte 10101100 is the same as 172
(1*2⁷+0*2⁶+1*2⁵...)

Now we can represent this number to the base of 3 by using the tenary system:
172 = 1*3⁰+0*3¹+1*3²+0*3³+2*3⁴

So 10101100 in the binary system equals to 10102 in the ternary system.

10102 now can be written using the bases with the encoding shown in the table. The first letter is A by convention:

ACTGCG equals to: AC=1, CT=0, TG=1 ...


Roadmap
-------
1. To make script convert back and foreward every possible file
	- Done (28.03.2013): fixed error with integers > 242
	- Performance is very bad!
		- the performance improved a lot. Its now possible to encode or decode any file in a reasonable time. Just the encoded file is 6 times bigger because of the method used. Could be zipped in the future
2. Include Filename and some kind of indentifier
3. Split the string so they actually could be transcripted

Goal
----
Actually produce some DNA and reverse transcript it back, so we can see if it is possible.

Dependecies
-----------
Depends on python3
Tested on Ubuntu 12_04
