from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write
from tkinter import filedialog
from tkinter import *
import matplotlib.pyplot as plt
import os, sys, subprocess, shlex, re, fnmatch
from subprocess import call
from pydub import AudioSegment

#PLOT DEL DOMINIO DEL TIEMPO
#Entrada: datos del audio
#Salida: datos del plot
def plotTiempo(data,rate):
	timp=len(data)/rate	
	t=linspace(0,timp,len(data))	#linspace(start,stop,number).Return evenly spaced numbers over a specified interval.
	plt.subplot(3,1,1)
	plt.plot(t,data)
	#plt.title("Dominio en el tiempo")
	plt.xlabel('Tiempo (s)')
	plt.ylabel('Amplitud')

#PLOT DEL DOMINIO DE LA FRECUENCIA
#Entrada: datos del audio
#Salida: datos del plot
def plotFrecuencia(data,rate):
	largo = len(data)
	plt.subplot(3,1,2)
	k = arange(largo)
	T = largo/rate
	frq = k/T 						# two sides frequency range
	frq = frq[range(round(largo/2))] # one side frequency range

	Y = fft(data)/largo			#Fast Fourier Transformation
	Y = Y[range(round(largo/2))]

	plt.plot(frq,abs(Y),'r') 		#Plot del espectro de frecuencia
	#bp=Y[:]  
	#for i in range(len(bp)): # (H-red)  
	#	if i>=10000:
	#		bp[i]=0
	#plt.plot(frq,abs(bp),'r') 		#Plot del espectro de frecuencia
	#plt.title("Dominio en la frecuencia")
	plt.xlabel('Frecuencia (Hz)')
	plt.ylabel('|F(w)|')

#CREA ESPECTOGRAMA DEL AUDIO
#Entrada: data del audio
#Salida: datos del specgram para su ploteo 
def spectrum(data):
	plt.subplot(3,1,3)
	Pxx, freqs, bins, im = plt.specgram(data)

#IDENTIFICA EL FORMATO DEL AUDIO
#Entrada: Direccion del audio
#Salida: string identificando el formato del audio 
def informacionAudio(direccionArchivo):
    cmnd = ['ffprobe','-v', 'error', '-show_entries', 'format=format_name', '-of','default=noprint_wrappers=1:nokey=1', direccionArchivo]
    p = subprocess.Popen(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err =  p.communicate()
    contador=0
    #tipoAudio=0=mp3
    #tipoAdio=1=wav
    #tipoAudio=2=formato no soportado
    for palabra in out:
    	contador=contador+palabra
    if contador == 282:
    	#mp3
    	tipoAudio=0
    elif contador == 344:
    	#wav
    	tipoAudio=1
    else:
    	#se deberia poner aca un mensaje de error! (con alguna ventana emergente y permitir al usuario buscar denuevo)
    	tipoAudio=2
    	print("Formato no soportado")
    return tipoAudio

#CONVIERTE MP3 A WAV
#Entrada: direccion del audio
#Salida: direccion audio convertido
def convertor(direccionArchivo):
	cancion = AudioSegment.from_mp3(direccionArchivo)
	direccionLimpia = direccionArchivo.split(".")
	direccionFinal = direccionLimpia[0] + ".wav"
	cancion.export(direccionFinal,format ="wav")
	return direccionFinal

#CAPTURA DE AUDIO 
def pedirAudio():
	window.fileName = filedialog.askopenfilename( filetypes = ( ("archivos wav","*.wav" ),("archivos mp3","*.mp3"),("All files","*.*") ) )
	nombreAudio = window.fileName
	tipoAudio = informacionAudio(nombreAudio)
	if tipoAudio == 0:
		nombreAudio = convertor(nombreAudio)
	
	rate,info=read(nombreAudio)		#función de doble retorno?
	dimension = info[0].size		#data: datos del audio (arreglo de numpy)
	if dimension==1:				#rate: frecuencia de muestreo
		data = info
	else:
		data = info[:,dimension-1]		

	plotTiempo(data,rate)
	plotFrecuencia(data,rate)
	spectrum(data)
	plt.show()


window = Tk()
window.title("The Puntorayas Inversionistas")
B = Button(window, text ="Buscar Audio", command = pedirAudio)
B.pack()
window.mainloop()
