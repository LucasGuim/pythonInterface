import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: R$ {cotacao_dolar} 
    Euro: R$ {cotacao_euro} 
    BTC: R$ {cotacao_btc}'''

    cotacoes['text']=texto



janela = Tk()

janela.title("Cotações em tempo real: ")
titulo = Label(janela,text='Clique no botão para atualizar as cotações das moedas. ',padx=10)
titulo.grid(column=0,row=0,pady=10)
botão = Button(janela,text='Executar',command=pegar_cotacoes,pady=5,padx=5)
botão.grid(column=0,row=1)
cotacoes = Label(janela,text='',pady=10)
cotacoes.grid(column=0,row=2,)

janela.mainloop()