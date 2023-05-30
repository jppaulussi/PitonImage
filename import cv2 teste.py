import imageios
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

IMAGE_CONTENT = ["C:\\temp\\piton\\teste\\errada.jpg", "C:\\temp\\piton\\teste\\outra.jpg"]

# Função para verificar a definição/qualidade da imagem
def identificar_problema(image_path):
    try:
        # Carregar a imagem e converter para escala de cinza
        image = Image.open(image_path).convert("L")
        image_array = np.array(image)
        min_val = np.min(image_array)
        max_val = np.max(image_array)
        hist = np.histogram(image_array, bins=256, range=(0, 255))[0]

        # Verificar os problemas
        problemas = []
        if min_val < 50:
            problemas.append("Muito escura")
        if max_val > 200:
            problemas.append("Muito clara")
        if np.max(hist) < 100:
            problemas.append("Baixo contraste")

        if len(problemas) == 0:
            return "Sem problemas aparentes"
        else:
            return ", ".join(problemas)
    except Exception as e:
        return f"Erro ao processar a imagem: {str(e)}"

# Loop para processar cada imagem
for image_path in IMAGE_CONTENT:
    problema = identificar_problema(image_path)

    # Exibir a imagem e descrição dos problemas
    plt.figure(figsize=(6, 4))
    image = imageio.imread(image_path)
    plt.imshow(image)
    plt.title(f"Imagem - {problema}")
    plt.axis('off')
    plt.show()

