import numpy as np
from scipy.io.wavfile import read,write
import matplotlib.pyplot as plt

def separar_audio(data,rate,threshold = 15000):
	lista = []
	for i in data:
		if i>= threshold:
			lista.append(1)
		else:
			lista.append(0)
	a = np.array(lista)
	plt.plot(a)
	plt.show()
