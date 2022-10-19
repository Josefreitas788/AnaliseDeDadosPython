import pandas as pd 

list_df = []
chunk_pd = pd.read_csv('~/Downloads/202207_Militares/202207_Cadastro.csv',encoding = 'iso-8859-15',sep=';', chunksize=100000)
df_cadastro = pd.DataFrame()

colunas_para_retirar_cadastro = ['CPF', 'MATRICULA', 'CLASSE_CARGO', 'REFERENCIA_CARGO', 'PADRAO_CARGO', 'NIVEL_CARGO',
       'SIGLA_FUNCAO', 'NIVEL_FUNCAO', 'FUNCAO', 'CODIGO_ATIVIDADE',
       'ATIVIDADE', 'OPCAO_PARCIAL', 'COD_UORG_LOTACAO', 'UORG_LOTACAO',
       'COD_ORG_LOTACAO', 'ORG_LOTACAO', 'COD_ORGSUP_LOTACAO',
       'ORGSUP_LOTACAO', 'COD_UORG_EXERCICIO', 'UORG_EXERCICIO',
       'COD_ORG_EXERCICIO', 'ORG_EXERCICIO', 'COD_ORGSUP_EXERCICIO',
       'ORGSUP_EXERCICIO', 'COD_TIPO_VINCULO', 'TIPO_VINCULO',
       'SITUACAO_VINCULO', 'DATA_INICIO_AFASTAMENTO',
       'DATA_TERMINO_AFASTAMENTO', 'REGIME_JURIDICO', 'JORNADA_DE_TRABALHO',
       'DATA_INGRESSO_CARGOFUNCAO', 'DATA_NOMEACAO_CARGOFUNCAO',
       'DATA_INGRESSO_ORGAO', 'DOCUMENTO_INGRESSO_SERVICOPUBLICO',
       'DATA_DIPLOMA_INGRESSO_SERVICOPUBLICO', 'DIPLOMA_INGRESSO_CARGOFUNCAO',
       'DIPLOMA_INGRESSO_ORGAO', 'DIPLOMA_INGRESSO_SERVICOPUBLICO',
       'UF_EXERCICIO']

for piece in chunk_pd:
    
    piece = piece.drop(colunas_para_retirar_cadastro,axis=1)      
    df_cadastro = piece
    list_df.append(piece)
    break

df_cadastro = pd.concat(list_df)
        
        
chunk_pd = pd.read_csv('~/Downloads/202207_Militares/202207_Remuneracao.csv',encoding = 'iso-8859-15',sep=';', chunksize=100000)
df_remuneracao = pd.DataFrame()
colunas_para_retirar_remunerada = ['ANO', 'MES', 'CPF', 
       'ABATE-TETO (R$)', 'ABATE-TETO (U$)', 'GRATIFICAÇÃO NATALINA (R$)',
       'GRATIFICAÇÃO NATALINA (U$)',
       'ABATE-TETO DA GRATIFICAÇÃO NATALINA (R$)',
       'ABATE-TETO DA GRATIFICAÇÃO NATALINA (U$)', 'FÉRIAS (R$)',
       'FÉRIAS (U$)', 'OUTRAS REMUNERAÇÕES EVENTUAIS (R$)',
       'OUTRAS REMUNERAÇÕES EVENTUAIS (U$)', 'IRRF (R$)', 'IRRF (U$)',
       'PSS/RPGS (R$)', 'PSS/RPGS (U$)', 'DEMAIS DEDUÇÕES (R$)',
       'DEMAIS DEDUÇÕES (U$)', 'PENSÃO MILITAR (R$)', 'PENSÃO MILITAR (U$)',
       'FUNDO DE SAÚDE (R$)', 'FUNDO DE SAÚDE (U$)',
       'TAXA DE OCUPAÇÃO IMÓVEL FUNCIONAL (R$)',
       'TAXA DE OCUPAÇÃO IMÓVEL FUNCIONAL (U$)',
       'REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (R$)',
       'REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (U$)',
       'VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - CIVIL (R$)(*)',
       'VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - CIVIL (U$)(*)',
       'VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (R$)(*)',
       'VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (U$)(*)',
       'TOTAL DE VERBAS INDENIZATÓRIAS (R$)(*)',
       'TOTAL DE VERBAS INDENIZATÓRIAS (U$)(*)',
       'VERBAS INDENIZATÓRIAS REGISTRADAS EM SISTEMAS DE PESSOAL - MILITAR (U$)(*)',
       'TOTAL DE VERBAS INDENIZATÓRIAS (R$)(*)',
       'TOTAL DE VERBAS INDENIZATÓRIAS (U$)(*)']
for piece in chunk_pd:
    piece = piece.drop(colunas_para_retirar_remunerada,axis=1)
    piece = piece.drop(piece.columns[[-1]],axis=1)
    piece = piece.drop(piece.columns[[-1]],axis=1)
    df_remuneracao = piece
    list_df.append(piece)     
    print(piece.columns)
    break
df_remuneracao = pd.concat(list_df)

df = pd.merge(df_cadastro,df_remuneracao,how='inner',on='Id_SERVIDOR_PORTAL') 
print(df)
#df.to_csv('202207_Militares.csv',index=False)
