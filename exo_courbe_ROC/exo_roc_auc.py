import matplotlib.pyplot as plt
import numpy as np
import os

from sklearn.metrics import roc_curve, auc

# le nom du dossier là ou on va enregistrer notre graphe
dir_graph = "./Graphes"
# le chemin du dossier
path_dir_graph = os.path.join(dir_graph)
# si le dossier n'est pas encore là, on créé le dossier
if not os.path.exists(path_dir_graph):
    os.makedirs(path_dir_graph)
# définir la long, largeur du graphe en pixel
plt.figure(figsize=(10,10))
# définir la grille
plt.grid(linestyle='--', color='lightgrey')
# mettre du titre pour le graphe
plt.title("ROC et AUC", fontsize=30, color='r', fontweight='bold', fontname='Times New Roman')
# tracer la ligne du hasard (y = x)
plt.plot([0, 1], [0, 1], linestyle='-', color='green', linewidth=3,label='Hasard')
plt.legend(loc="lower right")
# ajustement de la grille
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])

# Données
scores = np.array([0.95, 0.93, 0.87, 0.85, 0.83, 0.80, 0.76, 0.53, 0.43, 0.25])
classes_reelles = np.array([1, 1, 0, 1, 0, 0, 0, 1, 0, 1])  # + → 1, - → 0

# calcul de fpr rt tpr
fpr, tpr, thresholds = roc_curve(classes_reelles, scores)

# calcul du auc
roc_auc = auc(fpr, tpr)

# placer le fpr sur l'axe des abscisses et le tpr sur l'axe des ordonnées
plt.plot(fpr, tpr, lw=5, color = "blue")

plt.xlabel("False Positive Rate", fontsize=20, fontweight='bold', fontname='Courier New')
plt.ylabel("True Positive Rate", fontsize=20, fontweight='bold', fontname='Courier New')
plt.text(0.88,0.07, f"AUC {roc_auc:.2f}")
plt.savefig(path_dir_graph + "/roc_auc.png")
plt.show()