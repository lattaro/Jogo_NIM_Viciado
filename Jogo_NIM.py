pc = 0
p = 0

def campeonato():
    
    print("**** Rodada 1 ****")
    partida()
    print("**** Rodada 2 ****")
    partida()
    print("**** Rodada 3 ****")
    partida()
    print("**** Final do campeonato! ****")
    print("Placar: Você ",p,"X",pc," Computador")

def solo_ou_campeonato():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    x = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
    if x == 1:
        partida()
    else:
        campeonato()

def partida():
    n = int(input("Quanta peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n < m:
        print("Oops! Jogada inválida! A quantidade de peças precisa ser maior que o limite de peças por jogada")
        n = int(input("Quanta peças? "))
        m = int(input("Limite de peças por jogada? "))

    if n % (m+1) == 0:
            print("Voce começa!")
            usuario_escolhe_jogada(n,m)
    else:
        print("Computador começa!")
        computador_escolhe_jogada(n,m)
        
    
def usuario_escolhe_jogada(n,m):
        peca_usuario = int(input("Quantas peças você vai tirar? "))
        if peca_usuario > m:
            print("Oops! Jogada inválida! Tente de novo.")
            usuario_escolhe_jogada(n,m)
        else:
            n = n - peca_usuario
            if peca_usuario > 1:
                print("Você tirou",peca_usuario,"peças")
                if n > 1:
                    print("Agora restam apenas",n, "peças no tabuleiro.")
                    computador_escolhe_jogada(n,m)
                else:
                    print("Agora resta apenas uma peça no tabuleiro.")
                    computador_escolhe_jogada(n,m)
               

            if peca_usuario == 1:
                print("Você tirou uma peça")  
                if n > 1:
                    print("Agora restam apenas",n, "peças no tabuleiro.")
                    computador_escolhe_jogada(n,m)
                else:
                    print("Agora resta apenas uma peça no tabuleiro.")
                    computador_escolhe_jogada(n,m)  

def computador_escolhe_jogada(n,m): 
    peca_computador = 1
    while (peca_computador <= m):
        if (n - peca_computador) % (m+1) != 0:
            peca_computador = peca_computador + 1
        else:
            if (n - peca_computador) % (m+1) == 0:
                n = n - peca_computador
                if n == 0:
                    global pc
                    pc = pc + 1
                    print("O computador tirou",peca_computador, "peça")
                    print("Fim do jogo! O computador ganhou!")
                                
                else:
                    print("O computador tirou",peca_computador, "peça")
                    print("Agora resta",n,"no tabuleiro.")
                    usuario_escolhe_jogada(n,m)  
                      
solo_ou_campeonato()




