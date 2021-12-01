import pandas as pd
df = pd.read_csv('covid_22_noviembre.csv', sep=',', header=0)
df.head()

# 1.Número de casos de Contagiados en el País.
df.count()["ID de caso"]

# 2.Número de Municipios Afectados
df['Nombre municipio'].nunique()

# 3.Liste los municipios afectados (sin repetirlos)
df['Nombre municipio'].unique()

# 4. Número de personas que se encuentran en atención en casa
df[df["Ubicación del caso"] == "casa"]["Ubicación del caso"].count()


# 5.Número de personas que se encuentran recuperados
df[df["Recuperado"] == "Recuperado"]["Recuperado"].count()
