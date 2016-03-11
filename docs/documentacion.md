# Morse-Decoder
**Decodificador de código morse a partir de audio de transmisiones satelitales**

Integrantes:
	* Nicole Macarena Henríquez Sepúlveda
	* Katherine Marcela Liberona Irarrazabal
	* Maximiliano Felipe Andrés Pérez Rodríguez


Contenidos:
	* [Introducción](#introducción)
	* [Bibliotecas y paquetes utilizados](#bibliotecas-y-paquetes-utilizados)
	* [Componentes del programa](#componentes-del-programa)
	* [Funcionalidad](#funcionalidad)
	* [Manual de usuario](#manual-de-usuario)



##Introducción##
En primer lugar es necesario entender con qué se trabaja en este programa; el Código Morse.
[**Código Morse:**](http://www.codigomorse.com/) Es un código o sistema de comunicación que permite la comunicación telegráfica a través de la transmisión de impulsos eléctricos de longitudes diversas o por medios visuales, como luz, sonoros o mecánicos. Este código consta de una serie de puntos, rayas y espacios, que al ser combinados entre si pueden formar palabras, números y otros símbolos.

El objetivo del programa es analizar el audio que recibe como entrada, para que por medio de la frecuencia detectar los componentes del morse; puntos, rayas, espacios entre letras y espacios entre palabras, y así poder traducir el mensaje que se transmite.


##Bibliotecas y paquetes utilizados##

La mayoría de los paquetes y librerias de python son instaladas fácilmente mediante *pip*, que es un gestor de paquetes proporcionados por python.

[**Scipy:**](http://www.scipy.org/) Biblioteca de código abierto, enfocada principalmente en el área matemática, ciencias e ingeniería. Permite utilizar funciones que cumplen el mismo objetivo que las de *Matlab*, pero en *Python*. El uso de esta biblioteca en el programa es a tráves de la función *FFT*, la cual permite calcular la transformada de Fourier de los datos obtenidos de un audio, dichos datos también son obtenidos usando *Scipy*. También es usado para calcular variables estadísticas como la media, desviación estándar, máximos y mínimos. 

[**Numpy:**](http://www.numpy.org/) Biblioteca de funciones que permite trabajar tanto con vectores como con matrices, a través de funciones matemáticas de alto nivel. Las matrices que representan los audios con los que se trabaja en este programa son matrices del tipo *numpy*, lo que conlleva a que puedan ser trabajadas matemáticamente de forma más sencilla. 

[**Tkinter:**](https://wiki.python.org/moin/TkInter) Es una adaptación de la biblioteca *Tlc/tk* para su utilización en *Python*. Permite tener un estándar para la interfaz gráfica de usuario. Se entiende que los botones y las ventanas del programa serán creadas a partir de esta biblioteca.

[**Matplotlib:**](http://matplotlib.org/) Esta biblioteca permite la generación de gráficos, obtenidos a partir de los datos de *arrays* o listas. Los espectros, tanto en el dominio del tiempo como de la frecuencia, el espectograma y la gráfica del audio serán presentados usando los gráficos que entrega *Matplotlib*.

[**Ffmepg:**](https://www.ffmpeg.org/) Biblioteca que permite que *Python* trabaje con audios de extensión mp3, ya que nativamente solo trabaja con wav. De este modo es posible escoger cualquiera de los dos tipos de audio para usar el decodificador.

[**PyDub:**](https://github.com/jiaaro/pydub/blob/master/API.markdown) Como el módulo pylab de *Matplotlib* trabaja nativamente con wav para plotear los datos es necesario el uso de esta biblioteca para realizar la conversión de mp3 a wav.

![Gráfico](http://i.imgur.com/INpX1uZ.png?1 "Presentación gráficas de frecuencia y espectograma")


##Componentes del programa##
[**Fitro:**]


[**Decodificador:**]


[**Traductor:**]


##Funcionalidad##

El programa actual está basado, principalmente, en uno encontrado en internet creado por [haskell](https://sites.google.com/site/haskell102/home/frequency-analysis-of-audio-file-with-python-numpy-scipy). Este programa tuvo que ser estudiado y modificado para que sea capaz de trabajar frente a cualquier formato de audio del tipo punto wav.

Con la ayuda de Tkinter, al ejecutar el programa, se despliega una ventana con tres botones. El botón 'Load audio', al presionarlo, abre el 'gestor de archivos' que permite seleccionar el audio con extensión wav o mp3. Se hace el llamado a la función *plot_audio*, que por medio de las funciones *information_audio* determina el tipo de audio, *convertor* realiza la conversión a wav para trabajar y *read_audio* extrae los datos del audio y la frecuencia de muestreo.

Luego se realiza el filtrado de audio para eliminar el ruido, la función *filter* retorna así los datos del audio filtrados para seguir trabajando. Con esta información y la frecuencia de muestreo se hace el llamado a las funciones *plot_frecuency* que entrega la gráfica en el dominio de la frecuencia, *plot_time* entrega la gráfica en el dominio del tiempo, *spectrum* entrega la gráfica del espectrograma en cada segundo de tiempo y *plot_ones* que muestra a lo largo del tiempo los valores que toma el audio; 1 al existir sonido y 0 en su ausencia.

Cada gráficas se despliega por medio de Matplotlib en las distintas ventanas de la aplicación, mostrando en la ventana principal la gráfica en el tiempo y en ventanas secundarias las otras gráficas.


...




##Manual de usuario##

Para utilizar el programa los pasos a seguir son:
* Abrir una terminal en la carpeta que contiene el programa.
![parte 0](http://imgur.com/zRNP1uM)

* Ejecutar el programa con el comando "python3 ventana.py".
![parte 1](http://imgur.com/CFrEEe6)

* Se mostrará una ventana, donde al presionar el primer botón se selecciona el audio que se desea utilizar.
![parte 2]()

* En la ventana principal se muestra la gráfica del audio en función del tiempo y la traducción del mensaje. 
![parte 3](http://imgur.com/SVCRgf2)

* Al presionar el botón 'Show more graphs' se muestra una ventana con las gráficas del audio en función de la frecuencia y el espectograma.
![parte 4]()

* Al presionar el botón 'Show sound graph' se muestra la gráfica del sonido.
![parte 5]()