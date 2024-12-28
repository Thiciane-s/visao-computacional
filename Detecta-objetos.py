
from ultralytics import YOLO
import cv2
import math 
from pyfirmata import Arduino
import time
from datetime import datetime

# Definindo a porta do arduino
port = 'COM5'
board = Arduino(port)

time.sleep(2)  # Tempo para inicializar a comunicação com o Arduino

# Portas de saída no Arduino para cada LED
greenLed = 6
yeLed = 7
redLed = 8


# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# modelo
model = YOLO("yolo-Weights/yolov8n.pt")

# Arquivo para registrar logs
log_file = "event_log.csv"

# Criar o cabeçalho do arquivo de log (se não existir)
with open(log_file, 'a') as file:
    file.write("Data/Hora,Classe,Confiança\n")


# object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confiança da predição
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confiança --->",confidence)

            # class name
            cls = int(box.cls[0])
            print("Nome Classe -->", classNames[cls])

            # detalhes object 
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)


            # Sinaliza a presença de determinados objetos e acende os leds correspondentes
            if (classNames[cls] == "person"  ):
                board.digital[redLed].write(1)
            elif(classNames[cls] == "cell phone"):
                board.digital[yeLed].write(1)
            elif(classNames[cls] == "dog"):
                board.digital[greenLed].write(1)
            # Desliga os leds
            board.digital[yeLed].write(0)
            board.digital[redLed].write(0)
            board.digital[greenLed].write(0)

             # Registrar o evento no arquivo de log
            with open(log_file, 'a') as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp},{classNames[cls]},{confidence}\n")

    # Desliga a webcam ao pressionar a tecla q
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()