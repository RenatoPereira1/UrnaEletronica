import os
def limpar_tela(): # função para limpar tela
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def menu(): # função para o menu da urna
    MENU="""  
   ╔══════════ Urna Eletrônica v3.0 ══════════╗
       1: Listar candidatos                     
       2: Iniciar Votação                       
       3: Apurar votos                          
       4: Desligar a urna                       
   ╚══════════════════════════════════════════╝"""
    print(MENU)
    
def OpMenu(): # função para opções da urna
    return(int(input("Digite a sua opção: ")))  