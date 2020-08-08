# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:09:16 2020

@author: Hamilton Tenório da Silva
"""


#importa as bibliotecas
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

#cria o dataframe para gravar um csv no final
colunas =  ['protocolo', 'dataAbertura', 'descricao', 'nome', 'apelido', 'assunto', 'classificacao', 'aprovacao', 'arquivamento', 'ementa']
todasAsEmentas = pd.DataFrame(columns = colunas)

#informa a localização do driver do Chrome automatizado
driver = webdriver.Chrome("C:\ProgramData\Anaconda3\Lib\site-packages\chromedriver.exe")

pagina = 0
while True:
    pagina += 1
    print("Acessando página {}".format(pagina))
    
    #define URL para acesso e complementa com o número da página
    url = "https://mlegislativo.mirasoft.com.br/PortalMunicipe/Processos?page={}".format(pagina)
    driver.get(url)
    
    #procura as classes que representam cada bloco de informação
    elemento = driver.find_elements_by_class_name("col-sm-9.col-md-9.col-xs-12")
    ementa = driver.find_elements_by_class_name("panel-collapse.collapse")
    
    #verifica se ainda tem conteúdo
    if len(elemento) > 1:
        #define o número de blocos (são 5 elementos por bloco)
        blocos = len(elemento) // 5
        for i in range(blocos):
            protocolo = elemento[(i * 5) + 0].get_attribute('innerHTML').replace("\n", "").strip()
            dataAbertura = elemento[(i * 5) + 1].get_attribute('innerHTML').replace("\n", "").strip()
            vereador = elemento[(i * 5) + 2].get_attribute('innerHTML').replace("\n", "").strip()
            assunto = elemento[(i * 5) + 3].get_attribute('innerHTML').replace("\n", "").strip()
            dataFinal = elemento[(i * 5) + 4].get_attribute('innerHTML').replace("\n", "").strip()
            
            #retira conteúdo html de cada campo
            protocoloFinal = BeautifulSoup(protocolo, 'html.parser').get_text().replace("Número de Protocolo: ", "").strip()
            
            dataAberturaFinal = BeautifulSoup(dataAbertura, 'html.parser').get_text().strip()
            apoio = dataAberturaFinal.split("Data de Abertura:")
            descricao = apoio[0].replace("DESCRICAO:", "").strip()
            dataAbertura = apoio[1].strip()
            
            vereadorFinal = BeautifulSoup(vereador, 'html.parser').get_text().strip()
            apoio = vereadorFinal.split("Apelido:")
            nome = apoio[0].replace("Nome:", "").strip()
            apelido = apoio[1].strip()
            
            assuntoFinal = BeautifulSoup(assunto, 'html.parser').get_text().strip()
            apoio = assuntoFinal.split("Classificação:")
            assunto = apoio[0].replace("ASSUNTOS:", "").strip()
            classificacao = apoio[1].strip()
            
            dataFinalFinal = BeautifulSoup(dataFinal, 'html.parser').get_text().strip()
            apoio = dataFinalFinal.split("Data Arquivamento:")
            aprovacao = apoio[0].replace("Data Aprovação:", "").strip()
            arquivamento = apoio[1].strip()
            
            print("Protocolo {}".format(protocoloFinal))
            
            #pega o campo da ementa
            textoEmenta = BeautifulSoup(ementa[i].get_attribute('innerHTML'), 'html.parser').get_text().replace("\n", "").strip()
            #print(textoEmenta)
            dados = [[protocoloFinal, dataAbertura, descricao, nome, apelido, assunto, classificacao, aprovacao, arquivamento, textoEmenta]]
            esteRegistro = pd.DataFrame(data = dados, columns = colunas)
            todasAsEmentas = todasAsEmentas.append(esteRegistro)
    else:
        print("Não encontrou mais conteúdo. Encerrando.")
        break

#grava todo o conteúdo em um arquivo CSV    
todasAsEmentas.to_csv('projetos.csv', index = False, sep=";", quotechar='"', header=True)


#fecha o navegador
driver.quit()