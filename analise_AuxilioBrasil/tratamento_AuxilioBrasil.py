import pandas as pd 

def tratamento_AuxilioBrasil():
    chunk_pd = pd.read_csv('~/Downloads/202207_AuxilioBrasil.csv',encoding = 'iso-8859-15',sep=';', chunksize=100000)
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
        listdf.append(piece)


    df = pd.concat(listdf)
    return df 


