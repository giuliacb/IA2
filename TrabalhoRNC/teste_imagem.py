import torch
import cv2
import pyttsx3 #biblioteca de fala 
import os

# Carregar modelo YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5m', trust_repo=True)

# Lista de objetos escolares
objetos_escolares = {"backpack", "book", "scissors", "clock", "bottle", "cup", "laptop", "cell phone", "suitcase", "keyboard"}

# Inicializar TTS
engine = pyttsx3.init()

# Caminho da imagem
#imagem_path = "C:/Users/Giulia/IA2/IA2/TrabalhoRNC/mochila.jpg" 
imagem_path = r"C:\Users\Giulia\IA2\IA2\TrabalhoRNC\6209955c-8f2e-4678-9699-e00e64476cc7.png"

# Verificar se a imagem existe
if not os.path.exists(imagem_path):
    print("Erro: imagem não encontrada.")
    exit()

# Carregar e redimensionar a imagem
img = cv2.imread(imagem_path)
img = cv2.resize(img, (640, 640))  # Tamanho esperado pelo YOLOv5

# Rodar detecção
results = model(img)
labels = results.xyxyn[0][:, -1].numpy()
nomes = results.names
detectados = set()

def traduzir(objeto):
    traducoes = {
        "backpack": "mochila",
        "book": "livro",
        "scissors": "tesoura", 
        "clock": "relógio",
        "bottle": "garrafa",
        "cup": "copo", 
        "laptop": "notebook",
        "cell phone": "celular",
        "suitcase": "mochila/mala",
        "keyborad": "teclado",
        "handbag": "mochila/bolsa"
    }
    return traducoes.get(objeto, objeto)

print("\n🔎 Objetos detectados na imagem:")
for label in labels:
    objeto = nomes[int(label)]
    print(f" - {objeto}")
    if objeto in objetos_escolares:
        detectados.add(objeto)

# Falar objetos escolares detectados
print("\n📢 Resultado:")
if detectados:
    for item in detectados:
        print(f"Detectado: {item} ({traduzir(item)})")
        engine.say(item)
    engine.runAndWait()
else:
    print("Nenhum objeto escolar detectado.")

# Exibir imagem com boxes
img_anotada = results.render()[0]
cv2.imshow("Resultado da Detecção", img_anotada)
cv2.waitKey(0)
cv2.destroyAllWindows()
