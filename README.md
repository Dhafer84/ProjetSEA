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

## Dépendances  
- Python 3  
- Bibliothèques :  
  - `matplotlib`  
  - `opencv-python`  
  - `psutil`  

## Auteurs  
- **Dhafer BOUTHELJA**  
- **Yacine Hantous**  
