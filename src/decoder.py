import numpy as np
from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt
from math import fabs
from translator import *

def separate_audio(data,rate):
	lista = []
	data = np.absolute(data)
	max_value = np.amax(data)
	media = data.mean()
	threshold = ((max_value + media)/2)*1.1
	#print(threshold)
	for i in data:
		if i>= threshold:
			lista.append(1)
		else:
			lista.append(0)
	a = np.array(lista)
	return a

def ones_audio(data,rate):
	piece = 2*round(len(data)/rate)
	perfect=separate_audio(data,rate)
	lista = []
	uno = np.array(lista)
	cont = 0
	prom = 0
	for i in perfect:
		cont = cont + 1
		prom = prom + i
		if cont == piece:
			cont = 0
			prom = prom/piece
			if prom > 0:
				uno = np.append(uno,np.ones(piece))
			else:
				uno = np.append(uno,np.zeros(piece))
			prom = 0
	return count(uno)


def count(data):
	min0 = 9999999
	max0 = 0
	min1 = 9999999
	max1 = 0
	count = 1
	for i in range(1,len(data)):
		if data[i]==data[i-1]:
			count = count + 1
		else:
			if data[i]==0:
				if count >= max1:
					max1 = count
				if count <= min1:
					min1 = count
			else:
				if count >= max0:
					max0 = count
				if count <= min0:
					min0 = count
			count = 1
	#	print("max 1: ",max1)
	#	print("min 1: ",min1)
	#	print("max 0: ",max0)
	#	print("min 0: ",min0)
	return detector(data,max1,min1,min0)

def detector(data,max1,min1,min0):
	morse = ""
	count = 1
	for i in range(1,len(data)-1):
		if data[i]==data[i+1]:
			count = count + 1
		else:
			if data[i-1]==1:
				dif_max1 = fabs(max1-count)
				dif_min1 = fabs(min1-count)
				if dif_max1 > dif_min1:
					morse = morse + "."
				else:
					morse = morse + "-"
			else:
				if count > 2*min0:
					morse = morse + " "
			count = 0
	#print(decode_morse(morse))
	return morse


