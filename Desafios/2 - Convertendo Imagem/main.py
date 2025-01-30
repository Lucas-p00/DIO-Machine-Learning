import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para converter imagem para níveis de cinza
def rgb_to_grayscale(image):
    grayscale = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r, g, b = image[i, j]
            grayscale[i, j] = int(0.299 * r + 0.587 * g + 0.114 * b)
    return grayscale

# Função para converter imagem para binário
def grayscale_to_binary(grayscale, threshold=128):
    binary = np.zeros_like(grayscale, dtype=np.uint8)
    for i in range(grayscale.shape[0]):
        for j in range(grayscale.shape[1]):
            binary[i, j] = 255 if grayscale[i, j] >= threshold else 0
    return binary

image_path = "img.jpg"  
image = cv2.imread(image_path)

grayscale_image = rgb_to_grayscale(image)

binary_image = grayscale_to_binary(grayscale_image)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Plotar imagens
plt.figure(figsize=(15, 5))  

plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title("Imagem Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(grayscale_image, cmap="gray")
plt.title("Imagem em Cinza")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap="gray")
plt.title("Imagem Binária")
plt.axis("off")

plt.tight_layout()
plt.show()