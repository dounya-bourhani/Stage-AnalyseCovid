import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Prédiction des cas de covid en Random Forest

# On récupère le jeu de données
series = pd.read_csv("C:/Users/bourh/OneDrive/Bureau/CoursL3/Stage/Stage-AnalyseCovid/Classeur1.csv", sep=";", header=0, index_col=0)

X = series[['code', 'nom', 'deces', 'guerisons', 'source']]
y = series['cas']

print(X)
