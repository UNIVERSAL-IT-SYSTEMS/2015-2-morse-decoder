# Morse-Decoder
**Decodificador de código morse a partir de audio de transmisiones satelitales**
Integrantes:
* Nicole Macarena Henríquez Sepúlveda
* Katherine Marcela Liberona Irarrazabal
* Maximiliano Felipe Andrés Pérez Rodríguez

##Bibliotecas y paquetes utilizados

La mayoría de los paquetes y librerias de python son instaladas fácilmente por *pip* que es un gestor de paquetes proporcionados por python.

**Scipy:** Biblioteca de codigo abierto, enfocada principalmente en el área matemática, ciencias e ingeniería. Permite utilizar funciones que cumplen el mismo objetivo que las de *Matlab*, pero en *Python*. El uso de esta biblioteca en el programa es a tráves de la función *FFT*, la cual permite calcular la transformada de Fourier de los datos obtenidos de un audio, dichos datos tanbien son obtenidos usando *Scipy*.

**Numpy:** Biblioteca de funciones que permite trabajar tanto con vectores como con matrices, a través de funciones matemáticas de alto nivel. Las matrices que representan los audios con los que se trabaja en este programa son matrices del tipo *numpy*, lo que conlleva a que puedan ser trabajadas matemáticamente de forma más sencilla. 

**Tkinter:** Es una adaptación de la biblioteca *Tlc/tk* para su utilización en *Python*. Permite tener un estándar para la interfaz gráfica de usuario. Se entiende que los botones y las ventanas del programa seran creadas a partir de esta biblioteca.

**Matplotlib:** Esta biblioteca permite la generación de gráficos, obtenidos a partir de los datos de *arrays* o listas. Los espectros tanto en el dominio del tiempo como de la frecuencia, seran presentandos usando los gráficos que entrega *Matplotlib*.

![Gráfico](http://i.imgur.com/Fa0z1XM.png)

