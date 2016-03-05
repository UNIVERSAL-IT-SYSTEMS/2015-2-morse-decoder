from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

#PLOT DEL DOMINIO DEL TIEMPO
#Entrada: datos del audio
#Salida: datos del plot
def plotTiempo(data,rate,forma):
	timp=len(data)/rate 
	t=linspace(0,timp,len(data))    #linspace(start,stop,number).Return evenly spaced numbers over a specified interval.
	a = forma.add_subplot(5,1,1)
	a.plot(t, data)
	return forma

#PLOT DEL DOMINIO DE LA FRECUENCIA
#Entrada: datos del audio
#Salida: datos del plot
def plotFrecuencia(data,rate,forma):
	largo = len(data)
	b = forma.add_subplot(5,1,3)
	k = arange(largo)
	T = largo/rate
	frq = k/T                       # two sides frequency range
	frq = frq[range(round(largo/2))] # one side frequency range

	Y = fft(data)/largo         #Fast Fourier Transformation
	Y = Y[range(round(largo/2))]
	b.plot(frq,abs(Y),'r') 
	#bp=Y[:]  
	#for i in range(len(bp)): # (H-red)  
	#	if i>=10000:
	#		bp[i]=0
	return forma

#CREA ESPECTOGRAMA DEL AUDIO
#Entrada: data del audio
#Salida: datos del specgram para su ploteo 
def spectrum(data,forma):
	c = forma.add_subplot(5,1,5)
	Pxx, freqs, bins, im = c.specgram(data)
	return forma