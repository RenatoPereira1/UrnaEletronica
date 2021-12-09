import os
def limpar_tela(): # função para limpar tela
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


MENU="""  
   ╔══════════ Urna Eletrônica v3.0 ══════════╗
       1: Listar candidatos                     
       2: Iniciar Votação                       
       3: Apurar votos                          
       4: Desligar a urna                       
   ╚══════════════════════════════════════════╝"""


# função para o menu da urna
def menu():
    return input(f"""{MENU}   
    Digite a sua opção:  """)

    


