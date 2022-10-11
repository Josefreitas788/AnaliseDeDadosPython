import pandas as pd 
import seaborn as sns

chunk_pd = pd.read_csv('~/Downloads/202207_AuxilioBrasil.csv',encoding = 'iso-8859-15',sep=';', chunksize=100000)
listdf = []
regioes ={
    'norte' : ['AC','AM','AP','PA','RO','RR','TO'],
    'nordeste' : ['AL','BA','CE','MA','PB','PE','PI','RN','SE'],
    'sudeste' : ['ES','MG','RJ','SP'],
    'sul' : ['PR','RS','SC'],
    'centro_oeste' : ['DF','GO','MT','MS']
}
cont = 0
df = pd.DataFrame()
for piece in chunk_pd:
    
    piece = piece.drop(['MÊS COMPETÊNCIA','NOME FAVORECIDO','NIS FAVORECIDO','CÓDIGO MUNICÍPIO SIAFI', 'CPF FAVORECIDO'],axis=1)
    piece['regiao'] = piece['UF'].apply(lambda uf: 'norte' if uf in regioes['norte'] else 'nordeste' if uf in regioes['nordeste'] else 'sudeste' if uf in regioes['sudeste'] else 'sul' if uf in regioes['sul'] else 'centro_oeste')
    #df = piece
    #break
    listdf.append(piece)
    # cont =+ 1
    # if cont == 2:
    #     break
    

df = pd.concat(listdf)

#Não há valores varios no dataframe
#print(df["VALOR PARCELA"].sum())

print(df)
sns.set(style="whitegrid")
ax = sns.countplot(x="regiao", data=df)
ax.set_title('Auxilio Brasil por Região')
ax.set_xlabel('Região')
ax.set_ylabel('Quantidade de Beneficiários')
ax.figure.savefig('auxilio_brasil_regiao.png')

ax = sns.countplot(x="", data=df)

    

