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

# 19.promedio de edad de contagiados x hombre y mujeres x ciudad x departamento
promCiudad = df.groupby
(["Nombre departamento", "Nombre municipio", "Sexo"]).Edad.mean()
print("Punto 19")
print(promCiudad)
print()

promCiudad = df.groupby
(['Nombre departamento', 'Nombre municipio', 'Sexo']).Edad.mean()
print("Punto 19")
print(promCiudad)
print()

# 20.Liste de mayor a menor el número de contagiados por país de procedencia
df['Nombre del país'].value_counts()[:10]

# 21.Liste de mayor a menor las fechas donde se presentaron mas contagios
fechaContagios = df.groupby
("Fecha de diagnóstico").size().sort_values(ascending=False)
print("Punto 21")
print(fechaContagios)
print()

fechaContagios = df.groupby
("Fecha de diagnóstico").size().sort_values(ascending=False)
print("Punto 21")
print(fechaContagios)
print()

# 22.Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia
tasaMor = (len(df[df['Ubicación del caso'] == 'Fallecido']) / len(df)) * 100
tasaRec = (len(df[df['Recuperado'] == 'Recuperado']) / len(df)) * 100
print("Punto 22")
print(tasaMor)
print(tasaRec)

print("Punto 22")
print(tasaMor)
print(tasaRec)
print()

# 23.Liste la tasa de mortalidad y recuperación que tiene cada departamento
tasaMorDept = (df[df['Ubicación del caso'] == 'Fallecido'].groupby
               ('Nombre departamento').size().sort_values
               (ascending=False)
               / df[df['Ubicación del caso'] == 'Fallecido'].groupby
               ('Nombre departamento').size().sort_values
               (ascending=False).sum()) * 100
tasaRecDept = (df[df['Recuperado'] == 'Recuperado'].groupby
               ('Nombre departamento').size().sort_values
               (ascending=False) / df[df['Recuperado'] == 'Recuperado'].groupby
               ('Nombre departamento').size().sort_values
               (ascending=False).sum()) * 100
print("Punto 23")
print(tasaMorDept)
print(tasaRecDept)
print()

print("Punto 23")
print(tasaMorDept)
print(tasaRecDept)
print()
