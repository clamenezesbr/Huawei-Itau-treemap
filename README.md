# 📊 Visualizador de Progresso do Projeto Huawei - Itaú

Este projeto tem como objetivo **visualizar de forma clara e interativa o progresso das atividades relacionadas ao projeto de migração em nuvem da Huawei com o banco Itaú**. A ferramenta utiliza dados estruturados em planilhas Excel e os transforma em gráficos de *Treemap*, permitindo uma análise detalhada do andamento por projeto, categoria e subcategoria.

## 🔍 Funcionalidades

- Visualização em treemap com 3 níveis hierárquicos: Projeto → Categoria → Subcategoria (ou Categoria diretamente, se não houver subcategoria).
- Cores baseadas no percentual de conclusão, com gradiente de vermelho (0%) a verde (100%).
- Tamanhos dos blocos proporcionais ao peso (%) de cada atividade.
- Labels dinâmicos, evitando níveis desnecessários quando não há subcategoria.

## 💼 Contexto

Este projeto foi desenvolvido para dar suporte à equipe de *Professional Services & Delivery* da Huawei no acompanhamento do progresso do projeto de migração em nuvem para o cliente Itaú. A ferramenta permite uma **tomada de decisão mais ágil e estratégica**, baseada em dados atualizados diretamente de uma planilha Excel.

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas**: para leitura e manipulação de dados.
- **Plotly Express**: para criação do gráfico Treemap interativo.
- **Excel (.csv)**: como fonte principal dos dados de progresso.

## 🧠 Como Funciona

1. Os dados são mantidos em uma planilha Excel exportada como `.csv` (ex: `Treemap_info.csv`).
2. O script em Python:
   - Carrega os dados usando o `pandas`.
   - Cria uma lógica para evitar subcategorias vazias.
   - Gera um gráfico Treemap com base nos pesos e percentuais de conclusão.
   - Aplica um gradiente de cores para indicar o nível de progresso.
3. O gráfico é exibido de forma interativa no navegador.

![TreeMap](https://i.ibb.co/rGbPDKkg/Map2.png)
