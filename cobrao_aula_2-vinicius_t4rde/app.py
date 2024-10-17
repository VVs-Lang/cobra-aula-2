import random 

# Função que gera a introdução da história
def gerar_introducao():
    introducoes = ["Era uma vez", "Há muito tempo atrás", "Num reino distante"] 
    return random.choice(introducoes)

# Função que gera o desnvolvimento da história
def gerar_desenvolvimento():
    desenvolvimento = ["Um valente cavaleiro" , "Uma destemida guerreira" , "Um bravo guerreiro" , "Uma poderosa feiticeira", "Um sábio mago"]
    return random.choice(desenvolvimento)

# Função que gera o final da história
def gera_final():
    finais = ["enfrentando dragoes feroses." , "derrotando um terrível vilão." , "descobrindo um tesouro escondido." , "salvando o reino da escuridao." , "encontrando um amor verdadeiro."]
    return random.choice(finais) 

# Funçaõ principal que gera toda a história
def gerar_historia():
   introducao = gerar_introducao()
   desenvolvimento = gerar_desenvolvimento()
   final = gera_final()

   historia = f" {introducao} {desenvolvimento} {final}"
   return historia

#Exibe a historia gerada
if __name__ ==  "__main__":
    print(gerar_historia())