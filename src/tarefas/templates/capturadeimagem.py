import cv2

# 0 representa a webcam padrão do computador (se tiver outra câmera externa, tente 1)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erro: Não foi possível acessar a webcam.")
else:
    print("Pressione 's' para salvar a foto ou 'q' para sair.")

    while True:
        # Lê cada quadro (frame) da câmera
        ret, frame = camera.read()

        if not ret:
            print("Falha ao capturar imagem.")
            break

        # Exibe a imagem em uma janela
        cv2.imshow("Captura de Imagem - OpenCV", frame)

        # Aguarda 1ms por uma tecla pressionada
        tecla = cv2.waitKey(1) & 0xFF

        if tecla == ord('s'):
            cv2.imwrite("foto_capturada.png", frame)
            print("Foto salva com sucesso como 'foto_capturada.png'!")
        elif tecla == ord('q') or tecla == 27:  # 'q' ou tecla ESC
            break


camera.release()
cv2.destroyAllWindows()