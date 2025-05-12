import torch
import cv2
import pyttsx3

# Carregar o modelo YOLOv5 pré-treinado
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)

# Lista de objetos escolares comuns no dataset COCO
objetos_escolares = {"backpack", "book", "pen", "pencil", "scissors"}

# Inicializar mecanismo de texto para fala
engine = pyttsx3.init()

# Captura de vídeo pela webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao acessar a webcam.")
    exit()

print("Sistema iniciado. Pressione 'q' para sair.")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detecção com o modelo
    results = model(frame)
    labels = results.xyxyn[0][:, -1].numpy()
    nomes = results.names
    detectados = set()

    for label in labels:
        objeto = nomes[int(label)]
        if objeto in objetos_escolares:
            detectados.add(objeto)

    # Mostrar resultados com bounding boxes
    anotado = results.render()[0]
    cv2.imshow("Objetos Escolares Detectados", anotado)

    # Emitir áudio com objetos encontrados
    for item in detectados:
        engine.say(f"{item}")
    if detectados:
        engine.runAndWait()

    # Sair com 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
