# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.5 # tempo de espera de cada ação da automação

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=1072, y=471)

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5) # tempo para garantir que o site tenha carregado

# Passo 2: Fazer login
# Colocando os passos abaixo como comentario, devido ao meu computador salvar o login,mas caso necessario tira o #,nas linhas onde tem *
# selecionar o campo de email
# * pyautogui.click(x=893, y=371)
# escrever o seu email
# * pyautogui.write("pythonimpressionador@gmail.com")
# * pyautogui.press("tab") # passando pro próximo campo
# * pyautogui.write("senha")
# clique no botao de login
pyautogui.click(x=964, y=532)
time.sleep(5)

# Cada indice dado ao "pyautogui.click(x,y)" depende de cada computador
# Por isso a ultilização do arquivo "auxiliar.py" para saber esse indices

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)   

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código do produto
    pyautogui.click(x=755, y=262)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim