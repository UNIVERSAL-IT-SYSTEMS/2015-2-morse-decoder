"""
DICCIONARIO DE LETRAS A MORSE
"""

letter_to_morse = {
	"a" : ".-",		"b" : "-...",	"c" : "-.-.",
	"d" : "-..",	"e" : ".",		"f" : "..-.",
	"g" : "--.",	"h" : "....",	"i" : "..",
	"j" : ".---",	"k" : "-.-",	"l" : ".-..",
	"m" : "--",		"n" : "-.",		"o" : "---",
	"p" : ".--.",	"q" : "--.-",	"r" : ".-.",
	"s" : "...",	"t" : "-",		"u" : "..-",
	"v" : "...-",	"w" : ".--",	"x" : "-..-",
	"y" : "-.--",	"z" : "--..",	"1" : ".----",
	"2" : "..---",	"3" : "...--",	"4" : "....-",
	"5" : ".....", 	"6" : "-....",	"7" : "--...",
	"8" : "---..",	"9" : "----.",	"0" : "-----",	
	" " : "/"
}

morse_to_letter = {morse: letter for letter, morse in letter_to_morse.items()}


"""
DECODIFICA EL MENSAJE
Entrada: string con el mensaje en morse
Salida: string con la traducción
"""
def decode_morse(morse_code):
	return ''.join(morse_to_letter[code] for code in morse_code.split())

"""
CODIFICA EL MENSAJE EN MORSE
Entrada: string con mensaje 
Salida: string con codificación a morse
"""
def encode_morse(text):
	return ' '.join(letter_to_morse[letter] for letter in text)