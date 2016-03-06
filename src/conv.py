import os, sys, subprocess, shlex, re, fnmatch
from subprocess import call
from pydub import AudioSegment
from scipy.io.wavfile import read,write

"""
IDENTIFICA EL FORMATO DEL AUDIO
Entrada: Direccion del audio
Salida: string identificando el formato del audio 
"""
def informacion_audio(direccion_archivo):
	cmnd = [
		'ffprobe','-v', 'error',
		'-show_entries', 'format=format_name', 
		'-of','default=noprint_wrappers=1:nokey=1', 
		direccion_archivo
	]
	p = subprocess.Popen(
		cmnd, stdout=subprocess.PIPE, 
		stderr=subprocess.PIPE
	)
	out, err =  p.communicate()	
	contador=0									#tipoAudio = 0 -> mp3
	for palabra in out:							#tipoAudio = 1 -> wav	
		contador=contador+palabra				#tipoAudio = 2 -> formato no soportado
	if contador == 282:
		tipoAudio=0
	elif contador == 344:
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
def convertor(direccion_archivo):
	cancion = AudioSegment.from_mp3(direccion_archivo)
	direccionLimpia = direccion_archivo.split(".")
	direccionFinal = direccionLimpia[0] + ".wav"
	cancion.export(direccionFinal,format ="wav")
	return direccionFinal

def leer_audio(nombreAudio):
	rate,info=read(nombreAudio)					#función de doble retorno?
	dimension = info[0].size					#data: datos del audio (arreglo de numpy)
	if dimension==1:							#rate: frecuencia de muestreo
		data = info
	else:
		data = info[:,dimension-1]
	return rate, data