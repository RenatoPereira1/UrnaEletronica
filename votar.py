import apurar_voto
import confirmacao
import listar_candidatos


def votar_gov():
    var_votogov = input("\nInforme o voto para Governador (ou B para votar em Branco):").upper()
    if var_votogov == "B":  # votar no governador/voto em branco
        print("\nDeseja votar em branco\n")
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_brancoGov += 1
    elif var_votogov == "1":  # opção 1 para governador
        print(f'\nCandidato escolhido: {listar_candidatos.nome_Gov1}')
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_Gov1 += 1
    elif var_votogov == "2":  # opção 2 para governador
        print(f'\nCandidato escolhido: {listar_candidatos.nome_Gov2}')
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_Gov2 += 1
    elif var_votogov == "3":  # opção 3 para governado
        print(f'\nCandidato escolhido: {listar_candidatos.nome_Gov3}')
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_Gov3 += 1
    elif var_votogov == "4":  # opção 4 para governado
        print(f'\nCandidato escolhido: {listar_candidatos.nome_Gov4}')
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_Gov4 += 1
    elif var_votogov == "5":  # opção 5 para governado
        print(f'\nCandidato escolhido: {listar_candidatos.nome_Gov5}')
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_Gov5 += 1
    else:  # Opção de voto Nulo
        print("\nCandidato não encontrado, Deseja anular seu voto?\n")
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_nuloGov += 1
def votar_pres():
    var_votoPres = input("\n\nInforme o voto para Presidente (ou B para votar em Branco):").upper()
    if var_votoPres == "B":  # voto em branco
        print("\nDeseja votar em branco\n")
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_brancoPres += 1
    elif var_votoPres == "1":  # opção 1 para presidente
        print(f'\nCandidato escolhido: {listar_candidatos.nome_Pres1}')
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_Pres1 += 1
    elif var_votoPres == "2":  # opção 2 para presidente
        print(f'\nCandidato escolhido: {listar_candidatos.nome_Pres2}')
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_Pres2 += 1
    elif var_votoPres == "3":  # opção 3 para presidente
        print(f'\nCandidato escolhido: {listar_candidatos.nome_Pres3}')
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_Pres3 += 1
    elif var_votoPres == "4":  # opção 4 para presidente
        print(f'\nCandidato escolhido: {listar_candidatos.nome_Pres4}')
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_Pres4 += 1
    elif var_votoPres == "5":  # opção 5 para presidente
        print(f'\nCandidato escolhido: {listar_candidatos.nome_Pres5}')
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_Pres5 += 1
    else:  # Voto Nulo
        print("\nCandidato não encontrado, Deseja anular seu voto?\n")
        if confirmacao.funcao_confirmacao() == 1:
            apurar_voto.voto_nuloPres += 1
