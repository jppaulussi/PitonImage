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
