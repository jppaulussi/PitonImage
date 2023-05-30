import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carregar a imagem
image = cv2.imread("C:\\temp\\piton\\teste\\errada.jpg")

# Converter para escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar filtro de média para reduzir o ruído
blur_image = cv2.blur(gray_image, (5, 5))

# Aplicar filtro de mediana para reduzir ruído impulsivo (sal e pimenta)
median_image = cv2.medianBlur(gray_image, 5)

# Aplicar filtro de realce de nitidez (unsharp masking)
unsharp_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
unsharp_image = cv2.addWeighted(gray_image, 1.5, unsharp_image, -0.5, 0)

# Exibir as imagens
plt.figure(figsize=(12, 4))

plt.subplot(141)
plt.imshow(image[:, :, ::-1])
plt.title("Imagem Original")
plt.axis('off')

plt.subplot(142)
plt.imshow(unsharp_image, cmap='gray')
plt.title("Realce de Nitidez")
plt.axis('off')

plt.tight_layout()
plt.show()
