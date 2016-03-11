import numpy as np
from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt
from math import fabs
from translator import *

def separar_audio(data,rate):
	lista = []
	data = np.absolute(data)
	maximo_valor = np.amax(data)
	media = data.mean()
	threshold = ((maximo_valor + media)/2)*1.1
	#print(threshold)
	for i in data:
		if i>= threshold:
			lista.append(1)
		else:
			lista.append(0)
	a = np.array(lista)
	return a

def unos_audio(data,rate):
	trozo = 2*round(len(data)/rate)
	perfect=separar_audio(data,rate)
	lista = []
	uno = np.array(lista)
	cont = 0
	prom = 0
	for i in perfect:
		cont = cont + 1
		prom = prom + i
		if cont == trozo:
			cont = 0
			prom = prom/trozo
			if prom > 0:
				uno = np.append(uno,np.ones(trozo))
			else:
				uno = np.append(uno,np.zeros(trozo))
			prom = 0
	return contador(uno)


def contador(data):
	min0 = 9999999
	max0 = 0
	min1 = 9999999
	max1 = 0
	contador = 1
	for i in range(1,len(data)):
		if data[i]==data[i-1]:
			contador = contador + 1
		else:
			if data[i]==0:
				if contador >= max1:
					max1 = contador
				if contador <= min1:
					min1 = contador
			else:
				if contador >= max0:
					max0 = contador
				if contador <= min0:
					min0 = contador
			contador = 1
	#	print("max 1: ",max1)
	#	print("min 1: ",min1)
	#	print("max 0: ",max0)
	#	print("min 0: ",min0)
	return detector(data,max1,min1,min0)

def detector(data,max1,min1,min0):
	morse = ""
	contador = 1
	for i in range(1,len(data)-1):
		if data[i]==data[i+1]:
			contador = contador + 1
		else:
			if data[i-1]==1:
				dif_max1 = fabs(max1-contador)
				dif_min1 = fabs(min1-contador)
				if dif_max1 > dif_min1:
					morse = morse + "."
				else:
					morse = morse + "-"
			else:
				if contador > 2*min0:
					morse = morse + " "
			contador = 0
	#print(decode_morse(morse))
	return morse


