import numpy as np
from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt

def separar_audio(data,rate,threshold = 15000):
	lista = []
	data = np.absolute(data)
	maximo_valor = np.amax(data)
	print ("maximo valor",maximo_valor)
	minimo_valor = np.amin(data)
	print ("minimo valor",minimo_valor)
	
	for i in data:
		if i>= threshold:
			lista.append(1)
		else:
			lista.append(0)
	a = np.array(lista)
	return a

def unos_audio(data,rate,forma3):
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
	normal = forma3.add_subplot(1,1,1)
	normal.fill_between(range(len(uno)),uno)
	return forma3






