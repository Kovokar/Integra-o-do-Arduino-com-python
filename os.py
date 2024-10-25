import cv2
from cvzone.FaceDetectionModule import FaceDetector
import serial
import time

# Inicializa o detector de faces
detector = FaceDetector()

# Inicializa a captura de vídeo da webcam (câmera 0)
video = cv2.VideoCapture(0)

# Tenta conectar ao Arduino
try:
    arduino = serial.Serial('COM3', 9600)  # Certifique-se de que a porta COM está correta
    time.sleep(2)  # Espera 2 segundos para garantir que a conexão está estabilizada

    # Verifica se a conexão foi estabelecida corretamente
    if arduino.is_open:
        print("Conexão com o Arduino estabelecida com sucesso!")
    else:
        print("Falha ao conectar com o Arduino.")
        exit()  # Sai do programa se a conexão não for bem-sucedida

except serial.SerialException as e:
    print(f"Erro ao tentar conectar com o Arduino: {e}")
    exit()  # Sai do programa se ocorrer um erro ao tentar conectar

# Loop de detecção de faces e comunicação com o Arduino
time.sleep(2)
while True:
    ret, frame = video.read()
    img, bboxs = detector.findFaces(frame)

    if bboxs:
        print("Face detected")
        arduino.write(b'0')  # Envia sinal para o Arduino
    else:
        print("No face detected")
        arduino.write(b'1')  # Envia sinal diferente se não houver rosto

    # Mostra o frame com a detecção
    cv2.imshow("Face Detection", img)

    # Sai do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura e fecha as janelas
video.release()
cv2.destroyAllWindows()
arduino.close()
