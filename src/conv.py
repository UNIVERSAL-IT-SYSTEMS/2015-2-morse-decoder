import os, sys, subprocess, shlex, re, fnmatch
from subprocess import call
from pydub import AudioSegment

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