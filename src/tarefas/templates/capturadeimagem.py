import cv2

# Abrir a câmera
camera = cv2.VideoCapture(0)

while True:
    # Capturar imagem
    sucesso, imagem = camera.read()

    if not sucesso:
        print("Erro ao acessar a câmera")
        break

    # Mostrar imagem
    cv2.imshow("Minha Webcam", imagem)

    # Pressione ESPAÇO para capturar
    if cv2.waitKey(1) == 32:
        cv2.imwrite("captura.jpg", imagem)
        print("Imagem salva com sucesso!")
        break

# Encerrar câmera
camera.release()
cv2.destroyAllWindows()