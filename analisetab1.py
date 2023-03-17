import pandas as pd
import numpy
import openpyxl
import plotly.express as px
#axis = 0 == linha
#axis = 1 == coluna
#.drop é para retirar e dropna é para excluir valores vazios
#how é como vai ser all ou any, all é excluir as que tem tds os valores vazios e any as que tem um valor ou mais vazios
#se quiser excluir mais de uma use lista[] 
tabela = pd.read_csv(r"dadosusuarios.csv")
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],errors="coerce")
#para transformar usa pd.to_ dai vc escolhe qual mudança vc quer selecionar para sua tabela
#para erro, pode usar o ignore para ignorar, o raise para ele mostrar o erro, ou coerce que ele vai mudar os valores n numericos para virarem numericos, e os de textos vão ficar vazio
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())
print (tabela)
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))
#normalize vai mostar a porcentagem de pessoas que cancelaram
