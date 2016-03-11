from scipy import fft, arange, ifft
import numpy as np
from numpy import sin, linspace, pi
from decoder import separate_audio
"""
PLOT DEL DOMINIO DEL TIEMPO
Entrada: datos del audio
Salida: datos del plot
"""
def plot_time(data,rate,forma2,absolute=0):
	if absolute == 1:
		data = np.absolute(data)
	timp=len(data)/rate 
	t=linspace(0,timp,len(data))    			#linspace(start,stop,number)	
	p_time = forma2.add_subplot(1,1,1)		#Return evenly spaced numbers over a specified interval.
	p_time.set_title('Abs(audio)')
	p_time.set_xlabel('Tiempo [s]')
	p_time.set_ylabel('Amplitud [dB]')
	p_time.plot(t, data)
	return forma2

"""
PLOT DEL DOMINIO DE LA FRECUENCIA
Entrada: datos del audio
Salida: datos del plot
"""
def plot_frecuency(data,rate,forma):
	large = len(data)
	p_frecuency = forma.add_subplot(2,1,1)
	k = arange(large)
	T = large/rate
	frq = k/T                       			#Two sides frequency range
	frq = frq[range(round(large/2))] 			#One side frequency range
	Y = fft(data)/large         				#Fast Fourier Transformation
	Y = Y[range(round(large/2))]

	p_frecuency.plot(frq,abs(Y),'r')
	p_frecuency.set_title('Gráficos de Frecuencia y Spectograma')
	p_frecuency.set_xlabel('Magnitud')
	p_frecuency.set_ylabel('Frecuencia [Hz]')
	return forma

"""
CREA ESPECTOGRAMA DEL AUDIO
Entrada: data del audio
Salida: datos del espectograma para su ploteo 
"""
def spectrum(data,forma,rate):
	p_espec = forma.add_subplot(2,1,2)
	NFFT = 1024									#large de los ventanas de segmentos
	Pxx, freqs, bins, im = p_espec.specgram(
		data, NFFT=NFFT, Fs=rate
	)
	p_espec.set_xlabel('Tiempo [s]')
	p_espec.set_ylabel('Frecuencia')
	return forma

def plot_ones(data,rate,forma3):
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
	normal = forma3.add_subplot(1,1,1)
	normal.fill_between(range(len(uno)),uno)
	normal.set_title('Gráfico audio-morse')
	normal.set_xlabel('Tiempo [s]')
	normal.set_ylabel('Valor [1-0]')
	return forma3