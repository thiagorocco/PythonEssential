#ELSE: Assim que sai do laço WHILE, o código dentro da instrução ELSE será executado.
#BREAK: Parar o looping
#CONTINUE: Pula para a próxima interação

total=0

for count in range(1000000):
    count += 1
    if(count % 3 == 0 ): continue
    total += count
    
print(total)