from graph import *
from conv import *

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
forma = Figure(figsize=(5,1),dpi=100)

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

def plotearAudio(forma=forma):
	app.fileName = filedialog.askopenfilename( filetypes = ( ("All files","*.*"), ("archivos wav","*.wav" ),("archivos mp3","*.mp3") ) )
	nombreAudio = app.fileName
	tipoAudio = informacionAudio(nombreAudio)
	if tipoAudio == 0:
		nombreAudio = convertor(nombreAudio)
	
	rate, data = leerAudio(nombreAudio)
	#data = filter_passband(data,rate)
	plotTiempo(data,rate,forma)
	plotFrecuencia(data,rate,forma)
	spectrum(data,forma,rate)

	canvas = FigureCanvasTkAgg(forma, app)
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