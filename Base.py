import pandas as pd
df = pd.read_csv('covid_22_noviembre.csv', sep=',', header=0)
df.head()

# 1.Número de casos de Contagiados en el País.
df.count()["ID de caso"]

# 2.Número de Municipios Afectados
df['Nombre municipio'].nunique()


