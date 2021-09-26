#!/usr/bin/env python
# coding: utf-8

# # Médiathèque José Cabanis

#    Les amoureux du cinéma déplorent la disparition de bons nombre de vidéos store au fil des années.La Vod, le streaming ont eut raison des soirées films en familles avec un dvd emprunté chaque semaines. Les mediathèques apparaissent alors comme de bonnes alternatives, l'emprunt de films y rencontre un grand succès. 
# Nous nous intérésserons ici a la médiathèque José Cabanis situé a Toulouse.
#    
#    Les données fournies sont elles toutes cohérentes?
#    Quelles années ont enregistrés le plus d'emprunts?
#    Quelles sont les villes des sociétés de production qui rencontrent le plus de succès?
#    Quels films peuvent être qualifié de best seller?
#     
#     
# 

# ![](media.jpg)

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import os


# In[2]:


movies= pd.read_csv("toulouse_data.csv",sep=";")


# # Description du Data Frame

# In[3]:


movies.head()


# In[4]:


movies.shape


# In[5]:


movies.info()


# In[6]:


movies.describe()


# # Nettoyage Des données

# Affichons un df avec toutes les lignes qui ont au moins une valeur manquante

# In[7]:


val_manquantes = movies[movies.isnull().any(axis=1)]
val_manquantes


# Faisons disparaitre ces valeurs manquantes

# In[8]:


movies.dropna(inplace=True)


# In[9]:


movies.isnull().any()


# Renommons les colonnes pour plus de clarté

# In[10]:


mov=movies.rename(columns = {'Annee': 'Année', 'nbre_de_prets': 'Qtité de pret','titre':'Titre','editeur':'Editeur','indice':'Indice','bib':'Bibliothèque','cote':'Genre'})
mov


# Supprimons les colonnes peu intéressantes.
# 
# 

# In[11]:


mm= mov.drop(columns=["cat_1","cat_2"])


# Classons le tableau par année de 2011 à 2020

# In[12]:


movies_clean  = mm.set_index('Année')


# In[13]:


movies_clean.sort_index(inplace=True) 


# In[14]:


movies_clean


# Combien de livres empruntés par années?

# In[15]:


movies_clean.groupby('Année')['Qtité de pret'].sum().sort_values(ascending=False)


# Illustration avec un diagramme en barre

# In[16]:


movies_clean.groupby('Année')["Qtité de pret"].sum().plot.bar(figsize=(10,8))
plt.title("Quantité de livres empruntés")


# De quelle villes viennent les société de productions de ces films.

# In[17]:


movies_clean['Editeur'].unique()


# In[18]:


ville_production = movies_clean['Editeur']


# In[19]:


'Paris : France Télévision Distribution [éd.], 2001.'.split(':')[0].strip()


# Créons une boucle afin de n'afficher que le nom des villes dans un nouvelle colonne nommé ville_prod

# In[20]:


def get_ville(ville_production):
  return ville_production.split(':')[0].strip()


# In[21]:


movies_clean['ville_prod']=movies_clean['Editeur'].apply(get_ville)


# In[22]:


movies_clean


# In[23]:


movies_clean.groupby('ville_prod').sum()["Qtité de pret"].sort_values(ascending=False)


# Les sociétés sont très majoritairement parisienne, en témoigne le diagramme ci dessous.

# In[24]:


movies_clean.groupby('ville_prod')["Qtité de pret"].sum().plot.bar(figsize=(10,8))
plt.title("Ville d'edition des films empruntés")


# # Le plus interéssant désormais! Quel film a été le plus emprunté en presque 10 ans ?

# In[25]:


best_seller= movies_clean.groupby('Titre')["Qtité de pret"].sum().sort_values(ascending=False)


# In[26]:


best_seller


# ![](burton.jpg)

# Alice au pays des merveilles est devant. Le film est sortit en 2010 cela fait donc 10 ans qu'il est disponible, il a donc une grande longévité.Peter Pan et la Belle et le Clochard complète le podium. On remarque tout de meme que les films familiaux ne laissent pas beaucoup de place en tete du classement!
