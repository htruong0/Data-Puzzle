import pandas as pd

countries = ['Guinea', 'Iran', 'Trinidad and Tobago', 'Honduras', 'Lebanon',
             'Ethiopia', 'Niger', 'Afghanistan', 'India', 'American Samoa',
             'Cuba', 'Gabon', 'Nicaragua', 'Channel Islands', 'Martinique']

country_pop = pd.read_csv('https://raw.githubusercontent.com/hyperc54/data-puzzles-assets/master/misc/earth/population_by_country.csv')
country_surface = pd.read_csv('https://raw.githubusercontent.com/hyperc54/data-puzzles-assets/master/misc/earth/surface_by_country.csv')

df = country_pop.merge(country_surface)
df["Density"] = df["Population (2020)"] / df["Land Area (Km²)"]
df = df[df["Country (or dependency)"].isin(countries)]
names = df.sort_values(by="Density", ascending=False)["Country (or dependency)"].apply(lambda x: x[0])
message = "".join(names)
print(message)