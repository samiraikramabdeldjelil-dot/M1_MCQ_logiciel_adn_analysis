#abdeldjelil samira ikram,master 1 Microbiology and quality control,10/12/2025
#dib merwa
#tharaoui hanene
#belamri merwa
#messaoudi fatima
#dali youcef ines

import pandas as pd

# Données : Séquences ADN, Longueur , Pourcentage de GC
data = {  
    "Séquence": ["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"]
    "Longueur": [11, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}
# Création d'un DataFrame (tableau pandas)
df = pd.DataFrame(data)
print("**************** Creattion et affichage ****************","\n")

# Affichage du tableau
print("Tableau des séquences ADN :", "\n")
print(df, "\n" "\n") 
                 
