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
forma = Figure(figsize=(2,2),dpi=100)
forma2 = Figure(figsize=(2,2), dpi=100)
forma3 = Figure(figsize=(2,2), dpi=100)
translated_code = "hola"


class application(tk.Tk):
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

"""
SOLICITA AUDIO Y LLAMA A LAS FUNCIONES QUE LO ANALIZAN
Entrada: 
Salida: 
"""
def plot_audio(forma=forma):
	app.fileName = filedialog.askopenfilename( 
		filetypes = ( 
			("All files","*.*"), 
			("archivos wav","*.wav" ),
			("archivos mp3","*.mp3") 
		) 
	)
	name_audio = app.fileName
	type_audio = information_audio(name_audio)
	if type_audio == 0:
		name_audio = convertor(name_audio)
	print(name_audio)
	
	"""
	Procesamiento de datos
	"""
	rate, data, perfect = read_audio(name_audio)
	
	if perfect == 0:
		data = filter(data,rate)
	plot_frecuency(data,rate,forma)
	spectrum(data,forma,rate)
	plot_time(data,rate,forma2,1)
	plot_ones(data,rate,forma3)

	captured_code = ones_audio(data,rate)
	translated_code = decode_morse(captured_code)

	print()
	print(captured_code)
	print(translated_code)
	print()

"""
PÁGINAS/VENTANAS DEL PROGRAMA
"""
class start_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Welcome to the best morse decoder in the entire world!", fg="blue", font=LARGE_FONT)
		label.pack(pady=20, padx=10)
		button_load = Button(self, text="Load audio", command=plot_audio, height = 1, width = 13)
		button_load.pack()

		button_graph = Button(self, text="Show more graphs", command=lambda: controller.show_frame(graphs_page), height = 1, width = 13)
		button_graph.pack(padx=4, pady=10)

		button_graph2 = Button(self, text="Show sound graph", command=lambda: controller.show_frame(graphs_page2), height = 1, width = 13)
		button_graph2.pack()


		canvas1 = Canvas(self, height=30)
		canvas1.pack(side = tk.TOP, fill = BOTH, expand = True)
		label = Label(canvas1, text="Audio translation is:", fg="blue", font=LARGE_FONT)
		label.pack(side=tk.LEFT)

		label_translate = Label(canvas1, text=translated_code, fg="black", font=LARGE_FONT)
		label_translate.pack(side=tk.LEFT)


		canvas = FigureCanvasTkAgg(forma2, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True)

		#barra de navegación matplotlib
		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)



class graphs_page(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Graph page", fg="red", font=LARGE_FONT)
		label.pack(pady=20, padx=10)
		button_back = ttk.Button(self, text="Back to principal page", command=lambda: controller.show_frame(start_page))
		button_back.pack(padx=4, pady=10)

		canvas = FigureCanvasTkAgg(forma, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		#barra de navegación matplotlib
		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(fill=tk.BOTH, expand = True)


class graphs_page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Graph page 2 - Sound graph", fg="black", font=LARGE_FONT)
		label.pack(pady=20, padx=10)
		button_back = ttk.Button(self, text="Back to principal page", command=lambda: controller.show_frame(start_page))
		button_back.pack(padx=4, pady=10)

		canvas = FigureCanvasTkAgg(forma3, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

		#barrita de funcionalidades de la gráfica
		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(fill=tk.BOTH, expand = True)


app = application()
app.minsize(width=1200, height=600)
app.title("The Puntorayas Inversionistas")
app.mainloop()
