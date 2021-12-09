# opções válidas para o governador
candGov = {
        '10':{
                'nome':'Will Smith Ragatanga',
                'votos':0,
        },
        '11':{
                'nome':'Bruce Batman da Silva',
                'votos':0,
        },
        '12':{
                'nome':'Tony Stark Carvalho Pereira',
                'votos': 0,
        },
        '13':{
                'nome':'Wesley Safadão',
                'votos':0,
        },
        '14':{
                'nome':'Chimbinha da Joelma Ferreira',
                'votos':0,
        },
        'b':{
                'nome':'Votar em Branco',
                'votos':0,
        },
        '16':{
                'nome':'Votar nulo',
                'votos':0,
        },
}

# opções válidas para o presidente
candPres = {
        '1':{
                'nome':'Albert Einstein',
                'votos':0,
        },
        '2':{
                'nome':'Isaac Newton',
                'votos':0,
        },
        '3':{
                'nome':'Stephen Hawking',
                'votos':0,
        },
        '4':{
                'nome':'Bill Gates',
                'votos':0,
        },
        '5':{
                'nome':'Steve Jobs',
                'votos':0,
        },
        'b':{
                'nome':'Votar em Branco',
                'votos':0,
        },
        '7':{
                'nome':'Votar nulo',
                'votos':0,
        },

}



def listar(): # fução para listar os candidatos opção 1 do menu
    print(f"""
    ╔════════════Lista de candidatos════════════╗
     ═══════════════ Governador ══════════════ 
      Candidato (a) 10: {candGov['10']['nome']}
      Candidato (a) 11: {candGov['11']['nome']} 
      Candidato (a) 12: {candGov['12']['nome']} 
      Candidato (a) 13: {candGov['13']['nome']} 
      Candidato (a) 14: {candGov['14']['nome']} 
      ═══════════════ Presidente ═══════════════  
      Candidato (a) 1: {candPres['1']['nome']}
      Candidato (a) 2: {candPres['2']['nome']} 
      Candidato (a) 3: {candPres['3']['nome']} 
      Candidato (a) 4: {candPres['4']['nome']} 
      Candidato (a) 5: {candPres['5']['nome']}
    ╚═════════════════════════════════════════════╝                     
""")



