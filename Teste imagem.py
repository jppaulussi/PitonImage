"""""
import cv2
import os
import cv2

def enhance_image(image_path, save_path):
    # Carrega a imagem de origem
    img = cv2.imread(image_path)

    # Verifica se a imagem foi carregada corretamente
    if img is not None:
        # Realiza o processamento da imagem aqui
        equalized_image = cv2.equalizeHist(img)

        # Salva a imagem processada no diretório especificado
        cv2.imwrite(save_path, equalized_image)
    else:
        print("Erro ao carregar a imagem de origem.")

# Exemplo de uso
image_path = "C:\\Users\\fe540\\Documents\\Facul\\teste 2\\foto"
save_path = "C:\\Users\\fe540\\Documents\\Facul\\destino"
enhance_image(image_path, save_path)
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregar a imagem
image = cv2.imread("C:\\temp\\piton\\teste\\errada.jpg")

# Converter a imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Definir o kernel para as operações morfológicas
kernel_size = 3
kernel = np.ones((kernel_size, kernel_size), np.uint8)

# Aplicar a operação de fechamento
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Aplicar a operação de abertura
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

# Exibir as imagens

# Imagem original em RGB
plt.subplot(221), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original - RGB')
plt.axis('off')

# Imagem original em grayscale
plt.subplot(222), plt.imshow(gray, cmap='gray')
plt.title('Imagem Original - Grayscale')
plt.axis('off')

# Imagem após fechamento em RGB
plt.subplot(223), plt.imshow(cv2.cvtColor(closing, cv2.COLOR_BGR2RGB))
plt.title('Imagem Após Fechamento - RGB')
plt.axis('off')

# Imagem após fechamento em grayscale
plt.subplot(224), plt.imshow(closing, cmap='gray')
plt.title('Imagem Após Fechamento - Grayscale')
plt.axis('off')

# Exibir as imagens
plt.tight_layout()
plt.show()
