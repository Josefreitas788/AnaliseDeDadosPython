import pandas as pd 
import seaborn as sns
from tratamento_AuxilioBrasil import *



#Não há valores varios no dataframe
#print(df["VALOR PARCELA"].sum())
df = tratamento_AuxilioBrasil()
print(df)
sns.set(style="darkgrid")
ax = sns.countplot(x="regiao", data=df)
ax.set_title('Auxilio Brasil por Região')
ax.set_xlabel('Região')
ax.set_ylabel('Quantidade de Beneficiários')
ax.figure.savefig('auxilio_brasil_regiao.png')

#ax = sns.countplot(x="", data=df)

    

