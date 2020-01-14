import requests
import json
import pandas as pd
import decimal

url = "http://data.fixer.io/api/latest?access_key=1a6fb5944548d113b88b19e9cd503952"
resposta = requests.get (url) # resposta da URL
print(resposta)
if resposta.status_code == 200:
    print("Acesso realizado com sucesso")
    print("Buscando Informações...")
    dados = resposta.json()
    dolar_real = round(dados['rates']['BRL']/dados['rates']['USD'], 2) # conversão e arredondamento dos valores
    euro_real = round(dados['rates']['BRL']/dados['rates']['EUR'], 2)
    libra_real = round(dados['rates']['BRL']/dados['rates']['GBP'], 2)
    btc_real = round(dados['rates']['BRL']/dados['rates']['BTC'], 2)
    print("1 Dolar Americano vale: ", dolar_real, "reais")
    print("1 Euro vale ", euro_real, "reais")
    print("1 Libra vale ", libra_real, "reais")
    print("1 Bitcoin vale",btc_real, "reais")
    print("exportando resultado em tabela excel")
    #tela = pd.DataFrame({[dolar_real,euro_real,libra_real,btc_real], columns=['Dolar','Euro','Libra','Bitcoin']})
    tela = pd.DataFrame({'Moedas':['Dolar','Euro','Libra','Bitcoin'],'Valores':[dolar_real, euro_real,libra_real, btc_real]})
    tela.to_csv('valores.csv', index=False, sep=";",decimal=",")
    print('Arquivos exportados com sucesso')
else:
    print("Erro ao ler dados")