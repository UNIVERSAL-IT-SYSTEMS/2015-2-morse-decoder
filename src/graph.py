from scipy import fft, arange, ifft
import numpy as np
from numpy import sin, linspace, pi
from decoder import separar_audio
"""
PLOT DEL DOMINIO DEL TIEMPO
Entrada: datos del audio
Salida: datos del plot
"""
def plot_tiempo(data,rate,forma2,absolute=0):
	if absolute == 1:
		data = np.absolute(data)
	timp=len(data)/rate 
	t=linspace(0,timp,len(data))    			#linspace(start,stop,number)	
	p_tiempo = forma2.add_subplot(1,1,1)		#Return evenly spaced numbers over a specified interval.
	p_tiempo.set_title('Abs(audio)')
	p_tiempo.set_xlabel('Tiempo [s]')
	p_tiempo.set_ylabel('Amplitud [dB]')
	p_tiempo.plot(t, data)
	return forma2

"""
PLOT DEL DOMINIO DE LA FRECUENCIA
Entrada: datos del audio
Salida: datos del plot
"""
def plot_frecuencia(data,rate,forma):
	largo = len(data)
	p_frecuencia = forma.add_subplot(2,1,1)
	k = arange(largo)
	T = largo/rate
	frq = k/T                       			#Two sides frequency range
	frq = frq[range(round(largo/2))] 			#One side frequency range
	Y = fft(data)/largo         				#Fast Fourier Transformation
	Y = Y[range(round(largo/2))]

	p_frecuencia.plot(frq,abs(Y),'r')
	p_frecuencia.set_title('Gráficos de Frecuencia y Spectograma')
	p_frecuencia.set_xlabel('Magnitud')
	p_frecuencia.set_ylabel('Frecuencia [Hz]')
	return forma
"""
CREA ESPECTOGRAMA DEL AUDIO
Entrada: data del audio
Salida: datos del specgram para su ploteo 
"""
def spectrum(data,forma,rate):
	p_espec = forma.add_subplot(2,1,2)
	NFFT = 1024									#Largo de los ventanas de segmentos
	Pxx, freqs, bins, im = p_espec.specgram(
		data, NFFT=NFFT, Fs=rate
	)
	p_espec.set_xlabel('Tiempo [s]')
	p_espec.set_ylabel('Frecuencia')
	return forma

def plot_unos(data,rate,forma3):
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
	normal.set_title('Gráfico audio-morse')
	normal.set_xlabel('Tiempo [s]')
	normal.set_ylabel('Valor [1-0]')
	return forma3