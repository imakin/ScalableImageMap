#!/usr/bin/env python

data = '<area shape="poly" coords="218,238,196,270,326,354,419,296,417,299,392,290,389,290,338,274,337,274" onmouseover="onJazzExh" href="#gd_even_details" />'
angka = data[data.find("coords=\"")+len("coords=\""):][:data[data.find("coords=\"")+len("coords=\""):].find("\"")]

#scale is 350:510 for both width and height
origin = 510
scaled = 350

res = ""

while len(angka)>1:
	if angka.find(",")!=(-1):
		res = res + str(350*int(angka[:angka.find(",")])/510)+","
		angka = angka[angka.find(",")+1:]
	else:
		res = res + str(350*int(angka)/510)
		angka = ""
print res
