import cv2 as cv
from matplotlib import pyplot as plt

def show_image():
    # Lendo a imagem
    img = cv.imread("./images/Lena.jpg")

    # Imagem 1: Convertendo para a escala de cinza
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Imagem 2: Aplicando filtro de Blur
    img_blur = cv.blur(img_gray, (5, 5))

    # Imagem 3: Aplicando filtro Gaussiano
    img_gaussiano = cv.GaussianBlur(img_gray, (5, 5), 0)

    # Imagem 4: Aplicando filtro de Mediana
    img_mediana = cv.medianBlur(img_gray, 5)

    # Exibindo as imagens
    plt.subplot(2, 2, 1)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Escala de Cinza')
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(img_blur, cmap='gray')
    plt.title('Filtro de Blur')
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(img_gaussiano, cmap='gray')
    plt.title('Filtro Gaussiano')
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(img_mediana, cmap='gray')
    plt.title('Filtro de Mediana')
    plt.axis("off")

    plt.tight_layout()
    plt.show()

def main():
    show_image()

if __name__ == "__main__":
    main()