import cv2
import os

path = "./dataset/p"
"""
for filename in os.listdir(path):
    if filename.lower().endswith('.png'):
        bmp_path = os.path.join(path, filename)
        
        img = cv2.imread(bmp_path)
        if img is not None:
            jpg_filename = os.path.splitext(filename)[0] + '.jpg'
            jpg_path = os.path.join(path, jpg_filename)
            cv2.imwrite(jpg_path, img)
            print(f'Convertido {bmp_path} a {jpg_path}')
        else:
            print(f'No se pudo cargar la imagen {bmp_path}')
        os.remove(bmp_path)

"""

new_size = (38, 46)  # Cambia este valor al tamaño deseado


# Recorre todos los archivos de la carpeta
for filename in os.listdir(path):
    # Comprueba si el archivo tiene extensión .jpg
    if filename.lower().endswith('.jpg'):
        # Ruta completa del archivo de entrada
        jpg_path = os.path.join(path, filename)
        # Carga la imagen
        img = cv2.imread(jpg_path)
        if img is not None:
            # Redimensiona la imagen
            resized_img = cv2.resize(img, new_size)
            # Ruta completa del archivo de salida
            output_path = os.path.join(path, filename)
            # Guarda la imagen redimensionada
            cv2.imwrite(output_path, resized_img)
            print(f'Redimensionado {jpg_path} y guardado en {output_path}')
        else:
            print(f'No se pudo cargar la imagen {jpg_path}')
