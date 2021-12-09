from confirmacao import funcao_confirmacao
import listar_candidatos



def eleicao():
    funcao1 = 0
    while funcao1 != 1:
        votoGov = input(f"""Informe o voto para Governador (ou B para votar em Branco):""")
        if votoGov in listar_candidatos.candGov:
            print(f"""Candidato escolhido: {listar_candidatos.candGov[votoGov]['nome']}""")
            if funcao_confirmacao() == 1:
                listar_candidatos.candGov[votoGov]['votos'] += 1
                funcao1 +=1
        else:
            print(f"""Opção não encontrada deseja {listar_candidatos.candGov['16']['nome']}""")
            if funcao_confirmacao() == 1:
                listar_candidatos.candGov['16']['votos'] += 1
                funcao1 += 1

    funcao2 = 0
    while funcao2 !=1:
        votoPres = input(f"""Informe o voto para Presidente (ou B para votar em Branco):""")
        if votoPres in listar_candidatos.candPres:
            print(f"""Candidato escolhido: {listar_candidatos.candPres[votoPres]['nome']}""")
            if funcao_confirmacao() == 1:
                listar_candidatos.candPres[votoPres]['votos'] += 1
                funcao2 += 1
        else:
            print(f""" Opção não encontrada deseja {listar_candidatos.candPres['7']['nome']}""")
            if funcao_confirmacao() == 1:
                listar_candidatos.candPres['16']['votos'] += 1
                funcao2 += 1



