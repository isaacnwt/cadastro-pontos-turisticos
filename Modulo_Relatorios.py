def menu(pontosTur,visitantes,visitas):
    opc = 0
    while opc != 5:
        print("=============================== RELATORIOS ===============================")
        print("1- Consultar Ponto Turistico")
        print("2- Consultar Visitante")
        print("3- Consultar Pontos a partir do Preco de Entrada")
        print("4- Consultar Pontos a partir do Dia e Horario de Funcionamento")
        print("5- Sair")
        print("===========================================================================")
        opc = int(input("Escolha uma opcao: "))
        if opc < 1 or opc > 5:
            print("OPCAO INVALIDA!")
        else:
            if opc == 1:
                consulta_ponto(pontosTur,visitantes,visitas)
            elif opc == 2:
                consulta_visitante(pontosTur,visitantes,visitas)
            elif opc == 3:
                cosulta_preco(pontosTur,visitantes,visitas)
            elif opc == 4:
                consulta_dia(pontosTur,visitantes,visitas)
                
def consulta_ponto(pontosTur,visitantes,visitas):
    nome = input("Nome: ")
    if existe_ponto(pontosTur, nome):
        pontos = pontosTur[1]
        for ponto in pontos:
            if nome == ponto[0]:
                print(f"===== {ponto[0].upper()} =====")
                print(f"Endereco: {ponto[1].title()}")
                dias = ", ".join(ponto[2])
                print(f"Dias de funcionamento: {dias}")
                print(f"Horario de abertura: {ponto[3]}")
                print(f"Horario de fechamento: {ponto[4]}")
                print(f"Valor de entrada: {ponto[5]}")
                print("=========================")
                print("VISITANTES:")
        existe = False
        for visita in visitas:
            if nome == visita[1]:
                existe = True
                for cpf in visitantes:
                    if cpf == visita[0]:
                        print(visitantes[cpf][0])
        if existe == False:
            print("NENHUMA VISITA REGISTADA!")
    else:
        print("PONTO TURISTICO NAO CADASTRADO!")
        
def consulta_visitante(pontosTur,visitantes,visitas):
    nome = input("Nome: ")
    cad = False
    for cpf in visitantes:
        if nome.lower() in visitantes[cpf][0].lower():
            cad = True
            print(f"=== {visitantes[cpf][0].upper()} ===")
            print("CPF: ", cpf)
            print("Data de Nascimento: ", visitantes[cpf][1])
            print("Cidade: ", visitantes[cpf][2].title())
            print("Profissao: ", visitantes[cpf][3].title())
            print("E-mail: " , visitantes[cpf][4])
            print("Telefone(s): ", ', '.join(map(str,visitantes[cpf][5])))
            print("PONTOS VISITADOS:")
            existe = False
            for visita in visitas:
                if cpf == visita[0]:
                    existe = True
                    print(visita[1])
            if existe == False:
                print("NENHUMA VISITA REGISTRADA!")
    if cad == False:
        print("VISITANTE NAO CADASTRADO!")
    
def cosulta_preco(pontosTur,visitantes,visitas):
    valor = float(input("Valor Maximo: "))
    cad = False
    pontos = pontosTur[1]
    for ponto in pontos:
        if ponto[5] < valor:
            cad = True
            print(f"===== {ponto[0].upper()} =====")
            print(f"Endereco: {ponto[1].title()}")
            dias = ", ".join(ponto[2])
            print(f"Dias de funcionamento: {dias}")
            print(f"Horario de abertura: {ponto[3]}")
            print(f"Horario de fechamento: {ponto[4]}")
            print(f"Valor de entrada: {ponto[5]}")
            print("=========================")
            print("VISITANTES:")
            nome = ponto[0]
            existe = False
            for visita in visitas:
                if nome == visita[1]:
                    existe = True
                    for cpf in visitantes:
                        if cpf == visita[0]:
                            print(visitantes[cpf][0])
            if existe == False:
                print("NENHUMA VISITA REGISTADA!")
    if cad == False:
        print("NAO HA PONTO COM ESSE VALOR!")
        
def consulta_dia(pontosTur,visitantes,visitas):
    dia = input("Dia de funcionamento: ")
    hora = input("Horario de funcionamento: ")
    hora = float(hora.replace("h","."))
    cad = False
    pontos = pontosTur[1]
    for ponto in pontos:
        entrada = float(ponto[3].replace("h","."))
        saida = float(ponto[4].replace("h","."))
        dias = ponto[2]
        if dia in dias:
            if hora >= entrada and hora <= saida:
                cad = True
                print(f"===== {ponto[0].upper()} =====")
                print(f"Endereco: {ponto[1].title()}")
                dias = ", ".join(ponto[2])
                print(f"Dias de funcionamento: {dias}")
                print(f"Horario de abertura: {ponto[3]}")
                print(f"Horario de fechamento: {ponto[4]}")
                print(f"Valor de entrada: {ponto[5]}")
                print("=========================")
                print("VISITANTES:")
                nome = ponto[0]
                existe = False
                for visita in visitas:
                    if nome == visita[1]:
                        existe = True
                        for cpf in visitantes:
                            if cpf == visita[0]:
                                print(visitantes[cpf][0])
                if existe == False:
                    print("NENHUMA VISITA REGISTADA!")
    if cad == False:
        print("NAO HA PONTO FUNCIONANDO NESSE MOMENTO!")
    
def existe_ponto(cadastros, nome):
    pontosTur = cadastros[1]
    for ponto in pontosTur:
        if ponto[0] == nome:
            return True
    return False

