import cv2 as cv

def show_images(img_path):
    img = cv.imread(img_path)

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('Imagem Original', img)

    cv.imshow('Imagem em Escala Cinza', img_gray)

    cv.waitKey()
    cv.destroyAllWindows()

def main():
    img_path = './images/Lena.jpg'
    show_images(img_path)

if __name__ == "__main__":
    main() 