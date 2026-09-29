import cv2 as cv

def show_image(img_path):
    img = cv.imread(img_path)

    cv.namedWindow("Questao 1")
    cv.imshow("Questao 1", img)
    
    cv.waitKey()

    cv.destroyAllWindows()

def main():
    img_path = "./images/Lena.jpg"
    show_image(img_path)

if __name__ == "__main__":
    main()