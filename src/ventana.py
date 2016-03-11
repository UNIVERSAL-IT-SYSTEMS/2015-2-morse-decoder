import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style

from graph import *
from conv import *
from filt import *
from translator import *
from decoder import *


LARGE_FONT= ("Verdana", 12)
#style.use("ggplot")
forma = Figure(figsize=(2,2),dpi=100)
forma2 = Figure(figsize=(2,2), dpi=100)
forma3 = Figure(figsize=(2,2), dpi=100)

class ventanita(tk.Tk):
	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.frames = {}

		for pages in (start_page, graphs_page, graphs_page2):
			frame = pages(container, self)
			self.frames[pages] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(start_page)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


def plotear_audio(forma=forma):
	app.fileName = filedialog.askopenfilename( 
		filetypes = ( 
			("All files","*.*"), 
			("archivos wav","*.wav" ),
			("archivos mp3","*.mp3") 
		) 
	)
	nombre_audio = app.fileName
	tipoAudio = informacion_audio(nombre_audio)
	if tipoAudio == 0:
		nombre_audio = convertor(nombre_audio)
	print(nombre_audio)
	
	"""
	Procesamiento de datos
	"""
	rate, data = leer_audio(nombre_audio)
	
	data = filtrador(data,rate)
	plot_frecuencia(data,rate,forma)
	spectrum(data,forma,rate)
	plot_tiempo(data,rate,forma2,1)
	print(decode_morse(".... --- .-.. .- / -- ..- -. -.. ---"))
	print(encode_morse("hola mundo"))
	unos_audio(data,rate,forma3)
	

class start_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Welcome to the best morse decoder in the entire world!", fg="blue", font=LARGE_FONT)
		label.pack(pady=20, padx=10)
		boton_load = Button(self, text="Load audio", command=plotear_audio, height = 1, width = 13)
		boton_load.pack()

		boton_graph = Button(self, text="Show more graphs", command=lambda: controller.show_frame(graphs_page), height = 1, width = 13)
		boton_graph.pack(padx=4, pady=10)

		boton_graph2 = Button(self, text="Show sound graph", command=lambda: controller.show_frame(graphs_page2), height = 1, width = 13)
		boton_graph2.pack()


		canvas1 = Canvas(self, height=30)
		canvas1.pack(side = tk.TOP, fill = BOTH, expand = True)
		label = Label(canvas1, text="La traducción del audio morse es:", fg="blue", font=LARGE_FONT)
		label.pack(side=tk.LEFT)

		canvas = FigureCanvasTkAgg(forma2, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True)

		#barrita de funcionalidades de la gráfica
		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)



class graphs_page(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Graph page", fg="red", font=LARGE_FONT)
		label.pack(pady=20, padx=10)
		boton_back = ttk.Button(self, text="Back to principal page", command=lambda: controller.show_frame(start_page))
		boton_back.pack(padx=4, pady=10)

		canvas = FigureCanvasTkAgg(forma, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		#barrita de funcionalidades de la gráfica
		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(fill=tk.BOTH, expand = True)


class graphs_page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Graph page 2 - Sound graph", fg="black", font=LARGE_FONT)
		label.pack(pady=20, padx=10)
		boton_back = ttk.Button(self, text="Back to principal page", command=lambda: controller.show_frame(start_page))
		boton_back.pack(padx=4, pady=10)

		canvas = FigureCanvasTkAgg(forma3, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		#barrita de funcionalidades de la gráfica
		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(fill=tk.BOTH, expand = True)


app = ventanita()
app.minsize(width=1200, height=600)
#app.attributes("-fullscreen", True) 
app.title("The Puntorayas Inversionistas")
#app.iconbitmap('@image.xbm')
app.mainloop()
