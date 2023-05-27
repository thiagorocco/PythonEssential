'''
    Método re.VERBOSE
'''
import re

while True:
	texto = input("Digite sua string: " )

	minhaRegex = re.compile(r'''(
			(\d{2}|\(\d{2}\))?		# código de área
			(\s*)?				# espaço
			(\d{4})				# primeiros 3 dígitos
			(\s*|.*)			# separador
			(\d{4})				# últimos 4 dígitos
			)''', re.VERBOSE)
	minhaRegex = minhaRegex.search(texto)
	
	print(minhaRegex.group())
	
