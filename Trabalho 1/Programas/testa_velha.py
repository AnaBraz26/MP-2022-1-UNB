import velha

def test_vencedor_X() -> None:
    tabuleiro = [["X","X","X"],
                 ["O","O"," "],
                 [" "," "," "]]
    #Teste da linha com X vencedor
    assert velha.vencedor_X(tabuleiro) == 1

    tabuleiro = [["O","X"," "],
                 ["O","X"," "],
                 [" ","X"," "]]
    #Teste de coluna com X vencedor  
    assert velha.vencedor_X(tabuleiro) == 1

    tabuleiro = [["X"," ","O"],
                 ["O","X","O"],
                 [" ","X","X"]]
    #Teste de diagonal com X vencedor            
    assert velha.vencedor_X(tabuleiro) == 1

def test_vencedor_O() -> None:
    tabuleiro = [["X"," ","X"],
                 ["O","O","O"],
                 [" ","X"," "]]
    #Teste de linha com O vencedor
    assert velha.vencedor_O(tabuleiro) == 2
    
    tabuleiro = [["O"," ","X"],
                 ["O","X"," "],
                 ["O"," ","X"]]
    #Teste de coluna com O vencedor             
    assert velha.vencedor_O(tabuleiro) == 2
    
    tabuleiro = [["X"," ","O"],
                 [" ","O","X"],
                 ["O","X"," "]]
    #Teste de diagonal com O vencedor           
    assert velha.vencedor_O(tabuleiro) == 2


def test_empate() -> None:
    tabuleiro = [["O","X","O"],
                 ["O","X","X"],
                 ["X","O","X"]]
    #Teste de empate
    assert velha.empate(tabuleiro) == 0
    
    tabuleiro = [["O","X","X"],
                 ["X","O","O"],
                 ["O","X","X"]]
    #Teste de empate            
    assert velha.empate(tabuleiro) == 0

    tabuleiro = [["X","X","X"],
                 ["X","O","O"],
                 ["O","O","X"]]
    #Teste de coluna com X vencedor             
    assert velha.empate(tabuleiro) == 1

    tabuleiro = [["X","X","O"],
                 ["X","O","O"],
                 ["O","X","X"]]
    #Teste de diagonal com O vencedor             
    assert velha.empate(tabuleiro) == 2

    tabuleiro = [["O","O","X"],
                 ["X","O","O"],
                 ["O","X","X"]]
    #Teste de empate inválido          
    assert velha.empate(tabuleiro) == -2

def test_indefinido() -> None:
    tabuleiro = [["X"," ","X"],
                 [" ","O"," "],
                 ["X"," ","O"]]
    #Teste de jogo indefinido
    assert velha.indefinido(tabuleiro) == -1
    
    tabuleiro = [[" ","X"," "],
                 [" "," ","O"],
                 [" "," "," "]]
    #Teste de jogo indefinido            
    assert velha.indefinido(tabuleiro) == -1

    tabuleiro = [[" "," "," "],
                 [" "," "," "],
                 [" "," ","X"]]
    #Teste de jogo indefinido             
    assert velha.indefinido(tabuleiro) == -1

def test_invalido() -> None:
    tabuleiro = [[" "," "," "],
                 [" ","O"," "],
                 [" "," "," "]]
    #Teste de jogo invalido
    assert velha.invalido(tabuleiro) == -2
    
    tabuleiro = [[" ","X","X"],
                 [" "," "," "],
                 [" "," "," "]]
    #Teste de jogo invalido            
    assert velha.invalido(tabuleiro) == -2

    tabuleiro = [["X","X","X"],
                 ["X","X","X"],
                 ["X","X","X"]]
    #Teste de jogo invalido             
    assert velha.invalido(tabuleiro) == -2

    tabuleiro = [["O","X","O"],
                 ["O","O","X"],
                 ["X","O","X"]]
    #Teste de jogo invalido             
    assert velha.invalido(tabuleiro) == -2

    
    