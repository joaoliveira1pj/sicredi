import pandas as pd
import matplotlib.pyplot as plt

agencias = pd.read_excel('./base_agencias.xlsb', sheet_name='base', engine='pyxlsb')
associados = pd.read_excel('./base_associados.xlsb', sheet_name='base', engine='pyxlsb')
indicadores = pd.read_excel('./base_indicadores.xlsb', sheet_name='base', engine='pyxlsb')

def criar_faixa_etaria(idade):
    if idade <= 25:
        return '18-25 anos'
    elif idade <= 30:
        return '26-30 anos'
    elif idade <= 45:
        return '31-45 anos'
    elif idade <= 60:
        return '46-60 anos'
    else:
        return 'maiores de 60 anos'

associados['Faixa Etária'] = associados['idade'].apply(criar_faixa_etaria)

dados_completos = pd.merge(pd.merge(associados, indicadores, on=['ano_mes', 'num_conta']), agencias, on=['ano_mes', 'cod_ag'])

contagem_pessoas_por_agencia = dados_completos.groupby('nome_ag')['num_conta'].nunique()

fig, axs = plt.subplots(2, 1, figsize=(10,10))

dados_completos.groupby(['nome_ag', 'Faixa Etária'])['vlr_investimentos'].sum().unstack().plot(kind='bar', stacked=True, ax=axs[0])
axs[0].set_title('Investimentos por Agência e Faixa Etária')
axs[0].set_xlabel('Nome da Agência')
axs[0].set_ylabel('Valor dos Investimentos')
axs[0].tick_params(axis='x', rotation=30)

contagem_pessoas_por_agencia.plot(kind='bar', ax=axs[1])
axs[1].set_title('Número de Pessoas por Agência')
axs[1].set_xlabel('Nome da Agência')
axs[1].set_ylabel('Número de Pessoas')
axs[1].tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.show()
