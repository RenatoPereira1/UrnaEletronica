import listar_candidatos

# função para apuração dos votos opção 3 do menu
def apurar():
    print(f"""


    ╔════════════════════════ Apuração dos votos ════════════════════════╗

     ════════════════════════════ Governador ═══════════════════════════

     Votos do(a) candidato (a) {listar_candidatos.candGov['10']['nome']} : {listar_candidatos.candGov['10'] ['votos']} 
     Votos do(a) candidato (a) {listar_candidatos.candGov['11']['nome']} : {listar_candidatos.candGov['11'] ['votos']}
     Votos do(a) candidato (a) {listar_candidatos.candGov['12']['nome']} : {listar_candidatos.candGov['12'] ['votos']}
     Votos do(a) candidato (a) {listar_candidatos.candGov['13']['nome']} : {listar_candidatos.candGov['13'] ['votos']}
     Votos do(a) candidato (a) {listar_candidatos.candGov['14']['nome']} : {listar_candidatos.candGov['14'] ['votos']}
    
     ═══════════════════════════ Presidente ═══════════════════════════
    
     Votos do(a) candidato (a) {listar_candidatos.candPres['1']['nome']} : {listar_candidatos.candPres['1'] ['votos']}
     Votos do(a) candidato (a) {listar_candidatos.candPres['2']['nome']} : {listar_candidatos.candPres['2'] ['votos']}
     Votos do(a) candidato (a) {listar_candidatos.candPres['3']['nome']} : {listar_candidatos.candPres['3'] ['votos']}
     Votos do(a) candidato (a) {listar_candidatos.candPres['4']['nome']} : {listar_candidatos.candPres['4'] ['votos']}
     Votos do(a) candidato (a) {listar_candidatos.candPres['5']['nome']} : {listar_candidatos.candPres['5'] ['votos']}
    
     ═════════════════════════ Votos Anulados ═════════════════════════
    
     Votos anulados Governador: {listar_candidatos.candGov['16']['nome']} : {listar_candidatos.candGov['16'] ['votos']}
     Votos anulados Presidente: {listar_candidatos.candPres['7']['nome']} : {listar_candidatos.candPres['7'] ['votos']}
    
     ═════════════════════════ Votos em Branco ════════════════════════
    
     Votos em branco Governador: {listar_candidatos.candGov['b']['nome']} : {listar_candidatos.candGov['b'] ['votos']}
     Votos em branco Presidente: {listar_candidatos.candPres['b']['nome']} : {listar_candidatos.candPres['b'] ['votos']}
    
    ╚════════════════════════════════════════════════════════════════════╝""")
