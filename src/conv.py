import os, sys, subprocess, shlex, re, fnmatch
from subprocess import call
from pydub import AudioSegment
from scipy.io.wavfile import read,write

"""
IDENTIFICA EL FORMATO DEL AUDIO
Entrada: Direccion del audio
Salida: string identificando el formato del audio 
"""
def informacionAudio(direccionArchivo):
	cmnd = ['ffprobe','-v', 'error', '-show_entries', 'format=format_name', '-of','default=noprint_wrappers=1:nokey=1', direccionArchivo]
	p = subprocess.Popen(cmnd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err =  p.communicate()	
	contador=0									#tipoAudio = 0 -> mp3
	for palabra in out:							#tipoAudio = 1 -> wav	
		contador=contador+palabra				#tipoAudio = 2 -> formato no soportado
	if contador == 282:
		#mp3
		tipoAudio=0
	elif contador == 344:
		#wav
		tipoAudio=1
	else:
		tipoAudio=2
		print("Formato no soportado")
	return tipoAudio

"""
CONVIERTE MP3 A WAV
Entrada: direccion del audio
Salida: direccion audio convertido
"""
def convertor(direccionArchivo):
	cancion = AudioSegment.from_mp3(direccionArchivo)
	direccionLimpia = direccionArchivo.split(".")
	direccionFinal = direccionLimpia[0] + ".wav"
	cancion.export(direccionFinal,format ="wav")
	return direccionFinal

def leerAudio(nombreAudio):
	rate,info=read(nombreAudio)					#función de doble retorno?
	dimension = info[0].size					#data: datos del audio (arreglo de numpy)
	if dimension==1:							#rate: frecuencia de muestreo
		data = info
	else:
		data = info[:,dimension-1]
	return rate, data