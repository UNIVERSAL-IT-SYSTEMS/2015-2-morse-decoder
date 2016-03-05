#testeando rama
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write
import os, sys, subprocess, shlex, re, fnmatch
from subprocess import call
from pydub import AudioSegment

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style

LARGE_FONT= ("Verdana", 12)
style.use("ggplot")
f = Figure(figsize=(3,3),dpi=100)

class ventanita(tk.Tk):
	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.frames = {}

		frame = StartPage(container, self)
		self.frames[StartPage] = frame
		frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

#PLOT DEL DOMINIO DEL TIEMPO
#Entrada: datos del audio
#Salida: datos del plot
def plotTiempo(data,rate,f=f):
	timp=len(data)/rate 
	t=linspace(0,timp,len(data))    #linspace(start,stop,number).Return evenly spaced numbers over a specified interval.
	a = f.add_subplot(5,1,1)
	a.plot(t, data)
	return f

#COMENTARIOOOOOOOOOOOOOOOO

#PLOT DEL DOMINIO DE LA FRECUENCIA
#Entrada: datos del audio
#Salida: datos del plot
def plotFrecuencia(data,rate,f=f):
	largo = len(data)
	b = f.add_subplot(5,1,3)
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
	return f

#CREA ESPECTOGRAMA DEL AUDIO
#Entrada: data del audio
#Salida: datos del specgram para su ploteo 
def spectrum(data,f=f):
	c = f.add_subplot(5,1,5)
	Pxx, freqs, bins, im = c.specgram(data)
	return f

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
def plotearAudio(f=f):
	app.fileName = filedialog.askopenfilename( filetypes = ( ("archivos wav","*.wav" ),("archivos mp3","*.mp3"),("All files","*.*") ) )
	nombreAudio = app.fileName
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

	canvas = FigureCanvasTkAgg(f, app)
	canvas.show()
	canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

	#barrita de funcionalidades de la gráfica
	toolbar = NavigationToolbar2TkAgg(canvas, app)
	toolbar.update()
	canvas._tkcanvas.pack(fill=tk.BOTH, expand = True)

	#label2 = tk.Label(app, text="Traducción... pronto", fg="blue", font=LARGE_FONT) #solo para dejar un espacio entre botón y gráfico
	#label2.pack(pady=10) 

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Welcome to the best morse decoder in the entire world!", fg="blue", font=LARGE_FONT)
        label.pack(pady=20, padx=10)
        boton = ttk.Button(self, text="Click me!", command=plotearAudio)
        boton.pack()
  

app = ventanita()
app.minsize(width=600, height=250)
#app.maxsize(width=400, height=400)

#app.iconbitmap('@dog.xbm')
#img = PhotoImage(file='your-icon')
#app.tk.call('wm', 'iconphoto', root._w, img)

app.title("The Puntorayas Inversionistas")
app.mainloop()