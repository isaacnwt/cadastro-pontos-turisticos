import Modulo_Visitantes
import Modulo_PontosTur
import Modulo_MenuPrincipal
import Modulo_Visitas

#LISTA DE PONTOS TURISTICOS
pontosTur = []
if not Modulo_MenuPrincipal.existe_arquivo("PontosTur.txt"):
    cidade = input("Insira uma cidade: ")
    pontosTur.append(cidade)
    pontosTur.append([])
else:
    Modulo_PontosTur.recupera_cadastro(pontosTur)
    
#DICIONARIO DE VISITANTES   
visitantes = {}
if Modulo_MenuPrincipal.existe_arquivo("Visitantes.txt"):
    Modulo_Visitantes.recupera_cadastro(visitantes)
        
#DICIONARIO DE VISITAS
visitas = {}
if Modulo_MenuPrincipal.existe_arquivo("Visitas.txt"):
    Modulo_Visitas.recupera_cadastro(visitas)

Modulo_MenuPrincipal.menu_principal(pontosTur,visitantes,visitas)
