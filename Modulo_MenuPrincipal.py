import Modulo_Visitantes
import Modulo_PontosTur
import Modulo_Visitas
import Modulo_Relatorios

def menu_principal(pontosTur,visitantes,visitas):
    opc = 0
    while opc != 5:
        print("============ MENU PRINCIPAL =============")
        print("1- Gerenciamento de Pontos Turisticos")
        print("2- Gerenciamento de Visitantes")
        print("3- Gerenciamento de Visitas")
        print("4- Relatorios")
        print("5- Sair")
        print("=========================================")
        opc = int(input("Escolha uma opcao: "))
        if opc < 1 or opc > 5:
            print("OPCAO INVALIDA!")
        else:
            print("---------------------------------------------------")
            if opc == 1:
                Modulo_PontosTur.menu(pontosTur)
            if opc == 2:
                Modulo_Visitantes.menu(visitantes)    
            if opc == 3:
                if not existe_arquivo("PontosTur.txt"):
                    print("NENHUM PONTO TURISTICO CADASTRADO!")
                elif not existe_arquivo("Visitantes.txt"):
                    print("NENHUM VISITANTE CADASTRADO!")
                else:
                    Modulo_Visitas.menu(pontosTur,visitantes,visitas)
            if opc == 4:
                if not existe_arquivo("PontosTur.txt"):
                    print("NENHUM PONTO TURISTICO CADASTRADO!")
                elif not existe_arquivo("Visitantes.txt"):
                    print("NENHUM VISITANTE CADASTRADO!")
                else:
                    Modulo_Relatorios.menu(pontosTur,visitantes,visitas)
    
def existe_arquivo(arq):
    import os
    if os.path.exists(arq):
        return True
    else:
        return False
