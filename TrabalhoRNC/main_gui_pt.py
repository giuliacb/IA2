import torch
import cv2
import pyttsx3
import threading
import tkinter as tk
from tkinter import messagebox

# Carregar o modelo YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', trust_repo=True)

# Lista de objetos escolares esperados
objetos_esperados = {"backpack", "book", "scissors", "clock", "bottle", "cup", "laptop", "cell phone", "suitcase"}

# Inicializar TTS
engine = pyttsx3.init()

# Definir voz em português
def definir_voz_portugues():
    for voz in engine.getProperty('voices'):
        if 'pt' in voz.id.lower() or 'brazil' in voz.id.lower():
            engine.setProperty('voice', voz.id)
            break

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

executando = False

def detectar_objetos(status_label):
    global executando
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        messagebox.showerror("Erro", "Não foi possível acessar a webcam.")
        return

    status_label.config(text="Detectando objetos escolares...")

    while executando:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        labels = results.xyxyn[0][:, -1].numpy()
        nomes = results.names
        detectados = set()

        for label in labels:
            objeto = nomes[int(label)]
            if objeto in objetos_esperados:
                detectados.add(objeto)

        faltando = objetos_esperados - detectados

        anotado = results.render()[0]
        cv2.imshow("Objetos Escolares", anotado)

        if detectados:
            for item in detectados:
                falar(traduzir(item))

        status_msg = "Detectados: " + ", ".join([traduzir(o) for o in detectados])
        if faltando:
            status_msg += "\nFaltando: " + ", ".join([traduzir(o) for o in faltando])
        status_label.config(text=status_msg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    status_label.config(text="Detecção encerrada.")
    cap.release()
    cv2.destroyAllWindows()

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
        "suitcase": "mochila/mala"  # pode ajustar conforme necessário
    }
    return traducoes.get(objeto, objeto)

def iniciar(status_label):
    global executando
    if not executando:
        executando = True
        threading.Thread(target=detectar_objetos, args=(status_label,), daemon=True).start()

def parar():
    global executando
    executando = False

def criar_interface():
    definir_voz_portugues()

    janela = tk.Tk()
    janela.title("🎒 Identificador de Objetos Escolares")
    janela.geometry("430x250")
    janela.resizable(False, False)

    titulo = tk.Label(janela, text="Identificador de Objetos Escolares", font=("Arial", 14, "bold"))
    titulo.pack(pady=10)

    status = tk.Label(janela, text="Clique em 'Iniciar Detecção' para começar.", fg="blue", justify="left", wraplength=400)
    status.pack(pady=5)

    objetos_txt = tk.Label(janela, text=f"Esperados: {', '.join([traduzir(o) for o in objetos_esperados])}", fg="black")
    objetos_txt.pack()

    btn_iniciar = tk.Button(janela, text="Iniciar Detecção", bg="green", fg="white", font=("Arial", 12),
                            command=lambda: iniciar(status))
    btn_iniciar.pack(pady=5)

    btn_parar = tk.Button(janela, text="Sair", bg="red", fg="white", font=("Arial", 12),
                          command=lambda: (parar(), janela.destroy()))
    btn_parar.pack(pady=5)

    janela.mainloop()

if __name__ == "__main__":
    criar_interface()
