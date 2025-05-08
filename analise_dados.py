import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head())

# Histograma
cols = ['N_Avaliações_MinMax', 'Nota_MinMax', 'Preço_MinMax']

for col in cols:
    plt.figure(figsize=(10, 6))
    plt.hist(df[col], bins=30, color='skyblue', edgecolor='black')
    plt.title(f'Histograma de {col}')
    plt.xlabel(col)
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.show()

# Dispersão
plt.hexbin(df['Nota'], df['N_Avaliações'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro da bin')
plt.xlabel('Notas')
plt.ylabel('Avaliações')
plt.title('Realação de avaliações e notas')
plt.show()

plt.hexbin(df['Preço'], df['Nota'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro da bin')
plt.xlabel('Preço')
plt.ylabel('Nota')
plt.title('Relação de preço com notas')
plt.show()

# Mapa de calor Hearmap
corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos_Cod', 'Marca_Cod', 'Temporada_Cod', 'Material_Freq']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de calor das correlações')
plt.show()

# Gráfico de barras
plt.figure(figsize=(10, 8))
df['Gênero'].value_counts().plot(kind='bar', color='#1f56ed')
plt.title('Divisão de gêneros')
plt.xlabel("Gêneros")
plt.ylabel("Quantidade")
plt.show()

# Gráfico pizza
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values

percentual = (y / y.sum()) * 100
x_f = x[percentual >= 2]
y_f = y[percentual >= 2]

plt.figure(figsize=(10, 8))
plt.pie(y_f, labels=x_f, autopct='%.2f%%', startangle=90)
plt.title('Distribuição de gêneros')
plt.legend(title="Gêneros", loc="lower right")
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'], fill=True, color='#db1446')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.title('Densidade de preço')
plt.show()

# Gráfico de regressão
sns.regplot(x='Desconto', y='Nota', data=df, color='#32db14', scatter_kws={'alpha':0.2, 'color':"#c97a0a"})
plt.title('Regressão de desconto para Notas')
plt.xlabel('Desconto')
plt.ylabel('Nota')
plt.show()
