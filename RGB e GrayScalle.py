import cv2
from matplotlib import pyplot as plt

# Lista de caminhos das imagens
IMAGE_CONTENTS = ["C:\\temp\\piton\\teste\\errada.jpg"]

for image_path in IMAGE_CONTENTS:
    img_rgb = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
    img_gray = cv2.imread(image_path, 0)

    # Exibe imagem RGB grayscale
    plt.figure(figsize=(8, 4))
    plt.subplot(121)
    plt.imshow(img_rgb)
    plt.title("Imagem - RGB")
    plt.axis('off')

    plt.subplot(122)
    plt.imshow(img_gray, cmap='gray')
    plt.title("Imagem - Grayscale")
    plt.axis('off')

    plt.tight_layout()
    plt.show()