import os, sys, subprocess, shlex, re, fnmatch
from subprocess import call
from pydub import AudioSegment
from scipy.io.wavfile import read,write

"""
IDENTIFICA EL FORMATO DEL AUDIO
Entrada: Direccion del audio
Salida: string identificando el formato del audio 
"""
def information_audio(address_file):
	cmnd = [
		'ffprobe','-v', 'error',
		'-show_entries', 'format=format_name', 
		'-of','default=noprint_wrappers=1:nokey=1', 
		address_file
	]
	p = subprocess.Popen(
		cmnd, stdout=subprocess.PIPE, 
		stderr=subprocess.PIPE
	)
	out, err =  p.communicate()	
	count=0									#type_audio = 0 -> mp3
	for word in out:							#type_audio = 1 -> wav	
		count=count+word				#type_audio = 2 -> formato no soportado
	if count == 282:
		type_audio=0
	elif count == 344:
		type_audio=1
	else:
		type_audio=2
		print("Format not supported")
	return type_audio

"""
CONVIERTE MP3 A WAV
Entrada: direccion del audio
Salida: direccion audio convertido
"""
def convertor(address_file):
	song = AudioSegment.from_mp3(address_file)
	address_clean = address_file.split(".")
	address_final = address_clean[0] + ".wav"
	song.export(address_final,format ="wav")
	return address_final

"""
EXTRAE INFORMACIÓN DEL AUDIO
Entrada: nombre del audio
Salida: arreglo numpy con datos del audio, frecuencia de muestreo
"""
def read_audio(name_audio):
	rate,info=read(name_audio)				#función de doble retorno?
	dimension = info[0].size					#data: datos del audio (arreglo de numpy)
	if dimension==1:							#rate: frecuencia de muestreo
		data = info
		perfect = 1
	else:
		data = info[:,dimension-1]
		perfect = 0
	return rate, data, perfect
