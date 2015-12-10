# Morse-Decoder
**Decodificador de código morse a partir de audio de transmisiones satelitales**

Integrantes:
* Nicole Macarena Henríquez Sepúlveda
* Katherine Marcela Liberona Irarrazabal
* Maximiliano Felipe Andrés Pérez Rodríguez

##Bibliotecas y paquetes utilizados

La mayoría de los paquetes y librerias de python son instaladas fácilmente mediante *pip*, que es un gestor de paquetes proporcionados por python.

[**Scipy:**](http://www.scipy.org/) Biblioteca de código abierto, enfocada principalmente en el área matemática, ciencias e ingeniería. Permite utilizar funciones que cumplen el mismo objetivo que las de *Matlab*, pero en *Python*. El uso de esta biblioteca en el programa es a tráves de la función *FFT*, la cual permite calcular la transformada de Fourier de los datos obtenidos de un audio, dichos datos también son obtenidos usando *Scipy*.

[**Numpy:**](http://www.numpy.org/) Biblioteca de funciones que permite trabajar tanto con vectores como con matrices, a través de funciones matemáticas de alto nivel. Las matrices que representan los audios con los que se trabaja en este programa son matrices del tipo *numpy*, lo que conlleva a que puedan ser trabajadas matemáticamente de forma más sencilla. 

[**Tkinter:**](https://wiki.python.org/moin/TkInter) Es una adaptación de la biblioteca *Tlc/tk* para su utilización en *Python*. Permite tener un estándar para la interfaz gráfica de usuario. Se entiende que los botones y las ventanas del programa serán creadas a partir de esta biblioteca.

[**Matplotlib:**](http://matplotlib.org/) Esta biblioteca permite la generación de gráficos, obtenidos a partir de los datos de *arrays* o listas. Los espectros, tanto en el dominio del tiempo como de la frecuencia, serán presentandos usando los gráficos que entrega *Matplotlib*.

![Gráfico](http://i.imgur.com/Fa0z1XM.png)

##Funcionalidad

El programa actual creado está basado, principalmente, en uno encontrado en internet creado por [haskell](https://sites.google.com/site/haskell102/home/frequency-analysis-of-audio-file-with-python-numpy-scipy). Este programa tuvo que ser estudiado y modificado para que sea capaz de trabajar frente a cualquier formato de audio del tipo punto wav.

Con la ayuda de Tkinter, al correr el programa, se despliega una ventana con un botón. Al presionarlo se abre el 'gestor de archivos' que permite seleccionar el audio con extensión wav. Con los datos del audio a analizar se hace el llamado a la función plotTiempo, la cual retorna la gráfica de la señal en el dominio del tiempo.
Luego se realiza el llamado de la función plotFrecuencia, la cual recibe la información de la señal y retorna la gráfica en el dominio de la frecuencia.

Ambas gráficas obtenidas por medio de Matplotlib se muestran en una nueva ventana, donde además puede ser descargada.
