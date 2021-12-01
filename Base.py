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

# 6.Número de personas que ha fallecido
df[df["Recuperado"].str.lower() == "Fallecido".lower()]["Recuperado"].count()

# 7.Ordenar de Mayor a menor por tipo de caso
df['Tipo de contagio'].value_counts()

# 8.Número de departamentos afectados
df['Nombre departamento'].nunique()

# 9.Liste los departamentos afectados(sin repetirlos)
df['Nombre departamento'].unique()

# 10.Ordene de mayor a menor por tipo de atención
df['Tipo de recuperación'].value_counts()

# 11.Liste de mayor a menor los 10 departamentos con mas casos de contagiados
df['Nombre departamento'].value_counts()[:10]

# 12.Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
df[df["Recuperado"].str.lower() == "Fallecido".lower()]
["Nombre departamento"].value_counts()[:10]

# 13.Liste de mayor a menor los 10 departamentos con mas casos de recuperados
df[df["Recuperado"] == "Recuperado"]["Nombre departamento"].value_counts()[:10]

# 14.Liste de mayor a menor los 10 municipios con mas casos de contagiados
df['Nombre municipio'].value_counts()[:10]

# 15.Liste de mayor a menor los 10 municipios con mas casos de fallecidos
df[df["Recuperado"].str.lower() == "Fallecido".lower()]
["Nombre municipio"].value_counts()[:10]

# 16.Liste de mayor a menor los 10 municipios con mas casos de recuperados
df[df["Recuperado"] == "Recuperado"]["Nombre municipio"].value_counts()[:10]

# 17.Liste agrupado por departamento y en orden de Mayor a menor las ciudades
df[["Nombre departamento", " Nombre municipio"]].value_counts()

# 18.Número de Mujeres y hombres contagiados por ciudad por departamento
df[["Nombre departamento", " Nombre municipio", "Sexo"]].value_counts()