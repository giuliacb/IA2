## 🎒 Identificador de Objetos da Mochila Escolar

Projeto de acessibilidade que utiliza **Redes Neurais Convolucionais (RNC)** para identificar, em tempo real, objetos escolares dentro de uma mochila, fornecendo **feedback sonoro** ao usuário. A ideia é apoiar **pessoas com deficiência visual** no ambiente educacional.

---

## 📌 Objetivo

Criar uma prova de conceito utilizando **YOLOv5**, que:

* Detecta objetos escolares via webcam.
* Filtra apenas os itens relevantes.
* Fala os nomes dos objetos detectados, em português ou inglês.
* Pode futuramente identificar **objetos faltando**.

---

## 🧠 Tecnologias Utilizadas

| Componente                 | Ferramenta / Biblioteca                        |
| -------------------------- | ---------------------------------------------- |
| Rede Neural Convolucional  | YOLOv5 (pré-treinado - versão `yolov5s`)       |
| Processamento de imagem    | OpenCV                                         |
| Texto para fala (TTS)      | pyttsx3 (offline)                              |
| Framework de Deep Learning | PyTorch                                        |
| Interface                  | Tkinter                                        |
| Dataset                    | COCO (80 classes, incluindo objetos escolares) |

---

## 📸 Arquitetura Funcional

[Webcam] 
   ↓ 
[Redimensionamento e pré-processamento] 
   ↓ 
[YOLOv5 - Detecção de objetos] 
   ↓ 
[Filtro: apenas objetos escolares] 
   ↓ 
[Texto para fala com pyttsx3] 
   ↓ 
[Usuário ouve os objetos detectados]

---

## ✅ Pré-requisitos

Tenha o Python 3.12 instalado e, no terminal (PowerShell):
-> pip install torch torchvision opencv-python pyttsx3 yolov5

---

## 🗂️ Estrutura dos Arquivos

mochila_identificador/
├── main_gui.py     # Script da interface gráfica do usuário (graphic user interface)
├── main.py         # Script principal para detecção + feedback sonoro
├── README.md       # Este arquivo

---

## 🚀 Como Executar

1. Clone ou copie os arquivos para um diretório local:
2. No terminal, acesse a pasta do projeto:

cd <caminho do seu repositorio que contém o projeto>
python <nome do seu arquivo>


3. Aguarde o carregamento do modelo.
4. Mantenha a webcam apontada para os objetos escolares.
5. Pressione **`q`** para sair.

---

## 🖼️ Interface Gráfica com Tkinter

Além da versão por terminal, o projeto inclui uma **interface gráfica amigável**, construída com **Tkinter**, para facilitar o uso por qualquer pessoa — especialmente em situações onde a linha de comando não é ideal.

### Recursos da interface:

* ✅ **Botão “Iniciar Detecção”**: ativa a webcam e começa o processo de identificação.
* 🛑 **Botão “Sair”**: encerra a execução com segurança.
* 🌐 **Botão “Alternar Idioma” (PT/EN)**: muda entre os idiomas **Português** e **Inglês** para o feedback sonoro.
* 📦 **Lista de Objetos Esperados**: mostra os itens que deveriam estar na mochila.
* 🚨 **Aviso de Faltando**: se algum item da lista não for detectado, o sistema avisa por voz, por exemplo:

  * **Português**: “Faltando mochila”
  * **Inglês**: “backpack is missing”

### Como usar:

* Execute o script `main_gui.py`:
-> python main_gui.py
 
* Use os botões para iniciar, mudar idioma e encerrar o sistema.
* A detecção é mostrada visualmente com *bounding boxes* na janela da câmera e informada por áudio.

---

## 🧾 Objetos Detectáveis

O modelo detecta os seguintes objetos escolares (do dataset COCO):

* `"backpack"` (mochila)
* `"book"` (livro)
* `"scissors"` (tesoura)
* (Outros podem ser simulados, como `"pen"` usando `"cell phone"`)

---

## 🔊 Acessibilidade

O feedback é feito por voz com a biblioteca **`pyttsx3`**, que funciona offline e lê os nomes dos objetos detectados em tempo real.

---

## 🛠️ Melhorias Futuras

* Identificar objetos faltando com base em uma lista de materiais esperados.
* Suporte a múltiplos idiomas.
* Treinamento personalizado com fotos reais de materiais escolares.

---

## 👩‍💻 Desenvolvedora

**Giulia e João**
Projeto de Redes Neurais Artificiais (RNA)
Curso de Ciência da Computação – IESB
