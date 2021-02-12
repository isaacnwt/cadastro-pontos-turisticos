import Modulo_PontosTur

def menu(pontosTur,visitantes,cadastros):
    opc = 0
    while opc != 6:
        print("===== GERENCIAMENTO DE VISITAS =====")
        print("1- Cadastrar Visita")
        print("2- Alterar Visita")
        print("3- Remover Visita")
        print("4- Listar uma Visita")
        print("5- Listar todas as Visitas")
        print("6- Sair")
        print("====================================")
        opc = int(input("Escolha uma opcao: "))
        if opc < 1 or opc > 6:
            print("OPCAO INVALIDA!")
        else:
            if opc == 1:
                cadastrar(pontosTur,visitantes,cadastros) 
            elif opc == 2:
                alterar(cadastros)
            elif opc == 3:
                remover(cadastros)
            elif opc == 4:
                listar(cadastros)
            elif opc == 5:
                listarTodos(cadastros)
    grava_cadastro(cadastros)
    
def cadastrar(pontosTur,visitantes,cadastros):
    cpf = input("CPF do Visitante: ")
    nome = input("Ponto Turistico: ")
    if cpf not in visitantes:
        print("VISITANTE NAO CADASTRADO")
    elif not Modulo_PontosTur.existe_ponto(pontosTur,nome):
        print("PONTO TURISTICO NAO CADASTRADO!")
    else:
        pontos = pontosTur[1]
        for ponto in pontos:
            if nome == ponto[0]:
                dias = ", ".join(ponto[2])
                print(f"DIAS DE FUNCIONAMENTO: {dias}")
                print(f"HORARIO DE ABERTURA: {ponto[3]}")
                print(f"HORARIO DE FECHAMENTO: {ponto[4]}")
        data = input("Data da Visita: ")
        dia = input("Dia da Semana: ")
        entrada = input("Hora de Entrada: ")
        saida = input("Hora de Saida: ")
        #busca o preco cadastrado no Ponto Turistico
        pontos = pontosTur[1]
        for ponto in pontos:
            if nome == ponto[0]:
                preco = ponto[5]
                print(f"Preco do Ingresso: {preco}")
        cadastros[(cpf,nome)] = [data,dia,entrada,saida,preco]

def alterar(cadastros):
    cpf = input("CPF do Visitante: ")
    nome = input("Ponto Turistico: ")
    if (cpf,nome) not in cadastros:
        print("VISITA NAO CADASTRADA!")
    else:
        print("== QUAL ITEM DESEJA ALTERAR? ==")
        print("1- Alterar Data da Visita")
        print("2- Alterar Dia da Semana")
        print("3- Alterar Hora de Entrada")
        print("4- Alterar Hora de Saida")
        print("===============================")
        opc = int(input("Escolha uma opcao: "))
        if opc == 1:
            data = input("Data da Visita: ")
            cadastros[(cpf,nome)][0] = data
        elif opc == 2:
            dia = input("Dia da Semana: ")
            cadastros[(cpf,nome)][1] = dia
        elif opc == 3:
            entrada = input("Hora de Entrada: ")
            cadastros[(cpf,nome)][2] = entrada
        elif opc == 4:
            saida = input("Hora de Saida: ")
            cadastros[(cpf,nome)][3] = saida
        else:
            print("OPCAO INVALIDA!")

def remover(cadastros):
    cpf = input("CPF do Visitante: ")
    nome = input("Ponto Turistico: ")
    if (cpf,nome) not in cadastros:
        print("VISITA NAO CADASTRADA!")
    #funcao funcionando
    confirma = input("Certeza que deseja remover ?(sim/nao)")
    while confirma != "sim" and confirma != "nao":
        print("Opcao invalida...")
        confirma = input("Certeza que deseja remover ?(sim/nao)")
    if confirma == "sim":
        del cadastros[(cpf,nome)]
        print("Visitante removido com sucesso!")
    elif confirma == "nao":
        print("Operacao cancelada!")
        
def listar(cadastros):
    cpf = input("CPF do Visitante: ")
    nome = input("Ponto Turistico: ")
    if (cpf,nome) not in cadastros:
        print("VISITA NAO CADASTRADA!")
    else:
        print("====== VISITA ======")
        print("CPF: ", cpf)
        print("Ponto Turistico: ", nome.title())
        print("Data da Visita: ", cadastros[(cpf,nome)][0])
        print("Dia da Semana: ", cadastros[(cpf,nome)][1])
        print("Hora  de Entrada: ", cadastros[(cpf,nome)][2])
        print("Hora de Saida: " , cadastros[(cpf,nome)][3])
        print("Preco do Ingresso: ", cadastros[(cpf,nome)][4])
        print("=======================")

def listarTodos(cadastros):
        print("====== VISITAS ======")
        for visita in cadastros:
            print("CPF: ", visita[0])
            print("Ponto Turistico: ", visita[1].title())
            print("Data da Visita: ", cadastros[visita][0])
            print("Dia da Semana: ", cadastros[visita][1])
            print("Hora  de Entrada: ", cadastros[visita][2])
            print("Hora de Saida: ", cadastros[visita][3])
            print("Preco do Ingresso: ", cadastros[visita][4])
            print("=======================")

def grava_cadastro(cadastros):
    print("Gravando registros de Visitas...")
    arq = open("Visitas.txt","w")
    for visita in cadastros:
        linha = visita[0]+"\t"+visita[1]+"\t"+cadastros[visita][0]+"\t"+cadastros[visita][1]+"\t"+cadastros[visita][2]+"\t"+cadastros[visita][3]+"\t"+str(cadastros[visita][4])+"\n"
        arq.write(linha)
    arq.close()

def recupera_cadastro(cadastros):
    print("Recuperando registros de Visitas...")
    arq = open("Visitas.txt","r")
    linha = arq.readline()
    #Recupera primeira linha
    linha = linha[:len(linha)-1]
    visita = linha.split("\t")
    visita[6] = float(visita[6])
    cadastros[(visita[0],visita[1])] = visita[2:]
    #Recupera as outras linhas
    for linha in arq:
        linha = linha[:len(linha)-1]
        visita = linha.split("\t")
        visita[6] = float(visita[6])
        cadastros[(visita[0],visita[1])] = visita[2:]
    arq.close()
        
