Voici une version mise à jour de votre fichier README avec l'ajout d'un tableau comparatif entre les performances Mono-thread et Multi-thread :  

---

# Comparaison des Performances : Mono-Thread vs Multi-Thread  

## Description  
Ce projet compare les performances des systèmes **mono-thread** et **multi-thread** dans le traitement d'images en utilisant Python. Il analyse les temps d'exécution, l'utilisation des ressources (CPU et mémoire) et la réactivité des deux approches.  

## Fonctionnalités  
1. **Traitement d'images avec deux filtres :**  
   - Flou gaussien.  
   - Détection de contours.  
2. **Comparaison des performances :**  
   - Temps d'exécution.  
   - Utilisation du CPU.  
   - Utilisation de la mémoire.  
3. **Génération de graphiques pour visualiser les résultats :**  
   - Temps d'exécution.  
   - Utilisation des ressources (CPU, mémoire).  

## Structure du projet  
```
Projet SEA_Dhafer&Yacine/
├── comparaison.py            # Programme principal
├── traitement_image_mono.py  # Traitement mono-thread
├── traitement_image_multi.py # Traitement multi-thread
├── images/                   # Dossier contenant les images à traiter
├── performance_comparaison.png  # Graphique des performances
├── ressources_comparaison.png   # Graphique des ressources
└── README.md                 # Documentation
```  

## Installation  
1. **Cloner le dépôt :**  
   ```bash
   git clone <URL-du-dépôt>
   cd Projet SEA_Dhafer&Yacine
   ```  
2. **Installer les dépendances Python :**  
   Assurez-vous d'avoir Python 3 et `pip` installés.  
   ```bash
   pip install matplotlib opencv-python psutil
   ```  

## Exécution  
1. Placez vos images dans le dossier `images/`.  
2. Lancez le script principal :  
   ```bash
   python3 comparaison.py
   ```  

## Résultats  
- **`performance_comparaison.png` :** Comparaison des temps d'exécution entre mono-thread et multi-thread.  
- **`ressources_comparaison.png` :** Comparaison de l'utilisation du CPU et de la mémoire.  

## Tableau Comparatif  

| **Critère**             | **Mono-thread**                            | **Multi-thread**                          |
|-------------------------|--------------------------------------------|-------------------------------------------|
| **Exécution**           | Séquentielle (un filtre après l'autre)     | Parallèle (plusieurs filtres en même temps) |
| **Complexité**          | Simple (pas de gestion des threads)        | Moyenne (gestion et synchronisation des threads) |
| **Temps d'exécution**   | Plus long                                  | Potentiellement plus court si plusieurs cœurs sont disponibles |
| **Utilisation CPU (Début)** | Modérée (1 thread actif à la fois)        | Plus élevée (plusieurs threads actifs simultanément) |
| **Utilisation CPU (Fin)**   | Plus stable                              | Peut être instable selon la charge des threads |
| **Utilisation mémoire (Début)** | Faible (1 seule copie de l'image en mémoire) | Moyennement élevée (chaque thread peut avoir sa copie en mémoire) |
| **Utilisation mémoire (Fin)**   | Stable (aucune montée en charge importante) | Peut augmenter temporairement selon le nombre de threads actifs |
| **Efficacité sur petits fichiers** | Très bonne (charge limitée)               | Légèrement moins bonne (threads inutiles sur des fichiers légers) |
| **Efficacité sur gros fichiers**   | Plus lente, dépend d’un seul cœur         | Plus rapide grâce à la distribution de la charge sur plusieurs threads |

## Dépendances  
- Python 3  
- Bibliothèques :  
  - `matplotlib`  
  - `opencv-python`  
  - `psutil`  

## Auteurs  
- **Dhafer BOUTHELJA**  
- **Yacine Hantous**  
