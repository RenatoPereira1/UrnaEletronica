
def funcao_confirmacao(): # função para conirmação de voto 1 para sim 2 para não e 3 para outra opção
    var_confirmar = input("Confirma o voto? (s ou n): ").lower()
    if var_confirmar == "s":
        print("\nVoto Registrado")
        return 1
    elif var_confirmar == "n":
        return 2
    else:
        print("\nOpção inválida! ")
        return 3