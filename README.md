# Análise de Dados de E-commerce

Este projeto utiliza a biblioteca **pandas**, **matplotlib** e **seaborn** para realizar uma análise exploratória dos dados de um e-commerce. Os principais gráficos gerados são listados abaixo, cada um representando aspectos diferentes da distribuição e relação entre variáveis.

## 📊 Gráficos Gerados

### 1️⃣ Histogramas
Os histogramas mostram a distribuição das variáveis **N_Avaliações_MinMax**, **Nota_MinMax** e **Preço_MinMax**. Cada gráfico exibe a frequência de cada valor dentro de um intervalo específico.
![histograma AvaliaçãoMinMax](ht_avaliacaoMinMax.png)
![histograma_NotaMinMax](ht_notaMinMax.png)
![histograma_precoMinMax](ht_notaMinMax.png)
### 2️⃣ Gráficos de Dispersão
- **Relação de avaliações e notas**: Exibe a correlação entre o número de avaliações e a nota dos produtos.
![dispercao_avaliacao_nota](re_avaliacao_notas.png)
- **Relação de preço com notas**: Mostra como o preço dos produtos influencia suas notas.
![dispersao_preco_nota](re_preco_notas.png)
### 3️⃣ Mapa de Calor das Correlações
Este gráfico permite visualizar a relação entre variáveis como **Nota**, **Número de Avaliações**, **Desconto**, **Preço** e outros atributos. A intensidade das cores indica o grau de correlação.
![mapa_calor](mpa_calor.png)
### 4️⃣ Gráfico de Barras
Representa a **divisão de gêneros** entre os produtos disponíveis no e-commerce.
![Grafico_barra-genero](barra_divisao_generos.png)
### 5️⃣ Gráfico de Pizza
Exibe a **distribuição dos gêneros**, indicando a proporção de cada um no conjunto de dados.
![pizza_generos](pizza_genero.png)
### 6️⃣ Gráfico de Densidade
Mostra a distribuição de preços com uma curva de densidade, facilitando a visualização da concentração dos valores.
![densidade_preco](den_preco.png)
### 7️⃣ Gráfico de Regressão
Demonstra a relação entre **desconto** e **nota**, mostrando uma tendência de correlação entre essas variáveis.
![regrecao_desconto_nota](regre_desconto_preco.png)
## 🛠 Tecnologias Utilizadas
- **Python 3.x**
- **pandas**
- **matplotlib**
- **seaborn**

## 🚀 Como Executar o Código
1. Instale as dependências necessárias:
   ```bash
   pip install pandas matplotlib seaborn