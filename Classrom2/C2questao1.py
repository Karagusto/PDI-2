# Questão 1 (diferenciar imagens)
import cv2

cv2.__version__

def differ(img1, img2):
    d1 = cv2.absdiff(img1, img2)
    return d1

webcam = cv2.VideoCapture(0) #usar webcam
janela = "Tela de Captura"

cv2.namedWindow(janela, cv2.WINDOW_AUTOSIZE)


first = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY)



while True:

    last = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY) #Utilizey em grayscale para melhor visualização

    cv2.imshow(janela, differ(first, last))

    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.destroyWindow(janela)
        break


print("Fim")


# AND, OR, NOT, XOR

lena = cv2.imread("lena.png")
baboon = cv2.imread("baboon.png")
cv2.imshow("AND", cv2.bitwise_and(lena, lena))
cv2.imshow("OR", cv2.bitwise_or(lena, lena))
cv2.imshow("XOR", cv2.bitwise_xor(lena,lena))
cv2.imshow("NOT", cv2.bitwise_not(lena,lena))
