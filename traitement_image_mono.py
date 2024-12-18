#traitement_image_mono
import cv2
import time
import os
import psutil  # Pour mesurer les ressources

def apply_filters_mono(image_path, output_dir):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"L'image {image_path} n'a pas pu être chargée.")
    
    # Appliquer un flou gaussien
    blurred = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imwrite(f"{output_dir}/blurred_{os.path.basename(image_path)}", blurred)

    # Appliquer la détection de contours
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    cv2.imwrite(f"{output_dir}/edges_{os.path.basename(image_path)}", edges)

# Mesure du temps d'exécution et des ressources pour la version Mono-thread
def measure_mono(image_paths, output_dir):
    start_time = time.time()
    initial_cpu = psutil.cpu_percent(interval=0.1)
    initial_memory = psutil.virtual_memory().percent
    
    for image_path in image_paths:
        apply_filters_mono(image_path, output_dir)
    
    exec_time = time.time() - start_time
    final_cpu = psutil.cpu_percent(interval=0.1)
    final_memory = psutil.virtual_memory().percent
    
    return exec_time, initial_cpu, final_cpu, initial_memory, final_memory

    
