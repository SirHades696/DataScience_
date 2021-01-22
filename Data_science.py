import pandas
import matplotlib.pyplot as plt
from count_goals import count_goals as fn

path = __file__.split("Data_science.py")
data_path = path[0] + "dataset\\world_cups.xlsx"

world_cups = pandas.read_excel(data_path,sheet_name="world_cups")
matches = pandas.read_excel(data_path, sheet_name="matches")
players = pandas.read_excel(data_path, sheet_name="players")

"""
Ejercicios para realizar:
1.	¿De cuántos mundiales se tiene información?
2.	Obtener el nombre completo de cada mundial. Nombre + Anio
3.	Países que campeonaron de locales.
4.	Partidos del mundial con más goles.
5.	Goles promedio por partido para cada mundial.
6.	Goleador de cada mundial
7.	Gráfico de Barras con la cantidad de goles por mundial.
"""
# Ejercicios número 1:
print("Numero total de mundiales: " + str(world_cups.shape[0]))
print("#####################################################")

# Ejercicio número 2:
world_cups["Year"] = world_cups["Year"].astype(str) #Cambiando el tipo de dato para que pueda ser concatenado
world_cups["Full_name_wc"] = world_cups["Country"] + " " + world_cups["Year"]
print(world_cups.get(["Full_name_wc"]))
print("#####################################################")

# Ejercicio número 3:
locales = world_cups.loc[world_cups['Country'] == world_cups['Winner']]
print(locales)
print("#####################################################")

# Ejercicio número 4:
matches["Total Goals"] = matches["Home Team Goals"] + matches["Away Team Goals"]
goals = matches.get(["Home Team Name", "Away Team Name", "Home Team Goals", "Away Team Goals", "Total Goals"])
print(goals.sort_values(by = 'Total Goals', ascending= False))
print("#####################################################")

#Ejercicio número 5:
world_cups['AVG Goals'] = world_cups['GoalsScored'] / world_cups['MatchesPlayed']
avg_goals = world_cups.get(['Country', 'Year', 'AVG Goals'])
print(avg_goals.head())
print("#####################################################")

#Ejercicio número 6:
scorer = players.dropna(subset=["Event"])
scorer['All Goals'] = scorer['Event'].apply(fn)
print(scorer.get(['Player Name','All Goals']).groupby('Player Name').sum().sort_values(by = 'All Goals', ascending= False).head(10))
print("#####################################################")

#Ejercicio número 7:
world_cups.plot(kind = 'barh', x = 'Year', y ='GoalsScored')
plt.show()