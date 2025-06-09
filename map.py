import pandas as pd
import plotly.express as px

# Carregar o CSV
df = pd.read_csv("Treemap_info.csv")

# Criar coluna "Label_Final" que só usa Subcategoria se existir, senão evita nível extra
df["Tem_Subcategoria"] = df["Subcategoria"].notna()
df["Subcategoria"] = df["Subcategoria"].fillna("")
df["Label_Final"] = df.apply(
    lambda row: row["Subcategoria"] if row["Tem_Subcategoria"] else row["Categoria"],
    axis=1
)

# Criar Treemap
fig = px.treemap(
    df,
    path=["Projeto", "Categoria", "Label_Final"],
    values="Peso (%)",
    color="Conclusao (%)",
    color_continuous_scale=[(0.0, "red"), (0.5, "yellow"), (1.0, "green")]
)

# Estilo
fig.update_traces(
    textinfo="label+percent parent+value",
    textfont=dict(size=18, color="black")
)

# Exibir
fig.show()
