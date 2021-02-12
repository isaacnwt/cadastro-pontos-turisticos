def menu(cadastros):
    opc = 0
    while opc != 6:
        print("===== GERENCIAMENTO DE VISITANTES =====")
        print("1- Cadastrar Visitante")
        print("2- Alterar Visitante")
        print("3- Remover Visitante")
        print("4- Listar um Visitante")
        print("5- Listar todos Visitantes")
        print("6- Sair")
        print("========================================")
        opc = int(input("Escolha uma opcao: "))
        if opc < 1 or opc > 6:
            print("OPCAO INVALIDA!")
        else:
            if opc == 1:
                cadastrar(cadastros) 
            elif opc == 2:
                alterar(cadastros)
            elif opc == 3:
                remover(cadastros)
            elif opc == 4:
                listar(cadastros)
            elif opc == 5:
                listarTodos(cadastros)
    grava_cadastro(cadastros)

def cadastrar(cadastros):
    cpf = input("CPF do Visitante: ")
    if cpf in cadastros:
        print("VISITANTE JA CADASTRADO!")
    else:
        nome = input("Nome Completo: ")
        data = input("Data de Nascimento: ")
        cidade = input("Cidade: ")
        prof = input("Profissao: ")
        email = input("E-mail: ")
        if email == "":
            email = "NAO POSSUI EMAIL"
        telLista = []
        tel =(input("Telefone(s): "))
        if tel == "":
            telLista = ["NAO POSSUI TELEFONE"]
        else:
            while tel != "":
                telLista.append(tel)
                tel =(input("Telefone(s): "))
        cadastros[cpf] = (nome,data,cidade,prof,email,telLista)

def alterar(cadastros):
    cpf = input("CPF do Visitante: ")
    if cpf not in cadastros:
        print("VISITANTE NAO CADASTRADO!")
    else:
        vis = list(cadastros[cpf])
        print("== QUAL ITEM DESEJA ALTERAR? ==")
        print("1- Alterar Nome")
        print("2- Alterar Data de Nascimento")
        print("3- Alterar Cidade: ")
        print("4- Alterar Profissao")
        print("5- Alterar E-mail")
        print("6- Alterar Telefone(s)")
        print("===============================")
        opc = int(input("Escolha uma opcao: "))
        if opc == 1:
            nome = input("Nome: ")
            vis[0] = nome
        elif opc == 2:
            data = input("Data: ")
            vis[1] = data
        elif opc == 3:
            cidade = input("Cidade: ")
            vis[2] = cidade
        elif opc == 4:
            prof = input("Profissao: ")
            vis[3] = prof
        elif opc == 5:
            email = input("E-mail: ")
            if email == "":
                email = "NAO POSSUI EMAIL"
            vis[4] = email
        elif opc == 6:
            telLista = []
            tel =(input("Telefone(s): "))
            if tel == "":
                telLista = ["NAO POSSUI TELEFONE"]
            else:
                while tel != "":
                    telLista.append(tel)
                    tel =(input("Telefone(s): "))
            vis[5] = telLista
        else:
            print("OPCAO INVALIDA!")
        vis = tuple(vis)
        cadastros[cpf] = vis 
            
def remover(cadastros):
    cpf = input("CPF do Visitante: ")
    if cpf not in cadastros:
        print("VISITANTE NAO CADASTRADO!")
    else:
        del cadastros[cpf]
        print("Visitante removido com sucesso!")

def listar(cadastros):
    cpf = input("CPF do Visitante: ")
    if cpf not in cadastros:
        print("VISITANTE NAO CADASTRADO!")
    else:
        print("====== VISITANTE ======")
        print("CPF: ", cpf)
        print("Nome: ", cadastros[cpf][0].title())
        print("Data de Nascimento: ", cadastros[cpf][1])
        print("Cidade: ", cadastros[cpf][2].title())
        print("Profissao: ", cadastros[cpf][3].title())
        print("E-mail: " , cadastros[cpf][4])
        print("Telefone(s): ", ', '.join(map(str,cadastros[cpf][5])))
        print("=======================")

def listarTodos(cadastros):
    print("====== VISITANTES ======")
    for cpf in cadastros:
        print("CPF: ", cpf)
        print("Nome: ", cadastros[cpf][0].title())
        print("Data de Nascimento: ", cadastros[cpf][1])
        print("Cidade: ", cadastros[cpf][2].title())
        print("Profissao: ", cadastros[cpf][3].title())
        print("E-mail: " , cadastros[cpf][4])
        print("Telefone(s): ", ', '.join(map(str,cadastros[cpf][5])))
        print("=======================")

def grava_cadastro(cadastros):
    print("Gravando registros de Visitantes...")
    arq = open("Visitantes.txt","w")
    for cpf in cadastros:
        telefones =(cadastros[cpf][5])
        for num in range(len(telefones)):
            tels = "#".join(telefones)
        linha = cpf+"\t"+cadastros[cpf][0]+"\t"+cadastros[cpf][1]+"\t"+cadastros[cpf][2]+"\t"+cadastros[cpf][3]+"\t"+cadastros[cpf][4]+"\t"+tels+"\n"
        arq.write(linha)
    arq.close()

def recupera_cadastro(cadastros):
    print("Recuperando registros de Visitantes...")
    arq = open("Visitantes.txt","r")
    linha = arq.readline()
    #Recupera primeira linha
    linha = linha[:len(linha)-1]
    visitante = linha.split("\t")
    visitante[6] = visitante[6].split("#")
    cadastros[visitante[0]] = tuple(visitante[1:])
    #Recupera as outras linhas
    for linha in arq:
        linha = linha[:len(linha)-1]
        visitante = linha.split("\t")
        visitante[6] = visitante[6].split("#")
        cadastros[visitante[0]] = tuple(visitante[1:])
    arq.close()



        
