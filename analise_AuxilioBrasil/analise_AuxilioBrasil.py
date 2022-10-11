import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


chunk_pd = pd.read_csv('202207_AuxilioBrasil.csv',encoding = 'iso-8859-15',sep=';', chunksize=100000)
listdf = []
regioes ={
    'norte' : ['AC','AM','AP','PA','RO','RR','TO'],
    'nordeste' : ['AL','BA','CE','MA','PB','PE','PI','RN','SE'],
    'sudeste' : ['ES','MG','RJ','SP'],
    'sul' : ['PR','RS','SC'],
    'centro_oeste' : ['DF','GO','MT','MS']
}

df = pd.DataFrame()
for piece in chunk_pd:

    piece = piece.drop(['MÊS COMPETÊNCIA','NOME FAVORECIDO','NIS FAVORECIDO','CÓDIGO MUNICÍPIO SIAFI', 'CPF FAVORECIDO'],axis=1)
    piece['regiao'] = piece['UF'].apply(lambda uf: 'norte' if uf in regioes['norte'] else 'nordeste' if uf in regioes['nordeste'] else 'sudeste' if uf in regioes['sudeste'] else 'sul' if uf in regioes['sul'] else 'centro_oeste')
    df = piece
    break
    listdf.append(piece)
    

#df = pd.concat(listdf)

#Não há valores varios no dataframe
#print(df["VALOR PARCELA"].sum())

print(df)

sns.set(style="darkgrid")

plt.show()



    

