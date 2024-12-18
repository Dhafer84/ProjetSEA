#comparaison.py#
import os
import time
import matplotlib
matplotlib.use('Agg')  # Utiliser un backend sans interface graphique (ce qui évite le crash)
import matplotlib.pyplot as plt
from traitement_image_mono import measure_mono
from traitement_image_multi import measure_multi

if __name__ == "__main__":
    # Liste des images à traiter
    image_paths = [
        "images/image1.jpg",
        "images/image2.jpg",
        "images/image3.jpg",
        "images/image4.jpg"
    ]
    
    output_dir = "images"  # Dossier de sortie
    os.makedirs(output_dir, exist_ok=True)

    # Mesurer les performances et l'utilisation des ressources
    print("Mesure des performances et des ressources :")
    mono_time, mono_cpu_init, mono_cpu_final, mono_mem_init, mono_mem_final = measure_mono(image_paths, output_dir)
    multi_time, multi_cpu_init, multi_cpu_final, multi_mem_init, multi_mem_final = measure_multi(image_paths, output_dir)
    
    # Affichage des résultats
    print(f"Temps Mono-Thread : {mono_time:.2f} secondes")
    print(f"Temps Multi-Thread : {multi_time:.2f} secondes")
    
    # Comparaison du temps d'exécution
    labels = ["Mono-Thread", "Multi-Thread"]
    times = [mono_time, multi_time]
    plt.bar(labels, times, color=['blue', 'green'])
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Comparaison des Performances : Mono vs Multi-Thread")
    
    # Sauvegarder l'image au lieu d'afficher
    plt.savefig("performance_comparaison.png")  # Sauvegarder l'image
    print("Le graphique a été sauvegardé sous 'performance_comparaison.png'.")
    
    # Comparaison des ressources (CPU et Mémoire)
    cpu_usage = [multi_cpu_final - multi_cpu_init, mono_cpu_final - mono_cpu_init]  # Usage du CPU
    memory_usage = [multi_mem_final - multi_mem_init, mono_mem_final - mono_mem_init]  # Usage de la mémoire
    
    plt.figure(figsize=(10, 5))
    
    # Comparaison de l'utilisation CPU
    plt.subplot(1, 2, 1)
    plt.bar(labels, cpu_usage, color=['blue', 'green'])
    plt.ylabel("Utilisation CPU (%)")
    plt.title("Comparaison de l'Utilisation du CPU")
    
    # Comparaison de l'utilisation de la mémoire
    plt.subplot(1, 2, 2)
    plt.bar(labels, memory_usage, color=['blue', 'green'])
    plt.ylabel("Utilisation Mémoire (%)")
    plt.title("Comparaison de l'Utilisation de la Mémoire")
    
    plt.tight_layout()
    # Sauvegarder l'image comparant CPU et mémoire
    plt.savefig("ressources_comparaison.png")
    print("Le graphique des ressources a été sauvegardé sous 'ressources_comparaison.png'.")
