# Projet MSPR TPRE813 - Analyse électorale et socio-économique en Île-de-France

Ce projet vise à analyser les résultats électoraux et les indicateurs socio-économiques dans les départements de l’Île-de-France. Il utilise des données issues de fichiers Excel pour produire des visualisations permettant de mieux comprendre les liens entre certaines variables sociales et les résultats électoraux.

## Fichiers nécessaires

- `Resultat par dep avec vainqueur_societal.xlsx` : données électorales par département, incluant le vainqueur.
- `Prepa_correlation_par_departement_societal.xlsx` : données socio-économiques par département.

## Dépendances

Les bibliothèques Python suivantes sont nécessaires :

```bash
pip install pandas matplotlib seaborn numpy plotly geopandas
```

## Étapes principales du script

1. **Chargement des données** depuis les deux fichiers Excel.
2. **Filtrage** des départements de la région Île-de-France.
3. **Nettoyage** et fusion des deux jeux de données.
4. **Visualisations** :
   - `pairplot_indicateurs.png` : Pairplot des indicateurs selon le vainqueur.
   - `pauvrete_vainqueur.png` : Barplot du taux de pauvreté par département et vainqueur.
   - `salaire_violinplot.png` : Violinplot du salaire net moyen par vainqueur.
5. **Carte interactive** : `carte_pauvrete_idf.html` représentant le taux de pauvreté par département.

## Sorties générées

- `pairplot_indicateurs.png`
- `pauvrete_vainqueur.png`
- `salaire_violinplot.png`
- `carte_pauvrete_idf.html`

Projet réalisé dans le cadre de la MSPR TPRE813.