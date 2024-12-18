#traitement_image_multi.py
import os
import time  # Importation du module time
import cv2
import threading
import psutil  # Utilisation de psutil pour mesurer les ressources (CPU, Mémoire)

# Fonction pour appliquer des filtres à une image (version Mono-Thread)
def apply_blur(image, output_path):
    blurred = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imwrite(output_path, blurred)

def apply_edges(image, output_path):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    cv2.imwrite(output_path, edges)

# Mesure du temps d'exécution et des ressources pour la version Multi-thread
def measure_multi(image_paths, output_dir):
    threads = []
    start_time = time.time()
    initial_cpu = psutil.cpu_percent(interval=0.1)
    initial_memory = psutil.virtual_memory().percent
    
    for image_path in image_paths:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"L'image {image_path} n'a pas pu être chargée.")
        
        # Création des threads pour appliquer les filtres
        thread1 = threading.Thread(target=apply_blur, args=(image, f"{output_dir}/blurred_{os.path.basename(image_path)}"))
        thread2 = threading.Thread(target=apply_edges, args=(image, f"{output_dir}/edges_{os.path.basename(image_path)}"))
        
        thread1.start()
        thread2.start()
        
        threads.append(thread1)
        threads.append(thread2)
    
    # Attendre la fin de tous les threads
    for thread in threads:
        thread.join()
    
    exec_time = time.time() - start_time
    final_cpu = psutil.cpu_percent(interval=0.1)
    final_memory = psutil.virtual_memory().percent
    
    return exec_time, initial_cpu, final_cpu, initial_memory, final_memory


