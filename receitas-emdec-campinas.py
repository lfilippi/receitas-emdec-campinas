
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[51]:


receitas_emdec = pd.read_csv('receitas_emdec.csv', encoding='utf=8')
receitas_emdec.head(11)


# # Multas de trânsito e transportes

# In[12]:


#Filtra os valores de arrecadação das multas de trânsito e transportes por ano e soma

ano_2012 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2012.csv']
multas_transito_2012 = ano_2012[ano_2012['Receita'] == 'MULTAS DE TRÂNSITO']
multas_transportes_2012 = ano_2012[ano_2012['Receita'] == 'MULTAS DE TRANSPORTES']
total_multas_transito_2012 = multas_transito_2012['Valor'].astype('float64').sum()
total_multas_transportes_2012 = multas_transportes_2012['Valor'].astype('float64').sum()
total_multas_2012 = total_multas_transito_2012 + total_multas_transportes_2012

ano_2013 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2013.csv']
multas_transito_2013 = ano_2013[ano_2013['Receita'] == 'MULTAS DE TRÂNSITO']
multas_transportes_2013 = ano_2013[ano_2013['Receita'] == 'MULTAS DE TRANSPORTES']
total_multas_transito_2013 = multas_transito_2013['Valor'].astype('float64').sum()
total_multas_transportes_2013 = multas_transportes_2013['Valor'].astype('float64').sum()
total_multas_2013 = total_multas_transito_2013 + total_multas_transportes_2013

ano_2014 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2014.csv']
multas_transito_2014 = ano_2014[ano_2014['Receita'] == 'MULTAS DE TRÂNSITO']
multas_transportes_2014 = ano_2014[ano_2014['Receita'] == 'MULTAS DE TRANSPORTES']
total_multas_transito_2014 = multas_transito_2014['Valor'].astype('float64').sum()
total_multas_transportes_2014 = multas_transportes_2014['Valor'].astype('float64').sum()
total_multas_2014 = total_multas_transito_2014 + total_multas_transportes_2014

ano_2015 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2015.csv']
multas_transito_2015 = ano_2015[ano_2015['Receita'] == 'MULTAS DE TRÂNSITO']
multas_transportes_2015 = ano_2015[ano_2015['Receita'] == 'MULTAS DE TRANSPORTES']
total_multas_transito_2015 = multas_transito_2015['Valor'].astype('float64').sum()
total_multas_transportes_2015 = multas_transportes_2015['Valor'].astype('float64').sum()
total_multas_2015 = total_multas_transito_2015 + total_multas_transportes_2015

ano_2016 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2016.csv']
multas_transito_2016 = ano_2016[ano_2016['Receita'] == 'MULTAS DE TRÂNSITO']
multas_transportes_2016 = ano_2016[ano_2016['Receita'] == 'MULTAS DE TRANSPORTES']
total_multas_transito_2016 = multas_transito_2016['Valor'].astype('float64').sum()
total_multas_transportes_2016 = multas_transportes_2016['Valor'].astype('float64').sum()
total_multas_2016 = total_multas_transito_2016 + total_multas_transportes_2016

ano_2017 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2017.csv']
multas_transito_2017 = ano_2017[ano_2017['Receita'] == 'MULTAS DE TRÂNSITO']
multas_transportes_2017 = ano_2017[ano_2017['Receita'] == 'MULTAS DE TRANSPORTES']
total_multas_transito_2017 = multas_transito_2017['Valor'].astype('float64').sum()
total_multas_transportes_2017 = multas_transportes_2017['Valor'].astype('float64').sum()
total_multas_2017 = total_multas_transito_2017 + total_multas_transportes_2017

ano_2018 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2018.csv']
multas_transito_2018 = ano_2018[ano_2018['Receita'] == 'MULTAS DE TRÂNSITO']
multas_transportes_2018 = ano_2018[ano_2018['Receita'] == 'MULTAS DE TRANSPORTES']
total_multas_transito_2018 = multas_transito_2018['Valor'].astype('float64').sum()
total_multas_transportes_2018 = multas_transportes_2018['Valor'].astype('float64').sum()
total_multas_2018 = total_multas_transito_2018 + total_multas_transportes_2018


# In[16]:


#Valor médio mensal das receitas com multas em 2017

total_multas_2017 / 12


# In[15]:


#Valor médio mensal das receitas com multas em 2017

total_multas_2018 / 4


# In[14]:


#Valor total das receitas com multas de 2012 a 2017

total_multas_2012 + total_multas_2013 + total_multas_2014 + total_multas_2015 + total_multas_2016 + total_multas_2017


# In[19]:


#Constrói um dicionário com os dados

multas = {'Ano': ['2012', '2013', '2014', '2015', '2016', '2017'],
         'Multas transportes': [total_multas_transportes_2012, total_multas_transportes_2013, total_multas_transportes_2014, 
                                total_multas_transportes_2015, total_multas_transportes_2016, total_multas_transportes_2017],
         'Multas trânsito': [total_multas_transito_2012, total_multas_transito_2013, total_multas_transito_2014, 
                                total_multas_transito_2015, total_multas_transito_2016, total_multas_transito_2017],
         'Total': [total_multas_2012, total_multas_2013, total_multas_2014, total_multas_2015, total_multas_2016, total_multas_2017]}


# In[20]:


#Transforma o dicionário em um dataframe

df_total_multas = pd.DataFrame.from_dict(multas)
#df_total_multas.set_index('Ano', inplace=True)
df_total_multas.head(6)


# In[31]:


#Gera um arquivo CSV com os dados do dataframe

df_total_multas.to_csv('multas_transito_emdec_2012_2017.csv', encoding='utf-8')


# In[25]:


#Gráfico com o total em multas de 2012 a 2017

plt.style.use('ggplot')
df_total_multas.plot(kind='bar', y='Total', x='Ano')


# # Pátio de veículos

# In[27]:


#Filtra os valores de arrecadação por ano e faz a soma

ano_2012 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2012.csv']
patio_2012 = ano_2012[ano_2012['Receita'] == 'PÁTIO DE VEÍCULOS']
total_patio_2012 = patio_2012['Valor'].astype('float64').sum()

ano_2013 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2013.csv']
patio_2013 = ano_2013[ano_2013['Receita'] == 'PÁTIO DE VEÍCULOS']
total_patio_2013 = patio_2013['Valor'].astype('float64').sum()

ano_2014 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2014.csv']
patio_2014 = ano_2014[ano_2014['Receita'] == 'PÁTIO DE VEÍCULOS']
total_patio_2014 = patio_2014['Valor'].astype('float64').sum()

ano_2015 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2015.csv']
patio_2015 = ano_2015[ano_2015['Receita'] == 'PÁTIO DE VEÍCULOS']
total_patio_2015 = patio_2015['Valor'].astype('float64').sum()

ano_2016 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2016.csv']
patio_2016 = ano_2016[ano_2016['Receita'] == 'PÁTIO DE VEÍCULOS']
total_patio_2016 = patio_2016['Valor'].astype('float64').sum()

ano_2017 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2017.csv']
patio_2017 = ano_2017[ano_2017['Receita'] == 'PÁTIO DE VEÍCULOS']
total_patio_2017 = patio_2017['Valor'].astype('float64').sum()


# In[28]:


#Constrói um dicionário com os dados

patio = {'Ano': ['2012', '2013', '2014', '2015', '2016', '2017'],
         'Pátio de veículos': [total_patio_2012, total_patio_2013, total_patio_2014, 
                   total_patio_2015, total_patio_2016, total_patio_2017]}


# In[29]:


#Transforma o dicionário em um dataframe

df_total_patio = pd.DataFrame.from_dict(patio)
df_total_patio.set_index('Ano', inplace=True)
df_total_patio.head(6)


# In[60]:


#Gera um arquivo CSV com os dados do dataframe

df_total_patio.to_csv('arrecadacao_patio_emdec_2012_2017.csv', encoding='utf-8')


# In[30]:


#Gráfico com o total das receitas com o pátio de veículos de 2012 a 2017

plt.style.use('ggplot')
df_total_patio.plot(kind='bar')


# # Outras receitas

# In[54]:


#Filtra os valores de arrecadação por ano e faz a soma

ano_2012 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2012.csv']
convenio_2012 = ano_2012[ano_2012['Receita'] == 'CONVÊNIO PMC']
total_convenio_2012 = convenio_2012['Valor'].astype('float64').sum()

ano_2017 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2017.csv']
convenio_2017 = ano_2017[ano_2017['Receita'] == 'CONVÊNIO PMC']
total_convenio_2017 = convenio_2017['Valor'].astype('float64').sum()


# In[32]:


#Filtra os valores de arrecadação por ano e faz a soma

ano_2012 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2012.csv']
estacionamento_2012 = ano_2012[ano_2012['Receita'] == 'ESTACIONAMENTO ROTATIVO']
total_estacionamento_2012 = estacionamento_2012['Valor'].astype('float64').sum()

ano_2017 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2017.csv']
estacionamento_2017 = ano_2017[ano_2017['Receita'] == 'ESTACIONAMENTO ROTATIVO']
total_estacionamento_2017 = estacionamento_2017['Valor'].astype('float64').sum()


# In[41]:


#Filtra os valores de arrecadação por ano e faz a soma

ano_2012 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2012.csv']
outras_2012 = ano_2012[ano_2012['Receita'] == 'OUTRAS RECEITAS']
total_outras_2012 = outras_2012['Valor'].astype('float64').sum()

ano_2017 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2017.csv']
outras_2017 = ano_2017[ano_2017['Receita'] == 'OUTRAS RECEITAS']
total_outras_2017 = outras_2017['Valor'].astype('float64').sum()


# In[34]:


#Filtra os valores de arrecadação por ano e faz a soma

ano_2012 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2012.csv']
patio_2012 = ano_2012[ano_2012['Receita'] == 'PÁTIO DE VEÍCULOS']
total_patio_2012 = patio_2012['Valor'].astype('float64').sum()

ano_2017 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2017.csv']
patio_2017 = ano_2017[ano_2017['Receita'] == 'PÁTIO DE VEÍCULOS']
total_patio_2017 = patio_2017['Valor'].astype('float64').sum()


# In[35]:


#Filtra os valores de arrecadação por ano e faz a soma

ano_2012 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2012.csv']
financeiras_2012 = ano_2012[ano_2012['Receita'] == 'RECEITAS FINANCEIRAS']
total_financeiras_2012 = financeiras_2012['Valor'].astype('float64').sum()

ano_2017 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2017.csv']
financeiras_2017 = ano_2017[ano_2017['Receita'] == 'RECEITAS FINANCEIRAS']
total_financeiras_2017 = financeiras_2017['Valor'].astype('float64').sum()


# In[36]:


#Filtra os valores de arrecadação por ano e faz a soma

ano_2012 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2012.csv']
intercamp_2012 = ano_2012[ano_2012['Receita'] == 'TAXA DE GERENCIAMENTO INTERCAMP']
total_intercamp_2012 = intercamp_2012['Valor'].astype('float64').sum()

ano_2017 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2017.csv']
intercamp_2017 = ano_2017[ano_2017['Receita'] == 'TAXA DE GERENCIAMENTO INTERCAMP']
total_intercamp_2017 = intercamp_2017['Valor'].astype('float64').sum()


# In[37]:


#Filtra os valores de arrecadação por ano e faz a soma

ano_2012 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2012.csv']
taxi_2012 = ano_2012[ano_2012['Receita'] == 'TAXA DE TAXI']
total_taxi_2012 = taxi_2012['Valor'].astype('float64').sum()

ano_2017 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2017.csv']
taxi_2017 = ano_2017[ano_2017['Receita'] == 'TAXA DE TAXI']
total_taxi_2017 = taxi_2017['Valor'].astype('float64').sum()


# In[38]:


#Filtra os valores de arrecadação por ano e faz a soma

ano_2012 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2012.csv']
vistoria_2012 = ano_2012[ano_2012['Receita'] == 'VISTORIA DE VEÍCULOS']
total_vistoria_2012 = vistoria_2012['Valor'].astype('float64').sum()

ano_2017 = receitas_emdec[receitas_emdec['Ano'] == 'receitas_emdec_2017.csv']
vistoria_2017 = ano_2017[ano_2017['Receita'] == 'VISTORIA DE VEÍCULOS']
total_vistoria_2017 = vistoria_2017['Valor'].astype('float64').sum()


# In[55]:


#Constrói um dicionário com os dados

total_receitas_2017 = {'Tipo de receita': ['Multas de trânsito', 'Convênio PMC', 'Pátio de veículos', 
                                           'Taxa de gerenciamento Intercamp', 'Multas de transportes', 'Outras receitas'],

         'Valor': [total_multas_2017, total_convenio_2017, total_patio_2017, total_intercamp_2017, total_multas_transportes_2017, 
                   total_estacionamento_2017 + total_outras_2017 + total_financeiras_2017 + total_taxi_2017 + total_vistoria_2017]}


# In[56]:


#Transforma o dicionário em um dataframe

df_total_receitas_2017 = pd.DataFrame.from_dict(total_receitas_2017)
df_total_receitas_2017.set_index('Tipo de receita', inplace=True)
df_total_receitas_2017.head(6)


# In[76]:


#Gera um arquivo CSV com os dados do dataframe

df_total_receitas_2017.to_csv('distribuicao_receitas_emdec_2017.csv', encoding='utf-8')


# In[57]:


#Gráfico com a distribuição das receitas em 2017

df_total_receitas_2017.plot(kind='pie', subplots=True)

