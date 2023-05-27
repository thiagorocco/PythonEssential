import re

while True:
    email = input('Informe seu e-mail: ')
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+		# nome do usuário
        @				# arroba
        [a-zA-Z0-9.-]+    	# domínio
        (\.[a-zA-Z]{2,4})   	# ponto seguido de outros caracteres
        )''', re.VERBOSE)

    emailRegex = emailRegex.search(email)

    if emailRegex != None:
        print(emailRegex.group())
        break
    else:
        print('Informe um e-mail no formato válido(e-mail@email.com')