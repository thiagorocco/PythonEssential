import re

while True:
	texto = input("Digite sua string: " )

	minhaRegex = re.compile(r'Funk')
	minhaRegex = minhaRegex.sub('Heavy Metal', texto)
	
	print(minhaRegex)

	
