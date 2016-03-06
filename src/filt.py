from scipy import fft, arange, ifft
from scipy.signal import bilinear

"""
FILTRO PASABANDA
Entrada: información del audio
Salida: data filtrada
"""
def filter_passband(data,rate):
	largo = len(data)
	Y = fft(data)/largo         				#Fast Fourier Transformation
	Y = Y[range(round(largo/2))]
	freq_max=0;								
	cont = 0;
	for i in Y:
		cont = cont + 1							#contador de posición
		if i>=freq_max:
			pos = cont 							#Posición de la frecuencia máxima
			freq_max=i 							#Frecuencia máxima
	for i in range(len(Y)):
		if( (i > pos*1.025) or (i < pos*0.975)):
			Y[i]=0								#filtro al rededor de la frecuencia máxima
	data = ifft(Y)
	return data