# Projet MSPR TPRE813 - Analyse électorale et socio-économique en Île-de-France

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import geopandas as gpd

# Chargement des fichiers
df_election = pd.read_excel("Resultat par dep avec vainqueur_societal.xlsx")
df_socio = pd.read_excel("Prepa_correlation_par_departement_societal.xlsx")

# Liste des départements de l'Île-de-France
idf_departements = ['Paris', 'Seine-et-Marne', 'Yvelines', 'Essonne', 'Hauts-de-Seine',
                    'Seine-Saint-Denis', 'Val-de-Marne', "Val-d'Oise"]

# Filtrage des données
df_election_idf = df_election[df_election['libelle_departement'].isin(idf_departements)].copy()
df_socio_idf = df_socio[df_socio['libelle_departement'].isin(idf_departements)].copy()

# Suppression de doublons éventuels
df_election_idf = df_election_idf.drop_duplicates(subset=['libelle_departement'])
df_socio_idf = df_socio_idf.drop_duplicates(subset=['libelle_departement'])

# Fusion des deux fichiers
df = pd.merge(df_election_idf, df_socio_idf, on='libelle_departement', suffixes=('_el', '_soc'))

# Visualisations descriptives :

# 1. Pairplot - indicateurs croisés par vainqueur
sns.pairplot(df, hue="nomvainqueur", vars=['TxPeuDiplomes_el', 'SalaireNetMoyen_el', 'TxChomageAnnuel_el', 'TxPauvrete_el'])
plt.suptitle("Pairplot des indicateurs selon le vainqueur", y=1.02)
plt.tight_layout()
plt.savefig("pairplot_indicateurs.png")
plt.close()

# 2. Barplot - Taux de pauvreté par département
plt.figure(figsize=(10, 6))
sns.barplot(x='libelle_departement', y='TxPauvrete_el', hue='nomvainqueur', data=df)
plt.title("Taux de pauvreté par département et vainqueur")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("pauvrete_vainqueur.png")
plt.close()

# 3. Violinplot - Salaire net moyen selon le vainqueur
plt.figure(figsize=(8, 5))
sns.violinplot(x='nomvainqueur', y='SalaireNetMoyen_el', data=df)
plt.title("Salaire net moyen par vainqueur")
plt.tight_layout()
plt.savefig("salaire_violinplot.png")
plt.close()

# Carte interactive :

idf_df = df[['libelle_departement', 'TxPauvrete_el']].copy()
idf_df['code_insee'] = ['75', '77', '78', '91', '92', '93', '94', '95']

fig = px.choropleth(
    idf_df,
    geojson="https://france-geojson.gregoiredavid.fr/repo/departements.geojson",
    featureidkey="properties.code",
    locations="code_insee",
    color="TxPauvrete_el",
    hover_name="libelle_departement",
    color_continuous_scale="Reds",
    title="Carte des départements d’Île-de-France - Taux de pauvreté"
)
fig.update_geos(fitbounds="locations", visible=False)
fig.write_html("carte_pauvrete_idf.html")

# Résumé
print("\nGraphiques générés :")
print("- pairplot_indicateurs.png")
print("- pauvrete_vainqueur.png")
print("- salaire_violinplot.png")
print("Carte interactive : carte_pauvrete_idf.html")
