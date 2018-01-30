#!/usr/bin/python3

# Crea un programa que sirva de calculadora y que incluya las funciones 
# basicas (sumar, restar, multiplicar y dividir).

import sys

num_parametros = len(sys.argv)

if num_parametros == 4: # Hay que inluir el propio nombre del script.
	if (sys.argv[1] == "sumar") or (sys.argv[1] == "SUMAR"):
		result = float(sys.argv[2]) + float(sys.argv[3])
		print("\n** SUMAR **")
		print(sys.argv[2], "+", sys.argv[3], "=",  result, "\n")
	
	if (sys.argv[1] == "restar") or (sys.argv[1] == "RESTAR"):
		result = float(sys.argv[2]) - float(sys.argv[3])
		print("\n** RESTAR **")
		print(sys.argv[2], "-", sys.argv[3], "=",  result, "\n")
	
	if (sys.argv[1] == "multiplicar") or (sys.argv[1] == "MULTIPLICAR"):
		result = float(sys.argv[2]) * float(sys.argv[3])
		print("\n** MULTIPLICAR **")
		print(sys.argv[2], "*", sys.argv[3], "=",  result, "\n")
	
	if (sys.argv[1] == "dividir") or (sys.argv[1] == "DIVIDIR"):
		try:
			result = float(sys.argv[2]) / float(sys.argv[3])
			print("\n** DIVIDIR **")
			print(sys.argv[2], "/", sys.argv[3], "=",  result, "\n")
		except ZeroDivisionError:
			print("\nIndefinido\n")
else:
	print("Número de argumentos incorrectos.\n")
