from scipy import fft, arange, ifft
from scipy.signal import bilinear, butter, lfilter

"""
FILTRO PASABANDA CALCULA LIMITES DEL PASABANDA
Entrada: información del audio
Salida: limites del pasabanda
"""
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


"""
APLICA EL FILTRO
Entrada: información del audio
Salida: arreglo numpy filtrado
"""
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

"""
FILTRO PASABANDA (Butterworth)
Entrada: información del audio
Salida: data filtrada
"""
def filter(data,rate):
	large = len(data)
	Y = fft(data)/large         				#Fast Fourier Transformation
	Y = Y[range(round(large/2))]
	freq_max=0;								
	cont = 0;
	for i in Y:
		cont = cont + 1							#count de posición
		if i>=freq_max:
			pos = cont 							#Posición de la frecuencia máxima
			freq_max=i 							#Frecuencia máxima
	frec = pos*rate/large
	fs = rate
	lowcut = frec*0.95
	highcut = frec*1.05
	y = butter_bandpass_filter(
		data, lowcut, highcut, fs, order=6)
	return y