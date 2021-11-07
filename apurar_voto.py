import listar_candidatos
# apuração dos votos do presidente
voto_Pres1 = 0
voto_Pres2 = 0
voto_Pres3 = 0
voto_Pres4 = 0
voto_Pres5 = 0

# apuração dos votos do governador
voto_Gov1 = 0
voto_Gov2 = 0
voto_Gov3 = 0
voto_Gov4 = 0
voto_Gov5 = 0

# apurar os votos nulos/brancos
voto_nuloGov = 0
voto_brancoGov = 0
voto_nuloPres = 0
voto_brancoPres = 0


# função para apuração dos votos opção 3 do menu
def apurar():
    print(f"""


    ╔════════════════════════ Apuração dos votos ════════════════════════╗

     ════════════════════════════ Governador ═══════════════════════════

     Votos do(a) candidato (a) {listar_candidatos.nome_Gov1}: {voto_Gov1}
     Votos do(a) candidato (a) {listar_candidatos.nome_Gov2}: {voto_Gov2}
     Votos do(a) candidato (a) {listar_candidatos.nome_Gov3}: {voto_Gov3}
     Votos do(a) candidato (a) {listar_candidatos.nome_Gov4}: {voto_Gov4}
     Votos do(a) candidato (a) {listar_candidatos.nome_Gov5}: {voto_Gov5}
    \n
     ═══════════════════════════ Presidente ═══════════════════════════
    \n
     Votos do(a) candidato (a) {listar_candidatos.nome_Pres1}: {voto_Pres1}
     Votos do(a) candidato (a) {listar_candidatos.nome_Pres2}: {voto_Pres2}
     Votos do(a) candidato (a) {listar_candidatos.nome_Pres3}: {voto_Pres3}
     Votos do(a) candidato (a) {listar_candidatos.nome_Pres4}: {voto_Pres4}
     Votos do(a) candidato (a) {listar_candidatos.nome_Pres5}: {voto_Pres5}
    \n
     ═════════════════════════ Votos Anulados ═════════════════════════
    \n
     Votos anulados Governador: {voto_nuloGov}
     Votos anulados Presidente: {voto_nuloPres}
    \n
     ═════════════════════════ Votos em Branco ════════════════════════
    \n
     Votos em branco Governador: {voto_brancoGov}
     Votos em branco Presidente: {voto_brancoPres}
    \n
    ╚════════════════════════════════════════════════════════════════════╝\n""")
