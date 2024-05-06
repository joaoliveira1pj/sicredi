import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
agencias = pd.read_excel('./base_agencias.xlsb', sheet_name='base')
associados = pd.read_excel('./base_associados.xlsb', sheet_name='base')
indicadores = pd.read_excel('./base_indicadores.xlsb', sheet_name='base')

# Definir a ordem das faixas etárias
faixas_etarias = ['18-25 anos', '26-30 anos', '31-45 anos', '46-60 anos', 'maiores de 60 anos']

# Definir a função para criar a faixa etária
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

# Aplicar a função para criar a coluna 'Faixa Etária'
associados['Faixa Etária'] = associados['idade'].apply(criar_faixa_etaria)

# Converter a coluna 'Faixa Etária' para tipo categórico com a ordem desejada
associados['Faixa Etária'] = pd.Categorical(associados['Faixa Etária'], categories=faixas_etarias, ordered=True)

# Juntar os dados
dados_completos = pd.merge(pd.merge(associados, indicadores, on=['ano_mes', 'num_conta']), agencias, on=['ano_mes', 'cod_ag'])

# Configurar o estilo do gráfico
sns.set(style="whitegrid")

# Criar o gráfico de barras
plt.figure(figsize=(12, 8))
grafico = sns.barplot(x='nome_ag', y='vlr_investimentos', hue='Faixa Etária', data=dados_completos)
grafico.set_xticklabels(grafico.get_xticklabels(), rotation=45)

# Adicionar título e rótulos aos eixos
plt.title('Investimentos por Agência e Faixa Etária')
plt.xlabel('Nome da Agência')
plt.ylabel('Valor dos Investimentos')

# Adicionar legenda
plt.legend(title='Faixa Etária')

# Ajustar layout e mostrar o gráfico
plt.tight_layout()
plt.show()
