def menu(cadastros):
    opc = 0
    while opc != 6:
        print("==== GERENCIAMENTO DE PONTOS TURISTICOS ====")
        print("1- Cadastrar Ponto Turistico")
        print("2- Alterar Ponto Turistico")
        print("3- Remover Ponto Turistico")
        print("4- Listar um Ponto Turistico")
        print("5- Listar todos os Pontos Turisticos")
        print("6- Sair")
        print("============================================")
        opc = int(input("Escolha uma opcao: "))
        if opc < 1 or opc > 6:
            print("OPCAO INVALIDA!")
        else:
            if opc == 1:
                incluir(cadastros)
            elif opc == 2:
                alterar(cadastros)
            elif opc == 3:
                remover(cadastros)
            elif opc == 4:
                listar_um(cadastros)
            elif opc == 5:
                listar_todos(cadastros)
    grava_cadastro(cadastros)

def incluir(cadastros):
    nome = input("Nome do Ponto Turistico: ")
    if not existe_ponto(cadastros, nome):
        endereco = input("Endereco: ")
        print("Dias de funcionamento: ")
        dias = []
        dia = input()
        while dia != "":
            dias.append(dia)
            dia = input()
        hora_abre = input("Horario de abertura: ")
        hora_fecha = input("Horario de fechamento: ")
        preco = float(input("Preco de entrada: "))
        cadastros[1].append([nome,endereco,dias,hora_abre,hora_fecha,preco])
    else:
        print("PONTO TURISTICO JA CADASTRADO!")

def alterar(cadastros):
    nome = input("Nome do Ponto Turistico: ")
    if not existe_ponto(cadastros, nome):
        print("PONTO TURISTICO NAO CADASTRADO!")
    else:
        pontosTur = cadastros[1]
        for ponto in pontosTur:
            if ponto[0] == nome:   
                print("== QUAL ITEM DESEJA ALTERAR? ==")
                print("1- Nome")
                print("2- Endereco")
                print("3- Dias de funcionamento")
                print("4- Horario de abertura")
                print("5- Horario de fechamento")
                print("6- Preco de entrada")
                print("===============================")
                item = int(input("Escolha uma opcao: "))
                if item == 1:
                    nome = input("Nome: ")
                    ponto[0] = nome
                elif item == 2:
                    endereco = input("Endereco: ")
                    ponto[1] = endereco
                elif item == 3:
                    print("Dias de funcionamento: ")
                    dias = []
                    dia = input()
                    while dia != "":
                        dias.append(dia)
                        dia = input()
                    ponto[2] = dias
                elif item == 4:
                    hora_abre = input("Horario de abertura: ")
                    ponto[3] = hora_abre
                elif item == 5:
                    hora_fecha = input("Horario de fechamento: ")
                    ponto[4] = hora_fecha
                elif item == 6:
                    preco = float(input("Preco de entrada: "))
                    ponto[5] = preco
                else:
                    print("OPCAO INVALIDA!")

def remover(cadastros):
    nome = input("Qual Ponto Turistico deseja remover: ")
    if not existe_ponto(cadastros, nome):
        print("PONTO TURISTICO NAO CADASTRADO!")
    else:
        pontosTur = cadastros[1]
        for ponto in pontosTur:
            if ponto[0] == nome:
                pontosTur.remove(ponto)
                print("Ponto Turistico Removido com sucesso!")
                
def listar_um(cadastros):
    nome = input("Qual ponto Turistico deseja listar: ")
    if not existe_ponto(cadastros, nome):
        print("PONTO TURISTICO NAO CADASTRADO!")
    else:
        pontosTur = cadastros[1]
        for p in pontosTur:
            if p[0] == nome:
                ponto = p
                print(f"===== {cadastros[0].upper()} =====")
                print(f"Ponto Turistico: {ponto[0].title()}")
                print(f"Endereco: {ponto[1].title()}")
                dias = ", ".join(ponto[2])
                print(f"Dias de funcionamento: {dias}")
                print(f"Horario de abertura: {ponto[3]}")
                print(f"Horario de fechamento: {ponto[4]}")
                print(f"Valor de entrada: {ponto[5]}")

def listar_todos(cadastros):
    print(f"===== {cadastros[0].upper()} =====")
    pontosTur = cadastros[1]
    for p in pontosTur:
        ponto = p
        print(f"Ponto Turistico: {ponto[0].title()}")
        print(f"Endereco: {ponto[1].title()}")
        dias = ", ".join(ponto[2])
        print(f"Dias de funcionamento: {dias}")
        print(f"Horario de abertura: {ponto[3]}")
        print(f"Horario de fechamento: {ponto[4]}")
        print(f"Valor de entrada: {ponto[5]}")
        print("============================")

def existe_ponto(cadastros, nome):
    pontosTur = cadastros[1]
    for ponto in pontosTur:
        if ponto[0] == nome:
            return True
    return False

def grava_cadastro(cadastros):
    print("Gravando Registros de Pontos Turisticos...")
    arq = open("PontosTur.txt","w")
    cidade = cadastros[0]+"\n"
    arq.write(cidade)
    pontosTur = cadastros[1]
    for ponto in pontosTur:
        dias ="#".join(ponto[2])
        linha = ponto[0]+"\t"+ponto[1]+"\t"+dias+"\t"+ponto[3]+"\t"+ponto[4]+"\t"+str(ponto[5])+"\n"
        arq.write(linha)
    arq.close()

def recupera_cadastro(cadastros):
    print("Recuperando registros de Pontos Turisticos...")
    cadastros.append("Nome Indefinido")
    cadastros.append([])
    arq = open("PontosTur.txt","r")
    linha = arq.readline()
    cadastros[0] = linha[:len(linha)-1]
    for linha in arq:
        linha = linha[:len(linha)-1]
        ponto =  linha.split("\t")
        ponto[2] = ponto[2].split("#")
        ponto[5] = float(ponto[5])      
        cadastros[1].append(ponto)
    arq.close()
