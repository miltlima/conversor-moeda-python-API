#Importação dos módulos
import requests
import json
import pandas
#consumo do API da fixer
url = "http://data.fixer.io/api/latest?access_key=1a6fb5944548d113b88b19e9cd503952"
resposta = requests.get (url)
print(resposta)
if resposta.status_code == 200:
    print("Acesso realizado com sucesso")
    print("Buscando Informações...")
    dados = resposta.json()
    dolar_real = round(dados['rates']['BRL']/dados['rates']['USD'], 2)
    euro_real = round(dados['rates']['BRL']/dados['rates']['EUR'], 2)
    libra_real = round(dados['rates']['BRL']/dados['rates']['GBP'], 2)
    btc_real = round(dados['rates']['BRL']/dados['rates']['BTC'], 2)
    print("Dolar Americano: ", dolar_real, "reais")
    print("Euro ", euro_real, "reais")
    print("Libra ", libra_real, "reais")
    print("Bitcoin",btc_real, "reais")
    print("exportando resultado em tabela excel")
    tela = pandas.DataFrame({'Moedas':['Dolar','Euro','Libra','Bitcoin'],'Valores':[dolar_real, euro_real,libra_real, btc_real]})
    tela.to_csv('valores.csv')
    print('Arquivos exportados com sucesso')
else:
    print("Erro ao ler dados")