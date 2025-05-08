# Análise de Dados de E-commerce

Este projeto utiliza a biblioteca **pandas**, **matplotlib** e **seaborn** para realizar uma análise exploratória dos dados de um e-commerce. Os principais gráficos gerados são listados abaixo, cada um representando aspectos diferentes da distribuição e relação entre variáveis.

## 📊 Gráficos Gerados

### 1️⃣ Histogramas
Os histogramas mostram a distribuição das variáveis **N_Avaliações_MinMax**, **Nota_MinMax** e **Preço_MinMax**. Cada gráfico exibe a frequência de cada valor dentro de um intervalo específico.
![histograma AvaliaçãoMinMax](https://github.com/user-attachments/assets/65cac7ee-7041-4b8b-b1c8-2edbe462b6a3)
![histograma_NotaMinMax](https://github.com/user-attachments/assets/ffacaac2-9dcd-4b57-ac59-b19a86d06639)
![histograma_precoMinMax](https://github.com/user-attachments/assets/a09cd2ac-2116-42a0-b944-bb7c143ac59c)
### 2️⃣ Gráficos de Dispersão
- **Relação de avaliações e notas**: Exibe a correlação entre o número de avaliações e a nota dos produtos.
![dispercao_avaliacao_nota](https://github.com/user-attachments/assets/ce4aabb3-9b85-4539-a0db-c559f2596fd3)
- **Relação de preço com notas**: Mostra como o preço dos produtos influencia suas notas.
![dispersao_preco_nota](https://github.com/user-attachments/assets/0b0bf9c6-e4b9-4299-941b-81114fd8f4aa)
### 3️⃣ Mapa de Calor das Correlações
Este gráfico permite visualizar a relação entre variáveis como **Nota**, **Número de Avaliações**, **Desconto**, **Preço** e outros atributos. A intensidade das cores indica o grau de correlação.
![mapa_calor](https://github.com/user-attachments/assets/f26d922e-d571-4a92-9cf0-3942f4bee994)
### 4️⃣ Gráfico de Barras
Representa a **divisão de gêneros** entre os produtos disponíveis no e-commerce.
![Grafico_barra-genero](https://github.com/user-attachments/assets/df9bb622-0c35-46f6-b5a7-7844306fbc9b)
### 5️⃣ Gráfico de Pizza
Exibe a **distribuição dos gêneros**, indicando a proporção de cada um no conjunto de dados.
![pizza_generos](https://github.com/user-attachments/assets/1dec5857-ab41-4ad0-ae6f-7443914396c7)
### 6️⃣ Gráfico de Densidade
Mostra a distribuição de preços com uma curva de densidade, facilitando a visualização da concentração dos valores.
![densidade_preco](https://github.com/user-attachments/assets/6b4a6069-28e7-4566-8bad-be09be3c714d)
### 7️⃣ Gráfico de Regressão
Demonstra a relação entre **desconto** e **nota**, mostrando uma tendência de correlação entre essas variáveis.
![regrecao_desconto_nota](https://github.com/user-attachments/assets/cf571d32-92cd-44e2-993e-2813c039d03c)
## 🛠 Tecnologias Utilizadas
- **Python 3.x**
- **pandas**
- **matplotlib**
- **seaborn**

## 🚀 Como Executar o Código
1. Instale as dependências necessárias:
   ```bash
   pip install pandas matplotlib seaborn
