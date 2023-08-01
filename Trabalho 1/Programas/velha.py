#Função para verificar se o ganhador é o jogador X
def vencedor_X(tabuleiro): 
    marcador_X = 0  #Marca quantas vezes o X apareceu no jogo
    marcador_O = 0  #Marca quantas vezes o O apareceu no jogo

    #Para acontecer um empate é necessário que o X apareça 5 vezes e o O apareça 4 vezes
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == "X":
                marcador_X = marcador_X + 1
            elif tabuleiro[linha][coluna] == "O":
                marcador_O = marcador_O + 1

    #Caso a diferença entre X e O for maior que um quer dizer que houve uma jogada repetida de X 
    #(Jogo inválido)
    if(marcador_X > 0 and (marcador_X - marcador_O > 1)):
        return -2

    #Caso a quantidade O e for maior que a quantidade de X quer dizer que houve uma jogada repetida de O
    #(Jogo Invélido)
    if(marcador_X > 0 and ( marcador_O > marcador_X)):
        return -2
        
    for linha in range(3):
        #Verifica as Linhas do jogo
        if (tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == "X"):
            return 1    #Se fechar alguma linha com X, ele é o ganhador e sai 1

    for coluna in range(3):
        #Verifica as Colunas do jogo
        if (tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == "X"):
            return 1

    #Verifica as diagonais do jogo
    if((tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "X") or 
       (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "X")):
        return 1

#Função para verificar se o ganhador é o jogador Y
def vencedor_O(tabuleiro): 
    marcador_X = 0  #Marca quantas vezes o X apareceu no jogo
    marcador_O = 0  #Marca quantas vezes o O apareceu no jogo

    #Para acontecer um empate é necessário que o X apareça 5 vezes e o O apareça 4 vezes
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == "X":
                marcador_X = marcador_X + 1
            elif tabuleiro[linha][coluna] == "O":
                marcador_O = marcador_O + 1

    #Caso a diferença entre X e O for maior que um quer dizer que houve uma jogada repetida de X 
    #(Jogo inválido)
    if(marcador_X > 0 and (marcador_X - marcador_O > 1)):
        return -2

    #Caso a quantidade O e for maior que a quantidade de X quer dizer que houve uma jogada repetida de O
    #(Jogo Invélido)
    if(marcador_X > 0 and ( marcador_O > marcador_X)):
        return -2

    for linha in range(3):
        #Verifica as Linhas do jogo
        if (tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == "O"):
            return 2   

    for coluna in range(3):
        #Verifica as Colunas do jogo
        if (tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == "O"):
            return 2

    #Verifica as diagonais do jogo
    if((tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "O") or (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "O")):
        return 2

#Função para verificar se houve empate
def empate(tabuleiro): 
    marcador_X = 0  #Marca quantas vezes o X apareceu no jogo
    marcador_O = 0  #Marca quantas vezes o O apareceu no jogo

    #Para acontecer um empate é necessário que o X apareça 5 vezes e o O apareça 4 vezes
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == "X":
                marcador_X = marcador_X + 1
            elif tabuleiro[linha][coluna] == "O":
                marcador_O = marcador_O + 1

    #Caso a diferença entre X e O for maior que um quer dizer que houve uma jogada repetida de X 
    #(Jogo inválido)
    if(marcador_X > 0 and (marcador_X - marcador_O > 1)):
        return -2

    #Caso a quantidade O e for maior que a quantidade de X quer dizer que houve uma jogada repetida de O
    #(Jogo Invélido)
    if(marcador_X > 0 and ( marcador_O > marcador_X)):
        return -2

    #Além disso é necessário verificar dentre esse marcadores não houve um vencedor, o que pode ocorrer..
    for linha in range(3):
        #Verifica as Linhas do jogo
        if (tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == "O"):
            return 2
        elif(tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == "X"):
            return 1

    for coluna in range(3):
        #Verifica as Colunas do jogo
        if (tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == "O"):
            return 2
        elif(tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == "X"):
            return 1

    #Verifica as diagonais 
    if((tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "O") or (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "O")):
        return 2 
    elif((tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == "X") or (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == "X")):
        return 1
    
    #Caso isso ocorra haverá um empate no jogo
    if(marcador_X == 5 and marcador_O == 4):
        return 0

#Função para verificar se o jogo está indefinido
def indefinido(tabuleiro):
    marcador_X = 0
    marcador_O = 0

    #Verifica a quantidade de X e O no jogo
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == "X":
                marcador_X = marcador_X + 1
            elif tabuleiro[linha][coluna] == "O":
                marcador_O = marcador_O + 1

    #Caso o jogo comece com O
    #(jogo inválido)
    if(marcador_X == 0 and marcador_O > 0):
        return -2
    
    #Caso a diferença entre X e O for maior que um quer dizer que houve uma jogada repetida de X 
    #(jogo inválido)
    if(marcador_X > 0 and (marcador_X - marcador_O > 1)):
        return -2

    #Caso a quantidade O e for maior que a quantidade de X quer dizer que houve uma jogada repetida de O 
    #(jogo inválido)
    if(marcador_X > 0 and ( marcador_O > marcador_X)):
        return -2

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                return -1

#Função para verificar se o jogo está inválido
def invalido(tabuleiro):
    marcador_X = 0
    marcador_O = 0

    #Verifica a quantidade de X e O no jogo
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == "X":
                marcador_X = marcador_X + 1
            elif tabuleiro[linha][coluna] == "O":
                marcador_O = marcador_O + 1

    #Caso o jogo comece com O
    if(marcador_X == 0 and marcador_O > 0):
        return -2
    
    #Caso a diferença entre X e O for maior que um quer dizer que houve uma jogada repetida de X 
    if(marcador_X > 0 and (marcador_X - marcador_O > 1)):
        return -2

    #Caso a quantidade O e for maior que a quantidade de X quer dizer que houve uma jogada repetida de O 
    if(marcador_X > 0 and ( marcador_O > marcador_X)):
        return -2
    

