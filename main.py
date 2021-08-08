import cv2 as cv  # pacote opencv-python
# opencv depende também do pacote numpy

webcam = cv.VideoCapture(0)

if webcam.isOpened():
    print("Webcam conectada.")
    validacao, frame = webcam.read()

    while validacao:
        validacao, frame = webcam.read()
        cv.imshow("Captura de Video da Vida", frame)
        key = cv.waitKey(16)
        if key == 27:  # ESC
            break
    cv.imwrite("FotoMarcos.png", frame)
print("Webcam Desconectada.")
webcam.release()
cv.destroyAllWindows()
