import menu
import apurar_voto
import listar_candidatos
import votar

var_opcao = 0 #variavel que armazena as opções da urna

while var_opcao != 4: # estrutura de repetição da urna, parar ao digitar a opção 4

    menu.limpar_tela() # chamar a função para limpar a tela para ficr mais apresentavel

    menu.menu() #chamar a função do menu

    var_opcao = menu.OpMenu() # chamar a função do input de opção

    menu.limpar_tela()
    if var_opcao == 1:  # opção 1 do menu listar os candidatos
        listar_candidatos.listar() # chamar função da lista de candidatos
        input("Aperte Enter para voltar ao menu")

    elif var_opcao == 2:  # opção 2 do menu votação
        votar.votar_gov()
        votar.votar_pres()
        print("\n\n")
        input("Fim da votação !!!\n\nPrecione Enter para voltar ao menu")

    elif var_opcao == 3:  # opção 3 da urna, apuração de votos
        apurar_voto.apurar()
        input("Aperte Enter para voltar ao menu")

    elif var_opcao == 4:  # opção de saida e shutdown da urna
        print("\nObrigado por utilizar a Urna Eletrônica!\n")

    else:
        # opção invalida no menu
        print("\nOpção inválida!\nDigite uma opção válida.")
        input("Aperte Enter para voltar ao menu")
