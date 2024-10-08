# %%
import pandas as pd
import matplotlib as plt

# %%
# Filtrando a base de dados para conter apenas os feminicídios
df = pd.read_csv('BD_SINESP_2015-2024.csv')
feminicidios = df[df['evento'].str.contains('Feminicídio', case=False, na=False)]
feminicidios.to_csv('feminicidios_filtrados.csv', index=False)

print("Nova base de dados salva como 'feminicidios_filtrados.csv'")

# %%
df = pd.read_csv('feminicidios_filtrados.csv')

# %%
media = df['feminino'].mean()
mediana = df['feminino'].median()
desvio_padrao = df['feminino'].std()

print(f'Média: {media}')
print(f'Mediana: {mediana}')
print(f'Desvio Padrão: {desvio_padrao}')

# %%
ano_especifico = '2024'
df['data_referencia'] = pd.to_datetime(df['data_referencia'])
df_filtrado = df[df['data_referencia'].dt.year == int(ano_especifico)]
resultado = df_filtrado.groupby('uf')['feminino'].sum().reset_index()
print(resultado)

# %%
data_especifica = '2017-01-01' 
df_filtrado = df[df['data_referencia'] == data_especifica]
resultado = df_filtrado.groupby('uf')['feminino'].sum().reset_index()
print(resultado)
# %%
df['data_referencia'] = pd.to_datetime(df['data_referencia'])

df.groupby(df['data_referencia'].dt.month)['feminino'].sum().plot(kind='line')

plt.xlabel('Mês')
plt.ylabel('Número de Vítimas Femininas')
plt.title('Número de Feminicídios por Mês')
plt.grid(True)
plt.show()

# %%
df.groupby(df['data_referencia'].dt.year)['feminino'].sum().plot(kind='line')

plt.xlabel('Ano')
plt.ylabel('Número de Vítimas Femininas')
plt.title('Número de Feminicídios por Ano')
plt.grid(True)
plt.show()