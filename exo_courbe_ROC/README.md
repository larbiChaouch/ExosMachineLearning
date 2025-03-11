# Premier exercice de ROC et AUC
Ce projet explore l'évaluation des modèles de classification en utilisant la courbe ROC (Receiver Operating Characteristic) et l'AUC (Area Under Curve).
L'objectif est de comprendre comment ces métriques permettent d'analyser la performance d'un classificateur binaire.

## 1. Introduction à la courbe ROC et à l'AUC
La courbe ROC est un graphique qui illustre la capacité d'un modèle à distinguer entre deux classes.
Elle représente le taux de vrais positifs (True Positive Rate - TPR) en fonction du taux de faux positifs 
(False Positive Rate - FPR) pour différents seuils de décision.  
L'AUC (Area Under Curve) mesure l'aire sous la courbe ROC.  
Plus l'AUC est proche de 1, meilleur est le modèle.  
Une AUC de 0.5 indique un modèle aléatoire (aucune capacité de discrimination).  

## 2. Données utilisées
Les données suivantes représentent les scores de prédiction d'un modèle pour 10 objets, ainsi que leur classe réelle 
(+ pour positif, - pour négatif) :

| Objet | Score | Classe réelle |
|-------|-------|---------------|
| 1     | 0,95  | +             |
| 2     | 0,93  | +             |
| 3     | 0,87  | -             |
| 4     | 0,85  | +             |
| 5     | 0,83  | -             |
| 6     | 0,80  | -             |
| 7     | 0,76  | -             |
| 8     | 0,53  | +             |
| 9     | 0,43  | -             |
| 10    | 0,25  | +             |

Score : Probabilité estimée par le modèle que l'objet soit positif.  
Classe réelle : Valeur de vérité terrain (+ ou -).

## 3. Méthodologie
### - Calcul du TPR et du FPR :
Le modèle applique un seuil de décision pour classifier les objets en positifs ou négatifs.
En modifiant ce seuil, on obtient différentes valeurs de FPR et TPR.

### - Construction de la courbe ROC :
On trace le FPR (axe des abscisses) et le TPR (axe des ordonnées) pour plusieurs seuils.
Une ligne diagonale (y = x) représente un modèle aléatoire.
### - Calcul de l'AUC :

L’aire sous la courbe ROC est intégrée pour obtenir une mesure globale de performance.

## 4. Interprétation des résultats
Un modèle parfait aurait une AUC = 1 (pas de faux positifs).
Un modèle aléatoire aurait AUC = 0.5.
Plus l'AUC est élevée, meilleure est la capacité du modèle à différencier les classes.

## 5. Résultats obtenus
Le script génère une courbe ROC avec l'AUC calculée et l'enregistre sous ``Graphes/roc_auc.png``.

Visualisation :  
Pour ouvrir le graphe sur macOS :
```bash
open Graphes/roc_auc.png
```

sur Linux : 
```bash
xdg-open Graphes/roc_auc.png
```

## 6. Conclusion
- La courbe ROC est un outil puissant pour comparer différents modèles.  
- L’AUC fournit une mesure objective de la performance.  
- Un bon modèle doit maximiser l’AUC tout en minimisant les faux positifs.